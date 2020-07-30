from setuptools import setup, find_packages


setup(
    name="lab_clerk",
    version="0.0.6",
    description="Experiment Tracking and Evaluation",
    author="Phillip Wenig",
    author_email="phillip.wenig@hpi.de",
    license='unlicensed',
    packages=find_packages(),
    test_suite="tests",
    install_requires=[
        'pandas',
        'numpy'
    ]
)
