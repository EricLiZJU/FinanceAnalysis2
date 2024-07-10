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

from analyses import get_arbitrage_if_exists, ERC20Transaction, ERC20TransactionArgs

ERC20_TRANSFER_TOPIC = event_abi_to_log_topic(erc20.events.Transfer().abi)
ERC20_TRANSFER_TOPIC_HEX = '0x' + ERC20_TRANSFER_TOPIC.hex()

print(ERC20_TRANSFER_TOPIC_HEX)

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'
                            '29d793709e424f02b2c6ce2501f0dd61'))
print(w3.is_connected())

block = w3.eth.get_block(4654718)
file1 = open('block_info.txt', 'w')
file1.write(str(block))
file1.close()

transactionsHashList = block['transactions']
"""
for i in transactionsHashList:
    #print(i)
    txn_hash1 = bytes.hex(i)
    txn_hash_hex1 = '0x' + txn_hash1
    txn_hash = txn_hash_hex1
    btxn_hash = bytes.fromhex(txn_hash[2:])
    receipt = w3.eth.get_transaction_receipt(txn_hash)
    #print(receipt)
    txns = []
    for r in receipt['logs']:
        print(r['topics'][0])
        if r['topics'][0] == ERC20_TRANSFER_TOPIC:
            try:
                txns.append(erc20.events.Transfer().processLog(r))
            except:
                continue

    print(txns)
    arb = get_arbitrage_if_exists(
        w3,
        bytes.fromhex(txn_hash1),
        txns,
    )

    print(arb)

"""
txn_hash1 = 'ba48fc0e658bfd927370ae0dda6fd37793e504e90289cd8216e986ebf714699b'
txn_hash_hex1 = '0x' + txn_hash1
print(txn_hash1)
print(txn_hash_hex1)
txn_hash = txn_hash_hex1
btxn_hash = bytes.fromhex(txn_hash[2:])
receipt = w3.eth.get_transaction_receipt(txn_hash)
print(receipt)
txns = []
for r in receipt['logs']:
    print(r['topics'][0])
    print(r['topics'][0].hex())
    if r['topics'][0].hex() == ERC20_TRANSFER_TOPIC_HEX:
        print(erc20.events.Transfer().processLog(r))
        try:
            txns.append(erc20.events.Transfer().processLog(r))
        except:
            continue
print(txns)
arb = get_arbitrage_if_exists(
    w3,
    bytes.fromhex(txn_hash1),
    txns,
)

print(arb)
