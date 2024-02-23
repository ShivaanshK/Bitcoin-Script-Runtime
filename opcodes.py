import stack
from Crypto.Hash import RIPEMD160, SHA256, SHA1
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives import hashes

global_stack: stack.Stack = stack.Stack()
alt_stack: stack.Stack = stack.Stack()


def encode_stack_element(value: str) -> bytes:
	if value.startswith("0x"):
		return bytes.fromhex(value[2:])
	else:
		return value.encode("utf-8")


def OP_0_impl() -> None:
	global_stack.push("")


def OP_FALSE_impl() -> None:
	OP_0_impl()


def OP_PUSHDATA1_impl() -> None:
	return


def OP_PUSHDATA2_impl() -> None:
	return


def OP_PUSHDATA4_impl() -> None:
	return


def OP_1NEGATE_impl() -> None:
	global_stack.push("-1")


def OP_RESERVED_impl() -> None:
	return


def OP_1_impl() -> None:
	global_stack.push("1")


def OP_TRUE_impl() -> None:
	OP_1_impl()


def OP_2_impl() -> None:
	global_stack.push("2")


def OP_3_impl() -> None:
	global_stack.push("3")


def OP_4_impl() -> None:
	global_stack.push("4")


def OP_5_impl() -> None:
	global_stack.push("5")


def OP_6_impl() -> None:
	global_stack.push("6")


def OP_7_impl() -> None:
	global_stack.push("7")


def OP_8_impl() -> None:
	global_stack.push("8")


def OP_9_impl() -> None:
	global_stack.push("9")


def OP_10_impl() -> None:
	global_stack.push("10")


def OP_11_impl() -> None:
	global_stack.push("11")


def OP_12_impl() -> None:
	global_stack.push("12")


def OP_13_impl() -> None:
	global_stack.push("13")


def OP_14_impl() -> None:
	global_stack.push("14")


def OP_15_impl() -> None:
	global_stack.push("15")


def OP_16_impl() -> None:
	global_stack.push("16")


def OP_NOP_impl() -> None:
	return


def OP_VER_impl() -> None:
	return


############## Control Flow ################
BLOCK_NESTING = 1  # current depth of nested statement blocks, value of 1 is the "root." incremented by parser, NOT interpreter
EXEC_STACK: list[bool] = [True]  # execution history of nested blocks


def ctrl_flow_exec(instr: str) -> bool:
	if instr in {"OP_IF", "OP_NOTIF", "OP_ELSE", "OP_ENDIF"}:
		return True
	else:
		global EXEC_STACK
		return EXEC_STACK[-1]


def OP_IF_impl() -> None:
	global EXEC_STACK, BLOCK_NESTING
	if EXEC_STACK[-1]:
		cond = global_stack.pop()
		EXEC_STACK.append(convert_to_bool(cond))
	BLOCK_NESTING += 1


def OP_NOTIF_impl() -> None:
	global EXEC_STACK, BLOCK_NESTING
	if EXEC_STACK[-1]:
		cond = global_stack.pop()
		EXEC_STACK.append(not convert_to_bool(cond))
	BLOCK_NESTING += 1


def OP_ELSE_impl() -> None:
	global BLOCK_NESTING, EXEC_STACK
	if len(EXEC_STACK) == 1:
		raise ValueError("OP_ELSE located outside of OP_IF block")
	if BLOCK_NESTING == len(EXEC_STACK):
		EXEC_STACK[-1] = not EXEC_STACK[-1]


def OP_ENDIF_impl() -> None:
	global BLOCK_NESTING, EXEC_STACK
	if len(EXEC_STACK) == 1:
		raise ValueError("OP_ENDIF located outside of OP_IF block")
	if len(EXEC_STACK) == BLOCK_NESTING:
		EXEC_STACK.pop()
	BLOCK_NESTING -= 1


def OP_VERIFY_impl() -> None:
	top_item: str = global_stack.pop()
	if convert_to_bool(top_item):
		return
	else:
		raise ValueError("INVALID TRANSACTION - OP_VERIFY returned FALSE")


def OP_RETURN_impl() -> None:
	raise ValueError("INVALID TRANSACTION - OP_RETURN statement reached")


########## STACK ##############

def OP_TOALTSTACK_impl() -> None:
	alt_stack.push(global_stack.pop())


def OP_FROMALTSTACK_impl() -> None:
	global_stack.push(alt_stack.pop())


def OP_2DROP_impl() -> None:
	global_stack.pop()
	global_stack.pop()


def OP_2DUP_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	global_stack.push(top_item_2)
	global_stack.push(top_item)
	global_stack.push(top_item_2)
	global_stack.push(top_item)


def OP_3DUP_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	top_item_3: str = global_stack.pop()
	global_stack.push(top_item_3)
	global_stack.push(top_item_2)
	global_stack.push(top_item)
	global_stack.push(top_item_3)
	global_stack.push(top_item_2)
	global_stack.push(top_item)


def OP_2OVER_impl() -> None:
	x4, x3, x2, x1 = global_stack.pop_multi(4)
	global_stack.push_multi(x1, x2, x3, x4, x1, x2)


def OP_2ROT_impl() -> None:
	x6, x5, x4, x3, x2, x1 = global_stack.pop_multi(6)
	global_stack.push_multi(x3, x4, x5, x6, x1, x2)


def OP_2SWAP_impl() -> None:
	x4, x3, x2, x1 = global_stack.pop_multi(4)
	global_stack.push_multi(x3, x4, x1, x2)


def OP_IFDUP_impl() -> None:
	x = global_stack.top()
	if x != '0':
		global_stack.push(x)


def OP_DEPTH_impl() -> None:
	depth: int = global_stack.depth()
	global_stack.push(str(depth))


def OP_DROP_impl() -> None:
	global_stack.pop()


def OP_DUP_impl() -> None:
	top_item: str = global_stack.pop()
	global_stack.push(top_item)
	global_stack.push(top_item)


def OP_NIP_impl() -> None:
	top_item: str = global_stack.pop()
	global_stack.pop()
	global_stack.push(top_item)


def OP_OVER_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	global_stack.push(top_item_2)
	global_stack.push(top_item)
	global_stack.push(top_item_2)


def OP_PICK_impl() -> None:
	narg = global_stack.pop()
	n = to_int(narg)
	global_stack.push(global_stack.contents[-1 - n])


def OP_ROLL_impl() -> None:
	narg = global_stack.pop()
	n = to_int(narg)
	new_top = global_stack.contents.pop(-1 - n)
	global_stack.push(new_top)


def OP_ROT_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	top_item_3: str = global_stack.pop()
	global_stack.push(top_item_2)
	global_stack.push(top_item)
	global_stack.push(top_item_3)


def OP_SWAP_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	global_stack.push(top_item)
	global_stack.push(top_item_2)


def OP_TUCK_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	global_stack.push(top_item)
	global_stack.push(top_item_2)
	global_stack.push(top_item)


######### Splice ############
def OP_CAT_impl() -> None:
	return


def OP_SUBSTR_impl() -> None:
	return


def OP_LEFT_impl() -> None:
	return


def OP_RIGHT_impl() -> None:
	return


def OP_SIZE_impl() -> None:
	return


def OP_INVERT_impl() -> None:
	return


def OP_AND_impl() -> None:
	return


def OP_OR_impl() -> None:
	return


def OP_XOR_impl() -> None:
	return


def OP_EQUAL_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	if (top_item == top_item_2):
		OP_1_impl()
	else:
		OP_0_impl()


def OP_EQUALVERIFY_impl() -> None:
	OP_EQUAL_impl()
	OP_VERIFY_impl()


def OP_RESERVED1_impl() -> None:
	return


def OP_RESERVED2_impl() -> None:
	return


########### Arithmetic ##############
def to_int(i: str) -> int:
	if i == "":
		return 0
	try:
		return int(i)
	except ValueError:
		raise ValueError(f"INVALID OPERAND: {i}")


def OP_1ADD_impl() -> None:
	i = to_int(global_stack.pop())
	global_stack.push(str(i + 1))
	return


def OP_1SUB_impl() -> None:
	i = to_int(global_stack.pop())
	global_stack.push(str(i - 1))
	return


def OP_2MUL_impl() -> None:
	# disabled
	return


def OP_2DIV_impl() -> None:
	# disabled
	return


def OP_NEGATE_impl() -> None:
	i = to_int(global_stack.pop())
	global_stack.push(str(-1 * i))
	return


def OP_ABS_impl() -> None:
	i = to_int(global_stack.pop())
	global_stack.push(str(abs(i)))
	return


def OP_NOT_impl() -> None:
	top_item: str = global_stack.pop()
	try:
		item_to_int = to_int(top_item)
		if item_to_int == 0:
			OP_1_impl()
		else:
			OP_0_impl()
	except:
		OP_0_impl()


def OP_0NOTEQUAL_impl() -> None:
	inp = global_stack.pop()
	global_stack.push("0" if inp == "0" else "1")


def OP_ADD_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	try:
		item_to_int: int = int(top_item)
		item_to_int_2: int = int(top_item_2)
		sum: int = item_to_int + item_to_int_2
		global_stack.push(str(sum))
	except:
		raise ValueError("INVALID TYPES FOR OP_ADD")


def OP_SUB_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	try:
		item_to_int: int = int(top_item)
		item_to_int_2: int = int(top_item_2)
		difference: int = item_to_int_2 - item_to_int
		global_stack.push(str(difference))
	except:
		raise ValueError("INVALID TYPES FOR OP_SUB")


def OP_MUL_impl() -> None:
	# disabled
	return


def OP_DIV_impl() -> None:
	# disabled
	return


def OP_MOD_impl() -> None:
	# disabled
	return


def OP_LSHIFT_impl() -> None:
	# disabled
	return


def OP_RSHIFT_impl() -> None:
	# disabled
	return


def convert_to_bool(stack_item: str) -> bool:
	if stack_item == '' or stack_item == b'':
		return False
	try:
		item_to_int = int(stack_item)
		if item_to_int == 0:
			return False
		return True
	except ValueError:
		return True


def OP_BOOLAND_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	bool_result = convert_to_bool(top_item) and convert_to_bool(top_item_2)
	if bool_result:
		OP_1_impl()
	else:
		OP_0_impl()


def OP_BOOLOR_impl() -> None:
	top_item: str = global_stack.pop()
	top_item_2: str = global_stack.pop()
	bool_result = convert_to_bool(top_item) or convert_to_bool(top_item_2)
	if bool_result:
		OP_1_impl()
	else:
		OP_0_impl()


def OP_NUMEQUAL_impl() -> None:
	arg1 = global_stack.pop()
	arg2 = global_stack.pop()
	result = "0"
	try:
		num1 = to_int(arg1)
		num2 = to_int(arg2)
		result = "1" if num1 == num2 else "0"
	except ValueError:
		pass
	global_stack.push(result)


def OP_NUMEQUALVERIFY_impl() -> None:
	OP_NUMEQUAL_impl()
	OP_VERIFY_impl()


def OP_NUMNOTEQUAL_impl() -> None:
	arg1 = global_stack.pop()
	arg2 = global_stack.pop()
	result = "1"
	try:
		num1 = to_int(arg1)
		num2 = to_int(arg2)
		result = "0" if num1 == num2 else "1"
	except ValueError:
		pass
	global_stack.push(result)


def OP_LESSTHAN_impl() -> None:
	barg = global_stack.pop()
	aarg = global_stack.pop()
	result = "0"
	try:
		a = to_int(aarg)
		b = to_int(barg)
		result = "1" if a < b else "0"
	except ValueError:
		pass
	global_stack.push(result)


def OP_GREATERTHAN_impl() -> None:
	barg = global_stack.pop()
	aarg = global_stack.pop()
	result = "0"
	try:
		a = to_int(aarg)
		b = to_int(barg)
		result = "1" if a > b else "0"
	except ValueError:
		pass
	global_stack.push(result)


def OP_LESSTHANOREQUAL_impl() -> None:
	barg = global_stack.pop()
	aarg = global_stack.pop()
	result = "0"
	try:
		a = to_int(aarg)
		b = to_int(barg)
		result = "1" if a <= b else "0"
	except ValueError:
		pass
	global_stack.push(result)


def OP_GREATERTHANOREQUAL_impl() -> None:
	barg = global_stack.pop()
	aarg = global_stack.pop()
	result = "0"
	try:
		a = to_int(aarg)
		b = to_int(barg)
		result = "1" if a >= b else "0"
	except ValueError:
		pass
	global_stack.push(result)


def OP_MIN_impl() -> None:
	barg = global_stack.pop()
	aarg = global_stack.pop()
	result = "0"
	try:
		a = to_int(aarg)
		b = to_int(barg)
		result = str(min(a, b))
	except ValueError:
		pass
	global_stack.push(result)


def OP_MAX_impl() -> None:
	barg = global_stack.pop()
	aarg = global_stack.pop()
	result = "0"
	try:
		a = to_int(aarg)
		b = to_int(barg)
		result = str(max(a, b))
	except ValueError:
		pass
	global_stack.push(result)


def OP_WITHIN_impl() -> None:
	maxarg = global_stack.pop()
	minarg = global_stack.pop()
	xarg = global_stack.pop()
	result = "0"
	try:
		max = to_int(maxarg)
		min = to_int(minarg)
		x = to_int(xarg)
		result = "1" if min <= x < max else "0"
	except ValueError:
		pass
	global_stack.push(result)


######### Crypto ############


def OP_RIPEMD160_impl() -> None:
	top_item: str = global_stack.pop()
	hash = RIPEMD160.new()
	hash.update(encode_stack_element(top_item))
	global_stack.push("0x" + hash.hexdigest())


def OP_SHA1_impl() -> None:
	top_item: str = global_stack.pop()
	hash = SHA1.new()
	hash.update(encode_stack_element(top_item))
	global_stack.push("0x" + hash.hexdigest())


def OP_SHA256_impl() -> None:
	top_item: str = global_stack.pop()
	hash = SHA256.new()
	hash.update(encode_stack_element(top_item))
	global_stack.push("0x" + hash.hexdigest())


def OP_HASH160_impl() -> None:
	OP_SHA256_impl()
	OP_RIPEMD160_impl()


def OP_HASH256_impl() -> None:
	OP_SHA256_impl()
	OP_SHA256_impl()


def OP_CODESEPARATOR_impl() -> None:
	return


def OP_CHECKSIG_impl() -> None:
	public_key_bytes: bytes = encode_stack_element(global_stack.pop())
	sig_bytes: bytes = encode_stack_element(global_stack.pop())

	public_key: ec.EllipticCurvePublicKey = load_der_public_key(public_key_bytes)

	try:
		public_key.verify(
			sig_bytes,
			b"UTXOs",
			ec.ECDSA(hashes.SHA256())
		)
		OP_1_impl()
	except:
		OP_0_impl()


def OP_CHECKSIGVERIFY_impl() -> None:
	OP_CHECKSIG_impl()
	OP_VERIFY_impl()


def OP_CHECKMULTISIG_impl() -> None:
	# Pop Public Keys
	m: int = int(global_stack.pop())
	public_keys: list[bytes] = []
	for i in range(m):
		public_keys.append(encode_stack_element(global_stack.pop()))

	# Pop Signatures
	n: int = int(global_stack.pop())
	signatures: list[bytes] = []
	for i in range(n):
		signatures.append(encode_stack_element(global_stack.pop()))

	# Pop Dummy Element (our map optimization). If hex value: use it; Else: ignore the mapping
	mapping: str = global_stack.pop()

	if (mapping[0:2] == "0x"):
		mapping = mapping[2:]
		# Check if public key is used twice in the mapping
		if len(set(mapping)) != len(mapping):
			OP_0_impl()
			return
		# Check each signature against public key specified in the map
		for i in range(len(signatures)):
				try:
					public_key_loaded: ec.EllipticCurvePublicKey = load_der_public_key(public_keys[-(int(mapping[-(i + 1)], 16) + 1)])
					public_key_loaded.verify(
						signatures[i],
						b"UTXOs",
						ec.ECDSA(hashes.SHA256())
					)
				except:
					OP_0_impl()
					return
	else:
		# Check each signature against each public key. A public key can only match one signature.
		for signature in signatures:
			success: bool = False
			for i in range(m):
				try:
					public_key_loaded: ec.EllipticCurvePublicKey = load_der_public_key(public_keys[i])
					public_key_loaded.verify(
						signature,
						b"UTXOs",
						ec.ECDSA(hashes.SHA256())
					)
					public_keys.pop(i)
					success = True
					break
				except:
					pass
			if not success:
				OP_0_impl()
				return

	OP_1_impl()


def OP_CHECKMULTISIGVERIFY_impl() -> None:
	OP_CHECKMULTISIG_impl()
	OP_VERIFY_impl()


def OP_NOP1_impl() -> None:
	return


def OP_CHECKLOCKTIMEVERIFY_impl() -> None:
	return


def OP_NOP2_impl() -> None:
	return


def OP_CHECKSEQUENCEVERIFY_impl() -> None:
	return


def OP_NOP3_impl() -> None:
	return


def OP_NOP4_impl() -> None:
	return


def OP_NOP5_impl() -> None:
	return


def OP_NOP6_impl() -> None:
	return


def OP_NOP7_impl() -> None:
	return


def OP_NOP8_impl() -> None:
	return


def OP_NOP9_impl() -> None:
	return


def OP_NOP10_impl() -> None:
	return


def OP_CHECKSIGADD_impl() -> None:
	public_key_bytes: bytes = encode_stack_element(global_stack.pop())
	n: int = int(global_stack.pop())
	sig_bytes: bytes = encode_stack_element(global_stack.pop())

	if len(sig_bytes) == 0:
		global_stack.push(str(n))
		return	

	public_key: ec.EllipticCurvePublicKey = load_der_public_key(public_key_bytes)

	try:
		public_key.verify(
			sig_bytes,
			b"UTXOs",
			ec.ECDSA(hashes.SHA256())
		)
		global_stack.push(str(n + 1))
	except:
		raise ValueError("INVALID TRANSACTION - OP_CHECKSIGADD failed")


def OP_INVALIDOPCODE_impl() -> None:
	return


def is_opcode(opcode: str) -> bool:
	return opcode in OPCODES


OPCODES = {
	'OP_0': OP_0_impl,
	'OP_FALSE': OP_FALSE_impl,
	'OP_PUSHDATA1': OP_PUSHDATA1_impl,
	'OP_PUSHDATA2': OP_PUSHDATA2_impl,
	'OP_PUSHDATA4': OP_PUSHDATA4_impl,
	'OP_1NEGATE': OP_1NEGATE_impl,
	'OP_RESERVED': OP_RESERVED_impl,
	'OP_1': OP_1_impl,
	'OP_TRUE': OP_TRUE_impl,
	'OP_2': OP_2_impl,
	'OP_3': OP_3_impl,
	'OP_4': OP_4_impl,
	'OP_5': OP_5_impl,
	'OP_6': OP_6_impl,
	'OP_7': OP_7_impl,
	'OP_8': OP_8_impl,
	'OP_9': OP_9_impl,
	'OP_10': OP_10_impl,
	'OP_11': OP_11_impl,
	'OP_12': OP_12_impl,
	'OP_13': OP_13_impl,
	'OP_14': OP_14_impl,
	'OP_15': OP_15_impl,
	'OP_16': OP_16_impl,
	'OP_NOP': OP_NOP_impl,
	'OP_VER': OP_VER_impl,
	'OP_IF': OP_IF_impl,
	'OP_NOTIF': OP_NOTIF_impl,
	'OP_ELSE': OP_ELSE_impl,
	'OP_ENDIF': OP_ENDIF_impl,
	'OP_VERIFY': OP_VERIFY_impl,
	'OP_RETURN': OP_RETURN_impl,
	'OP_TOALTSTACK': OP_TOALTSTACK_impl,
	'OP_FROMALTSTACK': OP_FROMALTSTACK_impl,
	'OP_2DROP': OP_2DROP_impl,
	'OP_2DUP': OP_2DUP_impl,
	'OP_3DUP': OP_3DUP_impl,
	'OP_2OVER': OP_2OVER_impl,
	'OP_2ROT': OP_2ROT_impl,
	'OP_2SWAP': OP_2SWAP_impl,
	'OP_IFDUP': OP_IFDUP_impl,
	'OP_DEPTH': OP_DEPTH_impl,
	'OP_DROP': OP_DROP_impl,
	'OP_DUP': OP_DUP_impl,
	'OP_NIP': OP_NIP_impl,
	'OP_OVER': OP_OVER_impl,
	'OP_PICK': OP_PICK_impl,
	'OP_ROLL': OP_ROLL_impl,
	'OP_ROT': OP_ROT_impl,
	'OP_SWAP': OP_SWAP_impl,
	'OP_TUCK': OP_TUCK_impl,
	'OP_CAT': OP_CAT_impl,
	'OP_SUBSTR': OP_SUBSTR_impl,
	'OP_LEFT': OP_LEFT_impl,
	'OP_RIGHT': OP_RIGHT_impl,
	'OP_SIZE': OP_SIZE_impl,
	'OP_INVERT': OP_INVERT_impl,
	'OP_AND': OP_AND_impl,
	'OP_OR': OP_OR_impl,
	'OP_XOR': OP_XOR_impl,
	'OP_EQUAL': OP_EQUAL_impl,
	'OP_EQUALVERIFY': OP_EQUALVERIFY_impl,
	'OP_RESERVED1': OP_RESERVED1_impl,
	'OP_RESERVED2': OP_RESERVED2_impl,
	'OP_1ADD': OP_1ADD_impl,
	'OP_1SUB': OP_1SUB_impl,
	'OP_2MUL': OP_2MUL_impl,
	'OP_2DIV': OP_2DIV_impl,
	'OP_NEGATE': OP_NEGATE_impl,
	'OP_ABS': OP_ABS_impl,
	'OP_NOT': OP_NOT_impl,
	'OP_0NOTEQUAL': OP_0NOTEQUAL_impl,
	'OP_ADD': OP_ADD_impl,
	'OP_SUB': OP_SUB_impl,
	'OP_MUL': OP_MUL_impl,
	'OP_DIV': OP_DIV_impl,
	'OP_MOD': OP_MOD_impl,
	'OP_LSHIFT': OP_LSHIFT_impl,
	'OP_RSHIFT': OP_RSHIFT_impl,
	'OP_BOOLAND': OP_BOOLAND_impl,
	'OP_BOOLOR': OP_BOOLOR_impl,
	'OP_NUMEQUAL': OP_NUMEQUAL_impl,
	'OP_NUMEQUALVERIFY': OP_NUMEQUALVERIFY_impl,
	'OP_NUMNOTEQUAL': OP_NUMNOTEQUAL_impl,
	'OP_LESSTHAN': OP_LESSTHAN_impl,
	'OP_GREATERTHAN': OP_GREATERTHAN_impl,
	'OP_LESSTHANOREQUAL': OP_LESSTHANOREQUAL_impl,
	'OP_GREATERTHANOREQUAL': OP_GREATERTHANOREQUAL_impl,
	'OP_MIN': OP_MIN_impl,
	'OP_MAX': OP_MAX_impl,
	'OP_WITHIN': OP_WITHIN_impl,
	'OP_RIPEMD160': OP_RIPEMD160_impl,
	'OP_SHA1': OP_SHA1_impl,
	'OP_SHA256': OP_SHA256_impl,
	'OP_HASH160': OP_HASH160_impl,
	'OP_HASH256': OP_HASH256_impl,
	'OP_CODESEPARATOR': OP_CODESEPARATOR_impl,
	'OP_CHECKSIG': OP_CHECKSIG_impl,
	'OP_CHECKSIGVERIFY': OP_CHECKSIGVERIFY_impl,
	'OP_CHECKMULTISIG': OP_CHECKMULTISIG_impl,
	'OP_CHECKMULTISIGVERIFY': OP_CHECKMULTISIGVERIFY_impl,
	'OP_NOP1': OP_NOP1_impl,
	'OP_CHECKLOCKTIMEVERIFY': OP_CHECKLOCKTIMEVERIFY_impl,
	'OP_NOP2': OP_NOP2_impl,
	'OP_CHECKSEQUENCEVERIFY': OP_CHECKSEQUENCEVERIFY_impl,
	'OP_NOP3': OP_NOP3_impl,
	'OP_NOP4': OP_NOP4_impl,
	'OP_NOP5': OP_NOP5_impl,
	'OP_NOP6': OP_NOP6_impl,
	'OP_NOP7': OP_NOP7_impl,
	'OP_NOP8': OP_NOP8_impl,
	'OP_NOP9': OP_NOP9_impl,
	'OP_NOP10': OP_NOP10_impl,
	'OP_CHECKSIGADD': OP_CHECKSIGADD_impl,
	'OP_INVALIDOPCODE': OP_INVALIDOPCODE_impl,
}
