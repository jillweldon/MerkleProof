from merkle import *
import sys


def main():
    # command line: python3 main.py arg1 arg2 arg3
    # transaction file: sys.argv[1]
    # index of transaction to check: sys.argv[2]
    # hash of transaction to check: sys.argv[3]
    n = len(sys.argv)
    if n >= 2:
        with open(sys.argv[1], 'r') as f:
            txns = f.read()
        f.close()
        tree = merkle(txns)
        print(tree.get_merkle_root())

        if n >= 3:
            proof = mproof(tree, sys.argv[2])
            if n == 4:
                if tree.validate_proof(proof, sys.argv[3], tree.get_merkle_root()):
                    print("Valid")
                else:
                    print("Invalid")
    else:
        print("Invalid Arguments")


if __name__ == '__main__':
    main()
