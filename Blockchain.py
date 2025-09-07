from hashlib import sha256
from time import time
import json

class Block:
    def __init__(self, timestamp=None, data=None):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.nonce = 0
        self.difficulty = 5
        self.prevHash = None
        self.hash = self.getHash()


    def getHash(self):
        hash = sha256()
        hash.update(str(self.prevHash).encode('utf-8'))
        hash.update(str(self.timestamp).encode('utf-8'))
        hash.update(str(self.nonce).encode('utf-8'))
        hash.update(str(self.data).encode('utf-8'))
        return hash.hexdigest()

    
    def mine(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.getHash()


class Blockchain:
    def __init__(self):
        self.chain = [Block(str(int((time()))))]

    
    def getLastBlock(self):
        return self.chain[len(self.chain)-1]

    
    def addBlock(self, block):
        block.prevHash = self.getLastBlock().hash
        block.hash = block.getHash()
        block.mine(block.difficulty)

        self.chain.append(block)


    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            prevBlock = self.chain[i-1]

            if (currentBlock.prevHash != prevBlock.hash) or (currentBlock.hash != currentBlock.getHash()):
                return False

        return True


    def __repr__(self):
        return json.dumps([{'data': item.data, 'timestamp': item.timestamp, 'nonce': item.nonce, 'hash': item.hash, 'prevHash': item.prevHash} for item in self.chain], indent=4)


