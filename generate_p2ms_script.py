from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from Crypto.Hash import RIPEMD160, SHA256
import sys, random

# N of M Multisig
N = int(sys.argv[1])
M = int(sys.argv[2])

# Check values of M and N
if M < 1 or N < 1:
    print("N and M must be > 1!")
    sys.exit(1)
if M > 20:
    print("M can be 20 at max!")
    sys.exit(1)
elif N > M:
    print("N has to be less than M!")
    sys.exit(1)

# Generate M keys and N signatures at random
keys = []
signatures = []

for i in range(M):
    private_key = ec.generate_private_key(curve=ec.SECP256K1())
    keys.append(private_key)

selected_keys = random.sample(keys, N)
for key in selected_keys:
    signature = "0x" + key.sign(b"UTXOs", signature_algorithm=ec.ECDSA(hashes.SHA256())).hex()
    signatures.append(signature)

# Generate Script
public_keys_hex = ["0x" + key.public_key().public_bytes(encoding=serialization.Encoding.DER, format=serialization.PublicFormat.SubjectPublicKeyInfo).hex() for key in keys]
script_sig = f" {N} " + " ".join(public_keys_hex) + f" {M} OP_CHECKMULTISIG"
# Dummy Stack element is first element - We will use this to implement a mapping
script_pub_key = "OP_0 " + " ".join(signatures)
p2ms = script_pub_key + script_sig

# Write the P2MS script to a file
with open("p2ms_script", "w") as file:
    file.write(p2ms)

print("P2MS script written to file 'p2ms_script'")

