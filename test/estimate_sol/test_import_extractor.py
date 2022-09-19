import unittest

from estimate_sol.import_extractor import extract_imports

class TestImportExtractor(unittest.TestCase):

    # See https://docs.soliditylang.org/en/v0.8.15/grammar.html#a4.SolidityParser.importDirective for import spec
    # See https://topmonks.github.io/solidity_quick_ref/ for a condensed version:
    # import "path";
    # import * as name from "path";
    # import { name as alias|name, ... } from "path";
    # import "path" as namespace;
    SAMPLE_CODE = """\
pragma solidity 0.6.12;

import "@openzeppelin/contracts/math/SafeMath.sol" as safemath;
import 
    "synthetix/contracts/interfaces/IAddressResolver.sol";
import "../interfaces/ISwap.sol";import "./SynthSwapper.sol";

import {CollabFundsHandlerBase} from  "../CollabFundsHandlerBase.sol";
import {
ICollabFundsDrainable,
ICollabFundsShareDrainable
} from "../ICollabFundsDrainable.sol";

import { BaseCloseCrossContract as Banker } from "../BaseCloseCrossContract.sol";

import './Roles.sol';
import * as util from '../utilities.sol';

contract CollabFundsReceiver is ReentrancyGuard, CollabFundsHandlerBase, ICollabFundsDrainable, ICollabFundsShareDrainable {

    uint256 public totalEthReceived;
    uint256 public totalEthPaid;
}
"""

    EXPECTED_IMPORTS = {
        "@openzeppelin/contracts/math/SafeMath.sol",
        "synthetix/contracts/interfaces/IAddressResolver.sol",
        "../interfaces/ISwap.sol",
        "./SynthSwapper.sol",
        "../CollabFundsHandlerBase.sol",
        "../ICollabFundsDrainable.sol",
        "../BaseCloseCrossContract.sol",
        "./Roles.sol",
        "../utilities.sol",
    }

    def test_extract_imports(self):
        self.assertSetEqual(self.EXPECTED_IMPORTS, extract_imports(self.SAMPLE_CODE))