
number_range = range(130254, 678275)

num_string = "133333"

def contains_double(num_string):
    for i in range(len(num_string) - 1):
        num_1, num_2 = num_string[i:i+2]
        if num_1 == num_2:
            return True
    return False

def non_decreasing_digits(num_string):
    for i in range(len(num_string) - 1):
        num_1, num_2 = map(int, num_string[i:i+2])
        if num_2 < num_1:
            return False
    return True

n_found = 0
for i in number_range:
    if contains_double(str(i)) and non_decreasing_digits(str(i)):
        n_found += 1



def contains_exact_double(num_string):
    padded_num_string = "9" + num_string + "0"
    for i in range(len(padded_num_string) - 3):
        num_1, num_2, num_3, num_4 = padded_num_string[i:i+4]
        if num_2 == num_3:
            if num_1 != num_2 and num_4 != num_2:
                return True
    return False


n_found = 0
for i in number_range:
    if contains_exact_double(str(i)) and non_decreasing_digits(str(i)):
        n_found += 1



def generate_cadidate_digit(previous_digit):
    for i in range(previous_digit, 10):
        yield i
