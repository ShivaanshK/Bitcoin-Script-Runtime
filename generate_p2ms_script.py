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

# Generate M keys
keys = [ec.generate_private_key(curve=ec.SECP256K1()) for _ in range(M)]

# Select N keys at random for signatures
selected_keys = random.sample(keys, N)

# Generate signatures
signatures = {key: "0x" + key.sign(b"UTXOs", signature_algorithm=ec.ECDSA(hashes.SHA256())).hex() for key in selected_keys}

# Shuffle keys to randomize the order of public keys
random.shuffle(keys)

# Generate mapping based on shuffled keys
mapping = "0x"
for key in selected_keys:
    index = keys.index(key)
    mapping += hex(index)[2:]

# Generate public keys hex representation
public_keys_hex = ["0x" + key.public_key().public_bytes(encoding=serialization.Encoding.DER, format=serialization.PublicFormat.SubjectPublicKeyInfo).hex() for key in keys]

# Assemble the script
script_pub_key = f" {N} " + " ".join(public_keys_hex) + f" {M} OP_CHECKMULTISIG"

# Assemble signatures based on the mapping
script_sig_mapping = f"{mapping} " + " ".join(signatures[key] for key in selected_keys)  # Order by selected_keys which are already in the mapping
script_sig_no_mapping = "OP_0 " + " ".join(signatures[key] for key in selected_keys)

# Write the P2MS script to a file
with open("p2ms_script_mapping", "w") as file:
    file.write(script_sig_mapping + " " + script_pub_key)

with open("p2ms_script", "w") as file:
    file.write(script_sig_no_mapping + " " + script_pub_key)

print(f"P2MS script for {N} of {M} MS with mapping written to file 'p2ms_script_mapping'")
print(f"P2MS script for {N} of {M} MS without mapping written to file 'p2ms_script'")
