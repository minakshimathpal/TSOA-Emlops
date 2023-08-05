from setuptools import find_packages, setup

setup(
    name="classifier",
    version="0.0.1",
    description="PyTorch Lightning Cat vs Dog Classifier",
    author="Minakshi",
    author_email="",
    url="https://github.com/user/project",
    install_requires=["lightning", "hydra-core"],# this will look for requirements.txt
    packages=find_packages(), # find all the packages in your module 
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "classifier_train = classifier.train:main",
            "classifier_eval = classifier.eval:main",
            "classifier_predict = classifier.predict:main"
        ]
    },
)