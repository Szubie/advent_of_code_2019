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
intcode_list = list(map(int, "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(',')))

best_value = 0
best_phase_setting = None
phase_setting = (9, 8, 7, 6, 5)
for phase_setting in permutations(range(5, 10)):
    computers = [IntcodeComputer(intcode_list) for i in range(5)]
    current_value = 0
    for phase, computer in zip(phase_setting, computers):
        current_value = next(computer.execute(phase, current_value))
        print(current_value)
        while len(computer.output_channel) > 1:
            current_value = next(computer.execute(current_value))
            print(current_value)
    while True:
        try:
            for computer in computers:
                current_value = next(computer.execute(current_value))
                print(current_value)
                while len(computer.output_channel) > 1:
                    current_value = next(computer.execute(current_value))
                    print(current_value)
            if current_value > best_value:
                best_value = current_value
                best_phase_setting = phase_setting
        except:
            break

print('Best possible value:', best_value)
print('Best phase setting:', best_phase_setting)


"""
computer = computers[0]
results = computer.execute(intcode_list, 3, 0)
for res in results:
    print(res)

computer_2 = computers[1]
results = computer_2.execute(intcode_list)
for res in results:
    print(res)

computer_3 = computers[2]
results = computer_3.execute(intcode_list)
for res in results:
    print(res)

computer_4 = computers[3]
results = computer_4.execute(intcode_list)
for res in results:
    print(res)

computer_5 = computers[4]
results = computer_5.execute(intcode_list)
for res in results:
    print(res)


#print(list(permutations(range(5))))"""