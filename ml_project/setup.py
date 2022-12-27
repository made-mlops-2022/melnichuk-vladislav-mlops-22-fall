from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Homework_#1",
    packages=find_packages(),
    version="1.0.0",
    description="MLOps homework #1 project: classification",
    author="MelnichukVladislav",
    entry_points={
        "console_scripts": [
            "ml_example_train = ml_example.train_pipeline_start:train_pipeline_command"
        ]
    },
    install_requires=requirements,
    license="MIT",
)
