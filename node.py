from blockchain import Blockchain
from uuid import uuid4
from utility.verification import Verification 
from wallet import Wallet 

class Node: 

    def __init__(self):
        # self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    # Get the User Input for a transaction amount
    def get_transaction_value(self):
        """ Return input of user (new amount) as a float. """
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('You transaction amount please: '))
        return tx_recipient, tx_amount

    def get_user_choice(self): 
        user_input = input('Your choice: ')
        return user_input

    def print_blockchain_elements(self):
        # Print out the current blockchain
        for block in self.blockchain.chain: 
            print('Outputting the Block')
            print(block)
        else: 
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True

        while waiting_for_input: 
            print('\nPlease Choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output blockchain value')
            print('4: Check transaction validity')
            print('5: Create a Wallet')
            print('6: Load a Wallet')
            print('7: Save the Key')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print('Added Transaction!')
                else: 
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print('Mining failed. Do you have a wallet?')
            elif user_choice == '3':
                # Print out the current blockchain
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid!')
                else: 
                    print('There are invalid transactions')
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print('Invalid Blockchain!')
                waiting_for_input = False
                break
            print('Balance of {}: {:6.2f}'.format(self.wallet.public_key, self.blockchain.get_balance()))
        else: 
            print('User left!')
        
        print('Done!')

if __name__ == '__main__':
    node = Node()
    node.listen_for_input()