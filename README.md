# Audit-Tools

## Requirements

 * python3
 * On ubuntu, install the python3-setuptools package (or install setuptools via pip in your env) and python3-wheel (or install wheel via pip in your env) to make the packages

## Package generation

Run `python3 setup.py bdist_wheel` to generate the .whl file.

## Releases

You can download the project releases from [google-drive](https://drive.google.com/drive/folders/1B_cCyAvCLNOJ9jIDNO84FdDx4rQ8FXy6)

## Installation

 1. Activate the proper env to do the install (optional)
 1. Install:
    1. Via pip: Run `pip install path/to/generated.whl` (if using the .egg generated via setup.py it will be in the dist/ directory).
    1. Via easy_install: Run `python3 -m easy_install path/to/generated.egg` (if using the .egg generated via setup.py, it will be in the dist/ directory).

## Estimating solidity audits

After installing the egg, you can run `estimate-sol` to estimate solidity audits. See different options by running `estimate-sol --help`.

## Estimating clarity audits

For now, in order to estimate clarity audits, you can use the `estimate-clar.py` script. This will not be installed when installing the .egg.

## Run tests

To run all the tests run `python3 -m unittest -v`. See python documentation on how to run unit tests at: https://docs.python.org/3/library/unittest.html#command-line-interface
