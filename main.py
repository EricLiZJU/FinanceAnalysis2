import random
import collections
import itertools
import logging
import argparse
import os
import socket
import networkx as nx
import typing
import web3
import web3.types
import web3._utils.filters
from pip._internal.utils.logging import setup_logging
from web3 import Web3, EthereumTesterProvider, HTTPProvider
from eth_utils import event_abi_to_log_topic
from utils import erc20

from analyses import get_arbitrage_if_exists

ERC20_TRANSFER_TOPIC = event_abi_to_log_topic(erc20.events.Transfer().abi)
ERC20_TRANSFER_TOPIC_HEX = '0x' + ERC20_TRANSFER_TOPIC.hex()

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'
                            '29d793709e424f02b2c6ce2501f0dd61'))
print(w3.is_connected())

txn_hash = '7550be86887701dcbd4e28f8ae25fe4c9140a3f34984f14df6851f1b1747c0f3'
txn_hash_hex = '0x' + txn_hash
receipt = w3.eth.get_transaction_receipt(txn_hash_hex)
txns = []
for r in receipt['logs']:
    if r['topics'][0].hex() == ERC20_TRANSFER_TOPIC_HEX:
        try:
            txns.append(erc20.events.Transfer().process_log(r))
        except:
            continue
arb = get_arbitrage_if_exists(
    w3,
    bytes.fromhex(txn_hash),
    txns,
)

print(arb)

file = open('arbitrage_info.txt', 'w')
file.write(str(arb))
file.close()