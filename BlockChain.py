import hashlib
import string
import random
import time
import sys

class Block :
    def __init__(self,index,sender,receiver,amount,previous_hash,nonce):
        self.index = index
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.prev_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = nonce
        self.curr_hash ,self.bin_hash = self.compute_hash()
    
    def compute_hash(self):
        curr_hash = hashlib.sha256(f"{self.timestamp}{self.index}{self.sender}{self.receiver}{self.amount}{self.prev_hash}{self.nonce}".encode()).hexdigest()
        bin_hash = bin(int(curr_hash, 16))[2:].zfill(256)

        return curr_hash , bin_hash

    def __str__(self):
        return (
            f"Index : {self.index}\n"
            f"Nonce : {self.nonce}\n"
            f"Timestamp : {self.timestamp}\n"
            f"Sender : {self.sender}\n"
            f"Receiver : {self.receiver}\n"
            f"Amount Sent : {self.amount} USD\n"
            f"Previous Hash : {self.prev_hash}\n"
            f"Current Hash  : {self.curr_hash}"
            )



class BlockChain :
    def __init__(self,sender,receiver,amount,difficulty= 3):
        print(" "*30 + "Creating a new BlockChain......\n")
        self.chain = []
        self.create_genesis(sender,receiver,amount)
        self.difficulty = difficulty
   
    
    def create_genesis(self,sender,receiver,amount):
        print(" "*30 + "Adding Genesis Block.........")
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        previous_hash = hashlib.sha256(random_string.encode()).hexdigest()
        self.chain.append(Block(0,sender,receiver,amount,previous_hash,0))
        print("~"*30 + " Genesis Block Added Successfully " + "~"*30 + "\n")

    def add_block(self,sender,receiver,amount):
        prev_index = len(self.chain) - 1
        previous_hash = self.chain[-1].curr_hash
        new_block = Block(prev_index + 1,sender,receiver,amount,previous_hash,0)
        self.mine_block(new_block,self.difficulty)
        if(self.check_valid_chain(self.difficulty)):
            self.chain.append(new_block)
        print("~"*30 + f" Block {prev_index + 1} added to the chain successfully " + "~"*30 + "\n")
        
        

    def mine_block(self,block,difficulty):
        print("~"*30 + f" Mining Block {block.index} " + "~"*30)
        temp_bin_hash = block.bin_hash
        while(not (temp_bin_hash.startswith("0" * difficulty))):
            block.nonce += 1
            block.curr_hash ,block.bin_hash = block.compute_hash()
            temp_bin_hash = block.bin_hash
        print("~"*30 + f" Block {block.index} mined sucessfully " + "~"*30 )
        
    def valid_hash(self,block):
        expected_hash = block.curr_hash
        computed_hash , _= block.compute_hash()
        if(expected_hash == computed_hash):
            return 1
        else :
            return 0
    

    def check_valid_chain(self,difficulty):
        print(" "*30 + " Checking Chain Validity.......... ")
        l = len(self.chain)
        for i in range(1,l):
                if (self.chain[i].prev_hash != self.chain[i-1].curr_hash):
                    print("~"*30 + f" Linkage broken between Blocks {self.chain[i].index - 1} and {self.chain[i].index} !! ......" + "~"*30)
                    sys.exit(0)
                if not(self.chain[i].bin_hash.startswith("0" * self.difficulty)):
                    print("~"*30 + f" Block {self.chain[i].index} not mined properly !! ...... " + "~"*30)
                    sys.exit(0)
                if not(self.valid_hash(self.chain[i])):
                    print("~"*30 + f" Tampering Detected at Block {i} !! ....... " + "~"*30)
                    sys.exit(0)

        print("~"*30 + " The BlockChain linkage is Valid ! " + "~"*30)
        return 1

    def display_chain(self):
        print("The BlockChain :\n")    
        _ = self.check_valid_chain(self.difficulty)   
        print("-"*80)
        print("Genesis Block :\n")
        for block in  self.chain :
            print(block)
            print("-"*80)
        



# Initialing the chain with  user-defined genesis block

chain = BlockChain("Bob","Carol","40k")

# Adding more blocks
chain.add_block("Carol","Harrington","20k")
chain.add_block("Steve","Bob","100k")
chain.add_block("Steve","Carol","30k")

# Display the chain
chain.display_chain()


# Tampering with the block indexed 1 and checking if it can catch the error :
# chain.chain[1].index = 100
# chain.display_chain()













