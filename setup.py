from setuptools import setup

setup(
    install_requires=["fabric3", "numpy", "argparse", "pillow"],
    entry_points={
        "console_scripts": [
            "pir = main:main"
        ]
    }
)