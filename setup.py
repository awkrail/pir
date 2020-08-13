from setuptools import setup

setup(
    name="pir",
    version="0.0.1",
    description="A small package",
    author="misogil0116",
    install_requires=["fabric3", "numpy", "argparse", "pillow"],
    entry_points={
        "console_scripts": [
            "pir = main:main"
        ]
    }
)