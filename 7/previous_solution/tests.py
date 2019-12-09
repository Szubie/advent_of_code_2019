

#intcode_list = list(map(int, open('input.txt').read().split(',')))
intcode_list = list(map(int, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(",")))

opcode_n_params = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0
}

storage_ops = [1, 2, 3, 7, 8]

def parse_opcode(opcode):
    ''' Takes full opcode and returns op and param_immediate_mode_mask '''
    if len(str(opcode)) == 1:
        if int(opcode) in storage_ops:
            return opcode, [0 for i in range(opcode_n_params[opcode] -1 )] + [1]
        return opcode, [0 for i in range(opcode_n_params[opcode])]
    op_segment = int(str(opcode)[-2:])
    immediate_mode_mask = [0 for i in range(opcode_n_params[op_segment] - len(str(opcode)[:-2]))]
    for digit in str(opcode)[:-2]:
        immediate_mode_mask.append(int(digit))
    immediate_mode_mask = list(reversed(immediate_mode_mask)) # Param mask is read right to left
    if op_segment in storage_ops:
        immediate_mode_mask[-1] = 1  # Storage location in memory must be value
    return op_segment, immediate_mode_mask

def resolve_concrete_values(parameter_list, immediate_mode_mask):
    return [intcode_list[val] if mode == 0 else val for val, mode in zip(parameter_list, immediate_mode_mask)]

def ADD(parameter_list):
    input_1, input_2, storage_location = parameter_list
    intcode_list[storage_location] = input_1 + input_2

def MUL(parameter_list):
    input_1, input_2, storage_location = parameter_list
    intcode_list[storage_location] = input_1 * input_2

def INPUT(parameter_list):
    storage_location = parameter_list[0]
    program_input = int(input('Enter an integer input to the intcode program: '))
    intcode_list[storage_location] = program_input

def OUTPUT(parameter_list):
    storage_location = parameter_list[0]
    print(storage_location)

def HALT(parameter_list):
    exit()

def LESS_THAN(parameter_list):
    input_1, input_2, storage_location = parameter_list
    if input_1 < input_2:
        intcode_list[storage_location] = 1
    else:
        intcode_list[storage_location] = 0

def EQUALS(parameter_list):
    input_1, input_2, storage_location = parameter_list
    if input_1 == input_2:
        intcode_list[storage_location] = 1
    else:
        intcode_list[storage_location] = 0

def JUMP_IF_TRUE(parameter_list):
    is_true, jump_location = parameter_list
    if is_true != 0:
        return jump_location
    return None

def JUMP_IF_FALSE(parameter_list):
    is_true, jump_location = parameter_list
    if is_true == 0:
        return jump_location
    return None

ops_dict = {
    1: ADD,
    2: MUL,
    3: INPUT,
    4: OUTPUT,
    5: JUMP_IF_TRUE,
    6: JUMP_IF_FALSE,
    7: LESS_THAN,
    8: EQUALS,
    99: HALT
}

jump_opcodes = set([5, 6])

i = 0
while i < len(intcode_list):
    op, immediate_mode_mask = parse_opcode(intcode_list[i])
    op_params = intcode_list[i+1:i+1+opcode_n_params[op]]
    concrete_params = resolve_concrete_values(op_params, immediate_mode_mask)

    if op in jump_opcodes:
        if ops_dict[op](concrete_params) is not None:
            i = ops_dict[op](concrete_params)
        else:
            i = i + opcode_n_params[op] + 1
    else:
        ops_dict[op](concrete_params)
        i = i + opcode_n_params[op] + 1

