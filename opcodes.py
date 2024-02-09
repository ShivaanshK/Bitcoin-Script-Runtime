global_stack = None

def set_global_stack(stack):
    global global_stack
    global_stack = stack

def OP_0_impl() -> None:
	global_stack.push(b"")


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


def OP_IF_impl() -> None:
	
	return


def OP_NOTIF_impl() -> None:
	
	return


def OP_VERIF_impl() -> None:
	
	return


def OP_VERNOTIF_impl() -> None:
	
	return


def OP_ELSE_impl() -> None:
	
	return


def OP_ENDIF_impl() -> None:
	
	return


def OP_VERIFY_impl() -> None:
	top_item: str = global_stack.pop()
	if top_item:
		return
	else:
		raise "INVALID TRANSACTION"


def OP_RETURN_impl() -> None:
	
	return


def OP_TOALTSTACK_impl() -> None:
	
	return


def OP_FROMALTSTACK_impl() -> None:
	
	return


def OP_2DROP_impl() -> None:
	
	return


def OP_2DUP_impl() -> None:
	
	return


def OP_3DUP_impl() -> None:
	
	return


def OP_2OVER_impl() -> None:
	
	return


def OP_2ROT_impl() -> None:
	
	return


def OP_2SWAP_impl() -> None:
	
	return


def OP_IFDUP_impl() -> None:
	
	return


def OP_DEPTH_impl() -> None:
	
	return


def OP_DROP_impl() -> None:
	
	return


def OP_DUP_impl() -> None:
	top_item: str = global_stack.pop()
	global_stack.push(top_item)
	global_stack.push(top_item)


def OP_NIP_impl() -> None:
	
	return


def OP_OVER_impl() -> None:
	
	return


def OP_PICK_impl() -> None:
	
	return


def OP_ROLL_impl() -> None:
	
	return


def OP_ROT_impl() -> None:
	
	return


def OP_SWAP_impl() -> None:
	
	return


def OP_TUCK_impl() -> None:
	
	return


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


def OP_1ADD_impl() -> None:
	
	return


def OP_1SUB_impl() -> None:
	
	return


def OP_2MUL_impl() -> None:
	
	return


def OP_2DIV_impl() -> None:
	
	return


def OP_NEGATE_impl() -> None:
	
	return


def OP_ABS_impl() -> None:
	
	return


def OP_NOT_impl() -> None:
	
	return


def OP_0NOTEQUAL_impl() -> None:
	
	return


def OP_ADD_impl() -> None:
	
	return


def OP_SUB_impl() -> None:
	
	return


def OP_MUL_impl() -> None:
	
	return


def OP_DIV_impl() -> None:
	
	return


def OP_MOD_impl() -> None:
	
	return


def OP_LSHIFT_impl() -> None:
	
	return


def OP_RSHIFT_impl() -> None:
	
	return


def OP_BOOLAND_impl() -> None:
	
	return


def OP_BOOLOR_impl() -> None:
	
	return


def OP_NUMEQUAL_impl() -> None:
	
	return


def OP_NUMEQUALVERIFY_impl() -> None:
	
	return


def OP_NUMNOTEQUAL_impl() -> None:
	
	return


def OP_LESSTHAN_impl() -> None:
	
	return


def OP_GREATERTHAN_impl() -> None:
	
	return


def OP_LESSTHANOREQUAL_impl() -> None:
	
	return


def OP_GREATERTHANOREQUAL_impl() -> None:
	
	return


def OP_MIN_impl() -> None:
	
	return


def OP_MAX_impl() -> None:
	
	return


def OP_WITHIN_impl() -> None:
	
	return


def OP_RIPEMD160_impl() -> None:
	
	return


def OP_SHA1_impl() -> None:
	
	return


def OP_SHA256_impl() -> None:
	
	return


def OP_HASH160_impl() -> None:
	
	return


def OP_HASH256_impl() -> None:
	
	return


def OP_CODESEPARATOR_impl() -> None:
	
	return


def OP_CHECKSIG_impl() -> None:
	
	return


def OP_CHECKSIGVERIFY_impl() -> None:
	
	return


def OP_CHECKMULTISIG_impl() -> None:
	
	return


def OP_CHECKMULTISIGVERIFY_impl() -> None:
	
	return


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
	
	return


def OP_INVALIDOPCODE_impl() -> None:
	
	return

def is_opcode(opcode: str) -> bool:
	return opcode in OPCODES.keys()

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
	'OP_VERIF': OP_VERIF_impl,
	'OP_VERNOTIF': OP_VERNOTIF_impl,
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