import json
from web3 import Web3   


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]


abi=json.loads('[{"constant":false,"inputs":[{"name":"_number","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address=web3.toChecksumAddress("0x5b23Add49a67e0F3709E701328E6E612DF156f2d")

contract=web3.eth.contract(address=address,abi=abi)

print(contract.functions.get().call())

h=contract.functions.set(100).transact()

web3.eth.waitForTransactionReceipt(h)

print("transaction hash : "+str(h))
print(contract.functions.get().call())




