from merkletools import *


def merkle(txns):
    mt = MerkleTools(hash_type="sha256")
    for txn in txns.split('\n'):
        txn = txn.strip()
        txn = txn.strip(',')
        txn = txn.strip('"')
        mt.add_leaf(txn)
    mt.make_tree()
    return mt


def mproof(mt, index):
    p = mt.get_proof(int(index))
    return p

