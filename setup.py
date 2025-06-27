from setuptools import setup, find_packages

setup(
    name="autonomous-dq-agent",
    version="0.1.0",
    author="Sudheer",
    description="A cloud-ready, ML-powered, rule-driven data quality agent.",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pyyaml",
        "scikit-learn",
        "sqlalchemy",
        "boto3"
    ],
    entry_points={
        "console_scripts": [
            "dq-agent=dq_agent.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)