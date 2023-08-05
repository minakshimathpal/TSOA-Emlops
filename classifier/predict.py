from typing import Tuple, Dict
import lightning as L
import torch
import hydra
from omegaconf import DictConfig

from classifier.utils import pylogger

log = pylogger.get_pylogger(__name__)


#@utils.task_wrapper
def predict(cfg: DictConfig) -> Tuple[dict, dict]:
    # set seed for random number generators in pytorch, numpy and python.random
    if cfg.get("seed"):
        L.seed_everything(cfg.seed, workers=True)

    log.info(f"Instantiating datamodule <{cfg.data._target_}>")
    datamodule: LightningDataModule = hydra.utils.instantiate(cfg.data)

    log.info(f"Instantiating model <{cfg.model._target_}>")
    model: LightningModule = hydra.utils.instantiate(cfg.model)


    log.info(f"Instantiating trainer <{cfg.trainer._target_}>")
    trainer: Trainer = hydra.utils.instantiate(cfg.trainer)


    log.info("Starting Prediction!")
    preds = trainer.predict(model=model, datamodule=datamodule, return_predictions = True,  ckpt_path=cfg.test_ckpt_path)
    log.info(f"Prediction Values <{preds}>")
    print(f'Top-k[{cfg.model.topk}] preds : {preds}')


@hydra.main(version_base="1.3", config_path="../configs", config_name="predict.yaml")
def main(cfg: DictConfig):
    # Run inference on the model
    predict(cfg)


if __name__ == "__main__":
    main()