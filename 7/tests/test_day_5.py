from intcode_computer import IntcodeComputer

def test_1():
    intcode_list = list(map(int, open('../5/input.txt').read().split(',')))
    computer = IntcodeComputer(intcode_list)
    for value in computer.execute(1):
        assert value == 0 or value == 4511442
    assert value == 4511442

def test_equals_position_mode():
    intcode_list = [3,9,8,9,10,9,4,9,99,-1,8]
    inputs = [0, 8, 10]
    expected_outputs = [0, 1, 0]
    for input_value, expected_output in zip(inputs, expected_outputs):
        computer = IntcodeComputer(intcode_list)
        for value in computer.execute(input_value):
            pass
        assert value == expected_output

def test_equals_immediate_mode():
    intcode_list = [3,3,1108,-1,8,3,4,3,99]
    inputs = [0, 8, 10]
    expected_outputs = [0, 1, 0]
    for input_value, expected_output in zip(inputs, expected_outputs):
        computer = IntcodeComputer(intcode_list)
        for value in computer.execute(input_value):
            pass
        assert value == expected_output

def test_less_than_position_mode():
    intcode_list = [3,9,7,9,10,9,4,9,99,-1,8]
    inputs = [0, 8, 10]
    expected_outputs = [1, 0, 0]
    for input_value, expected_output in zip(inputs, expected_outputs):
        computer = IntcodeComputer(intcode_list)
        for value in computer.execute(input_value):
            pass
        assert value == expected_output

def test_less_than_immediate_mode():
    intcode_list = [3,3,1107,-1,8,3,4,3,99]
    inputs = [0, 8, 10]
    expected_outputs = [1, 0, 0]
    for input_value, expected_output in zip(inputs, expected_outputs):
        computer = IntcodeComputer(intcode_list)
        for value in computer.execute(input_value):
            pass
        assert value == expected_output

def test_jump_position():
    intcode_list = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    inputs = [0, 8, 10, -5]
    expected_outputs = [0, 1, 1, 1]
    for input_value, expected_output in zip(inputs, expected_outputs):
        computer = IntcodeComputer(intcode_list)
        for value in computer.execute(input_value):
            pass
        assert value == expected_output


def test_jump_immediate():
    intcode_list = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    inputs = [0, 8, 10, -5]
    expected_outputs = [0, 1, 1, 1]
    for input_value, expected_output in zip(inputs, expected_outputs):
        computer = IntcodeComputer(intcode_list)
        for value in computer.execute(input_value):
            pass
        assert value == expected_output


def test_large():
    intcode_list =  [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    inputs = [0, 8, 10, -5]
    expected_outputs = [999, 1000, 1001, 999]
    for input_value, expected_output in zip(inputs, expected_outputs):
        computer = IntcodeComputer(intcode_list)
        for value in computer.execute(input_value):
            pass
        assert value == expected_output

