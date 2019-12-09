import pandas as pd

def calculate_component_fuel(component_mass):
    return component_mass // 3 - 2

def calculate_total_component_fuel(component_mass):
    total_fuel_required = calculate_component_fuel(component_mass)
    additional_fuel_required = calculate_component_fuel(total_fuel_required)
    while additional_fuel_required > 0:
        total_fuel_required = total_fuel_required + additional_fuel_required
        additional_fuel_required = calculate_component_fuel(additional_fuel_required)
    return total_fuel_required

def recursive_calculate_total_component_fuel(component_mass, total_fuel_required=0):
    additional_fuel = calculate_component_fuel(component_mass)
    if additional_fuel <= 0:
        return total_fuel_required
    return recursive_calculate_total_component_fuel(additional_fuel, total_fuel_required + additional_fuel)

if __name__ == '__main__':
    print('Pandas solution')
    input_series = pd.read_csv('input.csv', header=None)[0]
    print('Part 1: Fuel required for all components')
    print(input_series.apply(calculate_component_fuel).sum())

    print('Part 2: Fuel required including fuel required for fuel')
    print(input_series.apply(calculate_total_component_fuel).sum())

    print('Part 2: Recursive solution')
    print(input_series.apply(recursive_calculate_total_component_fuel).sum())

    print('Raw Python solution')
    inputs = map(int, open('input.csv').readlines())
    print('Part 1: Fuel required for all components')
    print(sum(map(calculate_component_fuel, inputs)))

    print('Part 2: Fuel required including fuel required for fuel')
    inputs = map(int, open('input.csv').readlines())
    print(sum(map(calculate_total_component_fuel, inputs)))

    print('Part 2: List comprehension')
    inputs = map(int, open('input.csv').readlines())
    print(sum([calculate_total_component_fuel(x) for x in inputs]))