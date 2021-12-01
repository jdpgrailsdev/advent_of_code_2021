"""Package setup."""
from setuptools import find_packages, setup

setup(
    name="advent_of_code",
    version="0.0.1",
    description="Advent of Code 2021",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "click==8.0.1",
        "requests==2.26.0",
    ],
    entry_points={
        "console_scripts": [
            "advent_of_code = advent_of_code.cli:cli",
        ]
    },
)
