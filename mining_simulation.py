import hashlib
import datetime
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        attempts = 0
        start_time = time.time()
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.compute_hash()
            attempts += 1
        end_time = time.time()
        mining_time = end_time - start_time
        print(f"Block mined with nonce={self.nonce}")
        print(f"Hash: {self.hash}")
        print(f"Nonce attempts: {attempts}")
        print(f"Time taken: {mining_time:.4f} seconds")

# Example usage:
difficulty = 4  # Number of leading zeros required in hash
block = Block(1, datetime.datetime.utcnow(), "Sample block data", "0")
block.mine_block(difficulty)
