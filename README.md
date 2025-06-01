# Minimal Blockchain Implementation

This is a minimal implementation of a blockchain in python language with mining the blocks, checking chain validity and hash validity and proof of work (default difficulty = 3) . It simulates how blocks are created, linked, validated, and mined using Proof-of-Work.


## Block Structure

Each block in this minimal  blockchain implementation contains the following components:

- **Index**: Position of the block in the chain.
- **Timestamp**: The exact time when the block was created.
- **Sender**: The sender's identity (can be name or something else) .
- **Receiver**: The recipient's identity (can be name or something else ) .
- **Amount**: The value (may be money or coins)  transferred from sender to receiver.
- **Previous Hash**: The hash of the previous block. This links the current block to the one before it.
- **Current Hash**: The hash generated from the block's contents (including index ,sender, receiver, amount, timestamp, previous hash, and nonce). It is used to uniquely identify the block and thus keeps an integrity in the block chain. Any change in the block’s contents will result in a different current hash and hence tampering can be easily detected as all blocks are connected through hashes.
- **Nonce** : A number that is incremented during the mining process to find a valid hash that satisfies the difficulty level.

This structure ensures immutability: changing any part of the block will change its hash, and hence breaking the chain.



## Validation Logic

The following checks are performed to validate the blockchain:

- **valid_hash**: The block’s contents are rehashed, and the result is compared with the stored "curr_hash". If they differ, the block is invalid.
- **check_valid_chain**: It check if throughout the chain if the "prev_hash" in the current block must match the "curr_hash" of the previous block , each block's "curr_hash" must meet the defined difficulty and also checks if each hash is valid using valid_hash. This ensures chain continuity , proof-of-work validity and data integrity .

If any block fails these checks, the blockchain is considered invalid. The above checks also display respective errors if blockchain is not valid.



##  Proof-of-Work :

The Proof-of-Work mechanism enforces computational effort before a block is added:

- A **difficulty level** is set (in this project its default value is 3) which tells how many starting 0's must be in "bin_hash" of the block to be added , determined by incrementing over the "nonce".
- The **nonce** value is initialized (in this project by 0 ) and repeatedly incremented until a hash is found that meets the difficulty condition.
- Once a valid hash is found, the block is considered mined and can be added to the chain.

This process makes the blockchain tamper-resistant, as modifying a single block would require re-mining all subsequent blocks, which is computationally expensive and not possible.


## Summary

This project demonstrates the core principles behind blockchain technology:
- Tamper-proof data linking using cryptographic hashes
- Transaction structure with sender, receiver, timestamp and amount
- Integrity checking via validation logic
- Proof-of-Work to simulate mining
