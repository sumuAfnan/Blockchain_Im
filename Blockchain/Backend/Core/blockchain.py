from Blockchain.Backend.Core.blockheader import BlockHeader
from Blockchain.Backend.Core.block import Block
from Blockchain.Backend.Util.util import hash256
import time
import json


VERSION = 1
ZERO_HASH = "0" * 64
TARGET = "0000"


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.add_block(1, ZERO_HASH)

    def add_block(self, blockHeight, prevBlockHash):

        # Create a new block header
        version = VERSION
        timestamp = int(time.time())
        bits = "ffff0000"  # Placeholder for the actual difficulty target

        # transactions = []  # Placeholder for actual transactions
        Txs = ["A is sending {blockHeight} coins to B"]

        merkle_root = hash256(
            json.dumps(Txs).encode('utf-8')
        )

        block_header = BlockHeader(
            version,
            prevBlockHash,
            merkle_root,
            timestamp,
            bits
        )

        block_header.mine(TARGET)

        # Create a new block
        new_block = Block(
            blockHeight,
            1,
            block_header.__dict__,
            Txs
        ).__dict__

        # Add the new block to the blockchain
        self.chain.append(new_block)

        print(
            f"Block {blockHeight} added to the blockchain "
            f"with hash: {block_header.blockHash}"
        )

    def get_last_block(self):
        return self.chain[-1]

    def add_next_block(self):
        last_block = self.get_last_block()

        new_block_height = last_block["Height"] + 1

        new_prev_hash = last_block["BlockHeader"]["blockHash"]

        self.add_block(new_block_height, new_prev_hash)

    def print(self):
        print(json.dumps(self.chain, indent=4))