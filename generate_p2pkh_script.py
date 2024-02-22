#!/usr/bin/env pypy3

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from Crypto.Hash import RIPEMD160, SHA256

private_key = ec.generate_private_key(curve=ec.SECP256K1())
public_key = private_key.public_key().public_bytes(encoding=serialization.Encoding.DER, format=serialization.PublicFormat.SubjectPublicKeyInfo)
hash = SHA256.new()
hash.update(public_key)
hash2 = RIPEMD160.new()
hash2.update(hash.digest())
public_key_hash = hash2.hexdigest()
signature = private_key.sign(b"UTXOs", signature_algorithm=ec.ECDSA(hashes.SHA256())).hex()
print("Public Key:", "0x" + public_key.hex())
print("Public Key Hash:", "0x" + public_key_hash)
print("Signature:", "0x" + signature)

p2pkh_script = f"0x{signature} 0x{public_key.hex()} OP_DUP OP_HASH160 0x{public_key_hash} OP_EQUALVERIFY OP_CHECKSIG"

# Write the P2PKH script to a file
with open("p2pkh_script", "w") as file:
    file.write(p2pkh_script)

print("P2PKH script written to file 'p2pkh_script'")
 