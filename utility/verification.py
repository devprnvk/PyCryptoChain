from utility.hash_util import hash_string_256, hash_block
from wallet import Wallet

class Verification: 

    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        print(guess_hash)
        return guess_hash[0:2] == '00'

    @classmethod
    def verify_chain(cls, blockchain):
        """ Verify the Chain for Block chain blocks and values"""
        for (index, block) in enumerate(blockchain): 
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid')
                return False
        return True
    
    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):
        """Verify a transaction by checking for sufficient chains

        Arguments:
            :transaction: the transaction that should be verified.
        """
        if check_funds:
            sender_balance = get_balance()
            return sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)
    
    @classmethod 
    def verify_transactions(cls, open_transactions, get_balance):
        # is_valid = True
        # for tx in open_transactions: 
        #     if (verify_transaction(tx)):
        #         is_valid = True
        #     else: 
        #         is_valid = False
        # return is_valid
        return all([cls.verify_transaction(tx, get_balance, False) for tx in open_transactions])

   