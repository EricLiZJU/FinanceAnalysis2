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

arbCount = 0

block = w3.eth.get_block(20282055)
transactionsList = block['transactions']
for i in transactionsList:
    transactionsHashHex = i.hex()
    transactionsHash = transactionsHashHex[2:]
    receipt = w3.eth.get_transaction_receipt(transactionsHashHex)
    txns = []
    for r in receipt['logs']:
       if r['topics'][0].hex() == ERC20_TRANSFER_TOPIC_HEX:
         try:
                txns.append(erc20.events.Transfer().process_log(r))
         except:
             continue
    arb = get_arbitrage_if_exists(
        w3,
        bytes.fromhex(transactionsHash),
        txns,
    )
    if arb != None:
        print(arb)
        arbCount += 1

print(arbCount)
