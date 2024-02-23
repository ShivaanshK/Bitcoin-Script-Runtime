#!/usr/bin/env pypy3

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
import sys, random

# N of M Multisig
N = int(sys.argv[1])
M = int(sys.argv[2])

# Check values of M and N
if M < 1 or N < 1:
    print("N and M must be > 1!")
    sys.exit(1)
if M > 15:
    print("M can be 15 at max!")
    sys.exit(1)
elif N > M:
    print("N has to be less than M!")
    sys.exit(1)

# Generate M keys and N signatures at random
keys = []
signatures = []
mapping = "0x"

for i in range(M):
    private_key = ec.generate_private_key(curve=ec.SECP256K1())
    keys.append(private_key)

selected_keys = random.sample(keys, N)
for key in selected_keys:
    index = keys.index(key)
    mapping += hex(index)[2:]
    signature = "0x" + key.sign(b"UTXOs", signature_algorithm=ec.ECDSA(hashes.SHA256())).hex()
    signatures.append(signature)

# Generate Script
public_keys_hex = ["0x" + key.public_key().public_bytes(encoding=serialization.Encoding.DER, format=serialization.PublicFormat.SubjectPublicKeyInfo).hex() for key in keys]
script_pub_key = f" {N} " + " ".join(public_keys_hex) + f" {M} OP_CHECKMULTISIG"
# Dummy Stack element is first element - We will use this to implement a mapping
script_sig_mapping = f"{mapping} " + " ".join(signatures)
script_sig_no_mapping = "OP_0 " + " ".join(signatures)

# Write the P2MS script to a file
with open("p2ms_script_mapping", "w") as file:
    file.write(script_sig_mapping + script_pub_key)

with open("p2ms_script", "w") as file:
    file.write(script_sig_no_mapping + script_pub_key)

print("P2MS script with mapping written to file 'p2ms_script_mapping'")
print("P2MS script without mapping written to file 'p2ms_script'")
