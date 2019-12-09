

ops = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
}

intcode_list = open('input.txt').read().split(',')

def execute_op(opcode_index, input_address_1, input_address_2, output_memory):
    opcode = intcode_list[opcode_index]
    if opcode == 99:
        raise EOFError
    input_1, input_2 = intcode_list[intcode_list[input_address_1]], intcode_list[intcode_list[input_address_2]]
    intcode_list[intcode_list[output_memory]] = ops[opcode](input_1, input_2)

if __name__ == "__main__":
    for noun in range(100):
        for verb in range(100):
            print('Noun', noun, 'Verb', verb)
            intcode_list = list(map(int, open('input.txt').read().split(',')))
            intcode_list[1] = noun
            intcode_list[2] = verb
            for i in range(0, len(intcode_list) - 4, 4):
                try:
                    execute_op(i, i + 1, i + 2, i + 3)
                except EOFError:
                    break
            print(intcode_list[0])
            if intcode_list[0] == 19690720:
                print('Found answer')
                print('Noun', noun, 'Verb', verb)
                print(100 *noun + verb)
                exit()