from setuptools import setup

setup(
    name="estimate-sol",
    description="Script to estimate the size of solidity source code",
    url="https://github.com/CoinFabrik/estimate-sol",
    author="Coinfabrik team",
    version="0.0.0",
    packages=(),
    python_requires=">=3.8",
    install_requires=[
        "lib-estimate-sol"
    ],
    license="mit",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        "console_scripts": [
            "estimate-sol = estimate_sol.estimate_script:run",
        ],
    },
)