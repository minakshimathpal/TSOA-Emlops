from typing import Any, Dict, Optional, Tuple
from lightning.pytorch.utilities.types import EVAL_DATALOADERS

import torch
from lightning import LightningDataModule
from torch.utils.data import ConcatDataset, DataLoader, Dataset, random_split
from torchvision.datasets import CIFAR10
from torchvision.transforms import transforms


class CIFARDataModule(LightningDataModule): # we will instantiate this class in cifar.yaml
    """Example of LightningDataModule for CIFAR10
      dataset.

    A DataModule implements 6 key methods:
        def prepare_data(self):
            # things to do on 1 GPU/TPU (not on every GPU/TPU in DDP)
            # download data, pre-process, split, save to disk, etc...
        def setup(self, stage):
            # things to do on every process in DDP
            # load data, set variables, etc...
        def train_dataloader(self):
            # return train dataloader
        def val_dataloader(self):
            # return validation dataloader
        def test_dataloader(self):
            # return test dataloader
        def teardown(self):
            # called on every process in DDP
            # clean up after fit or test

    This allows you to share a full dataset without explaining how to download,
    split, transform and process the data.

    Read the docs:
        https://lightning.ai/docs/pytorch/latest/data/datamodule.html
    """

    def __init__(
            self,
            data_dir: str= "data/",
            train_val_test_split: Tuple[int,int,int] = (55_000,5_000,10_000),
            batch_size:int = 64,
            num_worker:int = 0,
            pin_memory: bool= False
            ):
        super().__init__()  ## these parameters in init will go to cifar.yaml in configs/data/
        # call this to save init parama to the checkpoints
        # this line also allows to access init params with 'self.hparams' attribute

        self.save_hyperparameters(logger=False)
        self.transforms = transforms.Compose([transforms.ToTensor(),
                                        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

        self.data_train: Optional[Dataset] = None
        self.data_val:   Optional[Dataset] = None
        self.data_test:  Optional[Dataset] = None

    @property
    def num_classes(self):
        """
        return number of classes to be classified
        """
        return 2
    
    def prepare_data(self) -> None:
        """
        Download data if needed.

        Do not use it to assign state (self.x = y).
        """
        CIFAR10(self.hparams.data_dir, train=True , download=True)
        CIFAR10(self.hparams.data_dir, train=False, download=True)

    def setup(self, stage:Optional[str] =None):
        """Load data. Set variables: `self.data_train`, `self.data_val`, `self.data_test`.

        This method is called by lightning with both `trainer.fit()` and `trainer.test()`, so be
        careful not to execute things like random split twice!
        """
        # load and split datasets only if not loaded already
        if not self.data_train and not self.data_val and not self.data_test:
            trainset= CIFAR10(self.hparams.data_dir,train=True,transform=self.transforms)
            testset=  CIFAR10(self.hparams.data_dir,train=True,transform=self.transforms)

            dataset= ConcatDataset(datasets=[trainset,testset])

            self.data_train,self.data_val,self.data_test = random_split(dataset=dataset,
                                                                        lengths= self.hparams.train_val_test_split,
                                                                        generator= torch.Generator().manual_seed(42))
    def train_dataloader(self):
        return DataLoader(dataset=self.data_train,
            batch_size=self.hparams.batch_size,
            num_workers=self.hparams.num_workers,
            pin_memory=self.hparams.pin_memory,
            shuffle=True,
        )
    
    def val_dataloader(self):
        return DataLoader(
            dataset=self.data_val,
            batch_size=self.hparams.batch_size,
            num_workers=self.hparams.num_workers,
            pin_memory=self.hparams.pin_memory,
            shuffle=False,
        )

    def test_dataloader(self):
        return DataLoader(
            dataset=self.data_test,
            batch_size=self.hparams.batch_size,
            num_workers=self.hparams.num_workers,
            pin_memory=self.hparams.pin_memory,
            shuffle=False,
        )

    def teardown(self, stage: Optional[str] = None):
        """Clean up after fit or test."""
        pass

    def state_dict(self):
        """Extra things to save to checkpoint."""
        return {}

    def load_state_dict(self, state_dict: Dict[str, Any]):
        """Things to do when loading checkpoint."""
        pass


if __name__ == "__main__":
    _ = CIFARDataModule()