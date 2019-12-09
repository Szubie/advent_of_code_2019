from process import calculate_component_fuel, calculate_total_component_fuel

def test_calculate_component_fuel():
    test_values = [12, 14, 1969, 100756]
    test_answers = [2, 2, 654, 33583]

    for value, answer in zip(test_values, test_answers):
        assert calculate_component_fuel(value) == answer

def test_calculate_total_component_fuel():
    test_values = [14, 1969, 100756]
    test_answers = [2, 966, 50346]

    for value, answer in zip(test_values, test_answers):
        assert calculate_total_component_fuel(value) == answer
