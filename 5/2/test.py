

ops = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x * y,
    '99': lambda x, y: exit()
}

intcode_list = '1,9,10,3,2,3,11,0,99,30,40,50'.split(',')

def execute_op(opcode_index, input_address_1, input_address_2, output_memory):
    opcode = intcode_list[opcode_index]
    input_1, input_2 = int(intcode_list[int(intcode_list[input_address_1])]), int(intcode_list[int(intcode_list[input_address_2])])
    intcode_list[int(intcode_list[output_memory])] = str(ops[opcode](input_1, input_2))

if __name__ == "__main__":
    for i in range(0, len(intcode_list) - 4, 4):
        execute_op(i, i + 1, i + 2, i + 3)
        print(intcode_list)

    