from intcode_computer import IntcodeComputer
from itertools import permutations

intcode_list = list(map(int, open('input.txt').read().split(',')))
#intcode_list = list(map(int, open('previous_solution/input.txt').read().split(',')))
#intcode_list = list(map(int, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(",")))

# 3, 1, 2, 4, 0
# 22, 46, 312, 4692, 112660

print('Part 1')

best_value = 0
best_phase_setting = None
for phase_setting in permutations(range(5)):
    computers = [IntcodeComputer(intcode_list) for i in range(5)]
    current_value = 0
    for phase, computer in zip(phase_setting, computers):
        current_value = next(computer.execute(phase, current_value))
    if current_value > best_value:
        best_value = current_value
        best_phase_setting = phase_setting

print('Best possible value:', best_value)
print('Best phase setting:', best_phase_setting)


print('Part 2')
intcode_list = list(map(int, open('input.txt').read().split(',')))

best_value = 0
best_phase_setting = None
for phase_setting in permutations(range(5, 10)):
    computers = [IntcodeComputer(intcode_list) for i in range(5)]

    for phase, computer in zip(phase_setting, computers):
        computer.input_list.append(phase)

    current_value = 0
    while computers[-1].halt_flag != True:
        for i, computer in enumerate(computers):
            try:
                for output_value in computer.execute(current_value):
                    #print(output_value)
                    current_value = output_value
            except IndexError:
                pass
            #print('Computer {} output: {}'.format(i, current_value))
    print('Permutation', phase_setting)
    final_output = current_value
    print('Final output', final_output)
    if final_output > best_value:
        best_value = final_output
        best_phase_setting = phase_setting

print('Best possible value:', best_value)
print('Best phase setting:', best_phase_setting)

