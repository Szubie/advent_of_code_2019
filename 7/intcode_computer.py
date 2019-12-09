class IntcodeComputer:
    def __init__(self, intcode_list):
        self.i = 0
        self.intcode_list = intcode_list
        self.opcode_n_params = {
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
        self.storage_ops = [1, 2, 3, 7, 8]
        self.ops_dict = {
            1: self.ADD,
            2: self.MUL,
            3: self.INPUT,
            4: self.OUTPUT,
            5: self.JUMP_IF_TRUE,
            6: self.JUMP_IF_FALSE,
            7: self.LESS_THAN,
            8: self.EQUALS,
            99: self.HALT
        }
        self.jump_opcodes = set([5, 6])
        self.output_channel = []

    def parse_opcode(self, opcode):
        ''' Takes full opcode and returns op and param_immediate_mode_mask '''
        if len(str(opcode)) == 1:
            if int(opcode) in self.storage_ops:
                return opcode, [0 for i in range(self.opcode_n_params[opcode] -1 )] + [1]
            return opcode, [0 for i in range(self.opcode_n_params[opcode])]
        op_segment = int(str(opcode)[-2:])
        immediate_mode_mask = [0 for i in range(self.opcode_n_params[op_segment] - len(str(opcode)[:-2]))]
        for digit in str(opcode)[:-2]:
            immediate_mode_mask.append(int(digit))
        immediate_mode_mask = list(reversed(immediate_mode_mask)) # Param mask is read right to left
        if op_segment in self.storage_ops:
            immediate_mode_mask[-1] = 1  # Storage location in memory must be value
        return op_segment, immediate_mode_mask

    def resolve_concrete_values(self, parameter_list, immediate_mode_mask):
        return [self.intcode_list[val] if mode == 0 else val for val, mode in zip(parameter_list, immediate_mode_mask)]

    def ADD(self, parameter_list):
        input_1, input_2, storage_location = parameter_list
        self.intcode_list[storage_location] = input_1 + input_2

    def MUL(self, parameter_list):
        input_1, input_2, storage_location = parameter_list
        self.intcode_list[storage_location] = input_1 * input_2

    def INPUT(self, parameter_list):
        storage_location = parameter_list[0]
        #program_input = int(input('Enter an integer input to the intcode program: '))
        program_input = self.input_list.pop(0)
        self.intcode_list[storage_location] = program_input

    def OUTPUT(self, parameter_list):
        output_value = parameter_list[0]
        self.output_channel.append(output_value)

    def HALT(self, parameter_list):
        self.intcode_list = []

    def LESS_THAN(self, parameter_list):
        input_1, input_2, storage_location = parameter_list
        if input_1 < input_2:
            self.intcode_list[storage_location] = 1
        else:
            self.intcode_list[storage_location] = 0

    def EQUALS(self, parameter_list):
        input_1, input_2, storage_location = parameter_list
        if input_1 == input_2:
            self.intcode_list[storage_location] = 1
        else:
            self.intcode_list[storage_location] = 0

    def JUMP_IF_TRUE(self, parameter_list):
        is_true, jump_location = parameter_list
        if is_true != 0:
            return jump_location
        return None

    def JUMP_IF_FALSE(self, parameter_list):
        is_true, jump_location = parameter_list
        if is_true == 0:
            return jump_location
        return None

    def execute(self, *inputs):
        self.input_list = list(inputs)

        while self.i < len(self.intcode_list):
            op, immediate_mode_mask = self.parse_opcode(self.intcode_list[self.i])
            op_params = self.intcode_list[self.i+1:self.i+1+self.opcode_n_params[op]]
            concrete_params = self.resolve_concrete_values(op_params, immediate_mode_mask)

            if op in self.jump_opcodes:
                if self.ops_dict[op](concrete_params) is not None:
                    self.i = self.ops_dict[op](concrete_params)
                else:
                    self.i = self.i + self.opcode_n_params[op] + 1
            else:
                self.ops_dict[op](concrete_params)
                self.i = self.i + self.opcode_n_params[op] + 1

            while len(self.output_channel) > 0:
                output = self.output_channel.pop()
                yield output
