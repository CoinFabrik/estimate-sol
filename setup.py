from setuptools import setup, find_packages
from audit_tools import __VERSION__

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="estimate-sol",
    description="Script to estimate the size of solidity source code",
    url="https://github.com/CoinFabrik/estimate-sol",
    author="Coinfabrik team",
    version=__VERSION__,
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    license="mit",
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "estimate-sol = estimate_sol.estimate_script:run",
        ],
    },
)