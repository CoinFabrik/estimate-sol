# estimate-sol

## Requirements

 * python >= 3.8

## Package generation

This repository contains 2 python projects, each with its own setup.py. The `lib` folder has all the code. The `cmd` folder has the command-line package. You need both to run the hole thing.

## Releases

Releases of the projects are published in pypi.

## Installation

On ubuntu it requires to install wheels either via `sudo apt install python3-wheel` (if installed in the system wide python) or, if installed in a virtual env, do `pip install wheel` inside de corresponding virtual env before installing.

Install by running `pip install estimate-sol` (`sudo pip3 install estimate-sol` to install system wide in ubuntu). Similar instructions should work for other systems.

## Estimating solidity audits

After installing, you can run `estimate-sol` to estimate solidity audits. See different options by running `estimate-sol --help`.

The defaults for the number of lines per week, the number of punctuations per week, the dependencies multiplier and the assembly multiplier can be set via the following environment variables:
 * ESTIMATE_SOL_DEFAULT_LINES_PER_WEEK
 * ESTIMATE_SOL_DEFAULT_PUNCTUATIONS_PER_WEEK
 * ESTIMATE_SOL_DEFAULT_DEPENDENCIES_MULTIPLIER
 * ESTIMATE_SOL_DEFAULT_ASSEMBLY_MULTIPLIER

## Run tests

To run all the tests run `python3 -m unittest -v` at the `lib` folder. See python documentation on how to run unit tests at: https://docs.python.org/3/library/unittest.html#command-line-interface
