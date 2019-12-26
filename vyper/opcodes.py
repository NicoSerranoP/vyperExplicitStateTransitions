from typing import (
    Dict,
    List,
    Optional,
)

active_evm_version = 0

EVM_VERSIONS = {
    'byzantium': 0,
    'constantinople': 1,
    'petersburg': 1,
    'istanbul': 2,
}
DEFAULT_EVM_VERSION = "byzantium"


# opcode as hex value, number of values removed from stack, added to stack, gas cost
OPCODES: Dict[str, List[Optional[int]]] = {
    'STOP': [0x00, 0, 0, 0],
    'ADD': [0x01, 2, 1, 3],
    'MUL': [0x02, 2, 1, 5],
    'SUB': [0x03, 2, 1, 3],
    'DIV': [0x04, 2, 1, 5],
    'SDIV': [0x05, 2, 1, 5],
    'MOD': [0x06, 2, 1, 5],
    'SMOD': [0x07, 2, 1, 5],
    'ADDMOD': [0x08, 3, 1, 8],
    'MULMOD': [0x09, 3, 1, 8],
    'EXP': [0x0a, 2, 1, 10],
    'SIGNEXTEND': [0x0b, 2, 1, 5],
    'LT': [0x10, 2, 1, 3],
    'GT': [0x11, 2, 1, 3],
    'SLT': [0x12, 2, 1, 3],
    'SGT': [0x13, 2, 1, 3],
    'EQ': [0x14, 2, 1, 3],
    'ISZERO': [0x15, 1, 1, 3],
    'AND': [0x16, 2, 1, 3],
    'OR': [0x17, 2, 1, 3],
    'XOR': [0x18, 2, 1, 3],
    'NOT': [0x19, 1, 1, 3],
    'BYTE': [0x1a, 2, 1, 3],
    'SHL': [0x1b, 2, 1, (None, 3)],
    'SHR': [0x1c, 2, 1, (None, 3)],
    'SAR': [0x1d, 2, 1, (None, 3)],
    'SHA3': [0x20, 2, 1, 30],
    'ADDRESS': [0x30, 0, 1, 2],
    'BALANCE': [0x31, 1, 1, (400, 400, 700)],
    'ORIGIN': [0x32, 0, 1, 2],
    'CALLER': [0x33, 0, 1, 2],
    'CALLVALUE': [0x34, 0, 1, 2],
    'CALLDATALOAD': [0x35, 1, 1, 3],
    'CALLDATASIZE': [0x36, 0, 1, 2],
    'CALLDATACOPY': [0x37, 3, 0, 3],
    'CODESIZE': [0x38, 0, 1, 2],
    'CODECOPY': [0x39, 3, 0, 3],
    'GASPRICE': [0x3a, 0, 1, 2],
    'EXTCODESIZE': [0x3b, 1, 1, 700],
    'EXTCODECOPY': [0x3c, 4, 0, 700],
    'RETURNDATASIZE': [0x3d, 0, 1, 2],
    'RETURNDATACOPY': [0x3e, 3, 0, 3],
    'EXTCODEHASH': [0x3f, 1, 1, (None, 400, 700)],
    'BLOCKHASH': [0x40, 1, 1, 20],
    'COINBASE': [0x41, 0, 1, 2],
    'TIMESTAMP': [0x42, 0, 1, 2],
    'NUMBER': [0x43, 0, 1, 2],
    'DIFFICULTY': [0x44, 0, 1, 2],
    'GASLIMIT': [0x45, 0, 1, 2],
    'CHAINID': [0x46, 0, 1, (None, None, 2)],
    'SELFBALANCE': [0x47, 0, 1, (None, None, 5)],
    'POP': [0x50, 1, 0, 2],
    'MLOAD': [0x51, 1, 1, 3],
    'MSTORE': [0x52, 2, 0, 3],
    'MSTORE8': [0x53, 2, 0, 3],
    'SLOAD': [0x54, 1, 1, (200, 200, 800)],
    'SSTORE': [0x55, 2, 0, 20000],
    'JUMP': [0x56, 1, 0, 8],
    'JUMPI': [0x57, 2, 0, 10],
    'PC': [0x58, 0, 1, 2],
    'MSIZE': [0x59, 0, 1, 2],
    'GAS': [0x5a, 0, 1, 2],
    'JUMPDEST': [0x5b, 0, 0, 1],
    'PUSH1': [0x60, 0, 1, 3],
    'PUSH2': [0x61, 0, 1, 3],
    'PUSH3': [0x62, 0, 1, 3],
    'PUSH4': [0x63, 0, 1, 3],
    'PUSH5': [0x64, 0, 1, 3],
    'PUSH6': [0x65, 0, 1, 3],
    'PUSH7': [0x66, 0, 1, 3],
    'PUSH8': [0x67, 0, 1, 3],
    'PUSH9': [0x68, 0, 1, 3],
    'PUSH10': [0x69, 0, 1, 3],
    'PUSH11': [0x6a, 0, 1, 3],
    'PUSH12': [0x6b, 0, 1, 3],
    'PUSH13': [0x6c, 0, 1, 3],
    'PUSH14': [0x6d, 0, 1, 3],
    'PUSH15': [0x6e, 0, 1, 3],
    'PUSH16': [0x6f, 0, 1, 3],
    'PUSH17': [0x70, 0, 1, 3],
    'PUSH18': [0x71, 0, 1, 3],
    'PUSH19': [0x72, 0, 1, 3],
    'PUSH20': [0x73, 0, 1, 3],
    'PUSH21': [0x74, 0, 1, 3],
    'PUSH22': [0x75, 0, 1, 3],
    'PUSH23': [0x76, 0, 1, 3],
    'PUSH24': [0x77, 0, 1, 3],
    'PUSH25': [0x78, 0, 1, 3],
    'PUSH26': [0x79, 0, 1, 3],
    'PUSH27': [0x7a, 0, 1, 3],
    'PUSH28': [0x7b, 0, 1, 3],
    'PUSH29': [0x7c, 0, 1, 3],
    'PUSH30': [0x7d, 0, 1, 3],
    'PUSH31': [0x7e, 0, 1, 3],
    'PUSH32': [0x7f, 0, 1, 3],
    'DUP1': [0x80, 1, 2, 3],
    'DUP2': [0x81, 1, 2, 3],
    'DUP3': [0x82, 1, 2, 3],
    'DUP4': [0x83, 1, 2, 3],
    'DUP5': [0x84, 1, 2, 3],
    'DUP6': [0x85, 1, 2, 3],
    'DUP7': [0x86, 1, 2, 3],
    'DUP8': [0x87, 1, 2, 3],
    'DUP9': [0x88, 1, 2, 3],
    'DUP10': [0x89, 1, 2, 3],
    'DUP11': [0x8a, 1, 2, 3],
    'DUP12': [0x8b, 1, 2, 3],
    'DUP13': [0x8c, 1, 2, 3],
    'DUP14': [0x8d, 1, 2, 3],
    'DUP15': [0x8e, 1, 2, 3],
    'DUP16': [0x8f, 1, 2, 3],
    'SWAP1': [0x90, 2, 2, 3],
    'SWAP2': [0x91, 2, 2, 3],
    'SWAP3': [0x92, 2, 2, 3],
    'SWAP4': [0x93, 2, 2, 3],
    'SWAP5': [0x94, 2, 2, 3],
    'SWAP6': [0x95, 2, 2, 3],
    'SWAP7': [0x96, 2, 2, 3],
    'SWAP8': [0x97, 2, 2, 3],
    'SWAP9': [0x98, 2, 2, 3],
    'SWAP10': [0x99, 2, 2, 3],
    'SWAP11': [0x9a, 2, 2, 3],
    'SWAP12': [0x9b, 2, 2, 3],
    'SWAP13': [0x9c, 2, 2, 3],
    'SWAP14': [0x9d, 2, 2, 3],
    'SWAP15': [0x9e, 2, 2, 3],
    'SWAP16': [0x9f, 2, 2, 3],
    'LOG0': [0xa0, 2, 0, 375],
    'LOG1': [0xa1, 3, 0, 750],
    'LOG2': [0xa2, 4, 0, 1125],
    'LOG3': [0xa3, 5, 0, 1500],
    'LOG4': [0xa4, 6, 0, 1875],
    'CREATE': [0xf0, 3, 1, 32000],
    'CALL': [0xf1, 7, 1, 700],
    'CALLCODE': [0xf2, 7, 1, 700],
    'RETURN': [0xf3, 2, 0, 0],
    'DELEGATECALL': [0xf4, 6, 1, 700],
    'CREATE2': [0xf5, 4, 1, (None, 32000)],
    'SELFDESTRUCT': [0xff, 1, 0, 25000],
    'STATICCALL': [0xfa, 6, 1, 40],
    'REVERT': [0xfd, 2, 0, 0],
    'INVALID': [0xfe, 0, 0, 0],
    'DEBUG': [0xa5, 1, 0, 0]
}

PSEUDO_OPCODES: Dict[str, List[Optional[int]]] = {
    'CLAMP': [None, 3, 1, 70],
    'UCLAMPLT': [None, 2, 1, 25],
    'UCLAMPLE': [None, 2, 1, 30],
    'CLAMP_NONZERO': [None, 1, 1, 19],
    'ASSERT': [None, 1, 0, 85],
    'ASSERT_REASON': [None, 3, 0, 85],
    'ASSERT_UNREACHABLE': [None, 1, 0, 17],
    'PASS': [None, 0, 0, 0],
    'BREAK': [None, 0, 0, 20],
    'CONTINUE': [None, 0, 0, 20],
    'SHA3_32': [None, 1, 1, 72],
    'SHA3_64': [None, 2, 1, 109],
    'SLE': [None, 2, 1, 10],
    'SGE': [None, 2, 1, 10],
    'LE': [None, 2, 1, 10],
    'GE': [None, 2, 1, 10],
    'CEIL32': [None, 1, 1, 20],
    'SET': [None, 2, 0, 20],
    'NE': [None, 2, 1, 6],
    'DEBUGGER': [None, 0, 0, 0],
    'LABEL': [None, 1, 0, 1],
    'GOTO': [None, 1, 0, 8]
}

COMB_OPCODES: Dict[str, List[Optional[int]]] = {**OPCODES, **PSEUDO_OPCODES}


def evm_wrapper(fn, *args, **kwargs):

    def _wrapper(*args, **kwargs):
        global active_evm_version
        evm_version = kwargs.pop('evm_version', DEFAULT_EVM_VERSION)
        active_evm_version = EVM_VERSIONS[evm_version]
        try:
            return fn(*args, **kwargs)
        finally:
            active_evm_version = EVM_VERSIONS[DEFAULT_EVM_VERSION]

    return _wrapper


def _gas(opcode_name):
    if isinstance(COMB_OPCODES[opcode_name][3], int):
        return COMB_OPCODES[opcode_name][3]
    if len(COMB_OPCODES[opcode_name][3]) <= active_evm_version:
        return COMB_OPCODES[opcode_name][3][-1]
    return COMB_OPCODES[opcode_name][3][active_evm_version]


def get_opcodes():
    return dict((k, v[:3]+[_gas(k)]) for k, v in OPCODES.items() if _gas(k) is not None)


def get_comb_opcodes():
    return dict((k, v[:3]+[_gas(k)]) for k, v in COMB_OPCODES.items() if _gas(k) is not None)
