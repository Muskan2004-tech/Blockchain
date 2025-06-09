import hashlib
import datetime
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": str(self.timestamp),
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.utcnow(), "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(
            index=prev_block.index + 1,
            timestamp=datetime.datetime.utcnow(),
            data=data,
            previous_hash=prev_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"  Timestamp      : {block.timestamp}")
            print(f"  Data           : {block.data}")
            print(f"  Nonce          : {block.nonce}")
            print(f"  Previous Hash  : {block.previous_hash}")
            print(f"  Hash           : {block.hash}\n")

if __name__ == "__main__":
    bc = Blockchain()
    bc.add_block("Block 1 Data")
    bc.add_block("Block 2 Data")

    print("Original chain:\n")
    bc.display_chain()
    print("Chain valid?", bc.is_chain_valid())

    print("\nTampering with Block 1...")
    bc.chain[1].data = "HACKED DATA"
    bc.chain[1].hash = bc.chain[1].compute_hash()

    print("\nAfter tampering:\n")
    bc.display_chain()
    print("Chain valid after tampering?", bc.is_chain_valid())
