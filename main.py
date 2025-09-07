from Blockchain import Blockchain, Block
from time import time

JeChain = Blockchain()

JeChain.addBlock(Block(str(int(time())), ({"from": "John", "to": "Bob", "amount": 100})))

print(JeChain)