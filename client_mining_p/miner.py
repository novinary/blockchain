import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 
def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain 6
    leading zeroes?
    """
    # encode a guess
    guess = f'{last_proof}{proof}'.encode()
    # hash the guess
    guess_hash = hashlib.sha256(guess).hexdigest()
    # return true if the last 6 digits of the hash = 0s
    return guess_hash[:6] == "000000"

def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm
    - Find a number p' such that hash(pp') contains 4 leading
    zeroes, where p is the previous p'
    - p is the previous proof, and p' is the new proof
    """
    # start our proof at zero
    proof = 0

    # increment proof by 1 until valid proof returns true
    while valid_proof(last_proof, proof) is False:
        proof += 1

    # once a valid proof is reached return it
    return proof


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server 
        res = requests.get(f"{node}/last-proof")
        last_proof = res.json()['last_proof']
        print(last_proofs)
        # and look for a new one
        new_proof = proof_of_work(last_proof)
        # TODO: When found, POST it to the server {"proof": new_proof}
        proof_submission = requests.post(f"{node}/mine", json={"proof": new_proof})
        proof_res = proof_submission.json()
        # TODO: If the server responds with 'New Block Forged'
        if proof_res['message'] == 'New Block Forged':
        # add 1 to the number of coins mined and print it.
            coins_mined += 1
        # Otherwise,print the message from the server.
        else:
            print(proof_res['Oops, an error occured.'])
    
