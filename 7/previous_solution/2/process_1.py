

ops = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x * y,
    '99': lambda x, y: exit()
}

intcode_list = open('input.txt').read().split(',')

def execute_op(opcode_index, input_address_1, input_address_2, output_memory):
    opcode = intcode_list[opcode_index]
    input_1, input_2 = int(intcode_list[int(intcode_list[input_address_1])]), int(intcode_list[int(intcode_list[input_address_2])])
    intcode_list[int(intcode_list[output_memory])] = ops[opcode](input_1, input_2)

if __name__ == "__main__":
    intcode_list[1] = 86
    intcode_list[2] = 9
    print(intcode_list)
    for i in range(0, len(intcode_list) - 4, 4):
        execute_op(i, i + 1, i + 2, i + 3)
        print(intcode_list)