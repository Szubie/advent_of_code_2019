

line_1, line_2 = open('input.txt').readlines()
line_1, line_2 = line_1.split(','), line_2.split(',')


def get_next_coordinates(start_coords, instruction):
    new_coords = start_coords[:]
    if instruction[0] == 'L':
        new_coords[0] -= int(instruction[1:])
    elif instruction[0] == 'R':
        new_coords[0] += int(instruction[1:])
    elif instruction[0] == 'U':
        new_coords[1] += int(instruction[1:])
    elif instruction[0] == 'D':
        new_coords[1] -= int(instruction[1:])
    else:
        raise ValueError('Unrecognised instruction:', instruction[0])
    return new_coords

def get_line_coordinates_from_points(start_coords, end_coords):
    intermediate_coords = []
    coord_diff = [ end_value - start_value for start_value, end_value in zip(start_coords, end_coords)]
    changed_index = 1 if coord_diff[0] == 0 else 0
    increment = int(coord_diff[changed_index] > 0) * 2 - 1
    for i in range(0, coord_diff[changed_index] + increment, increment):
        current_coords = start_coords[:]
        current_coords[changed_index] += i
        intermediate_coords.append(current_coords)
    return intermediate_coords

def get_coordinates_visited_set(line, start_coords=[0, 0]):
    coords_set = set()
    current_coords = start_coords
    for instruction in line:
        next_coords = get_next_coordinates(current_coords, instruction)
        line_coords = get_line_coordinates_from_points(current_coords, next_coords)
        #print(current_coords, next_coords)
        coords_set.update(map(tuple, line_coords))
        current_coords = next_coords
    return coords_set


line_1_coords_visited_set = get_coordinates_visited_set(line_1)
line_2_coords_visited_set = get_coordinates_visited_set(line_2)

intersection_points = line_1_coords_visited_set.intersection(line_2_coords_visited_set)
intersection_points.remove((0, 0 ))

distances_from_centre = { coords : abs(coords[0] - 0) + abs(coords[1] - 0) for coords in intersection_points}
nearest_intersect_coords = min(distances_from_centre, key=distances_from_centre.get)
minimum_distance = min(distances_from_centre.values())


# Benefit of getting sequential results
def get_coordinates_visited(line, start_coords=[0, 0]):
    coords_list = []
    current_coords = start_coords
    for instruction in line:
        next_coords = get_next_coordinates(current_coords, instruction)
        line_coords = get_line_coordinates_from_points(current_coords, next_coords)
        #print(current_coords, next_coords)
        coords_list.append(line_coords)
        current_coords = next_coords
    return coords_list

line_1_coords_visited_list = get_coordinates_visited(line_1)
line_1_coords_visited_flat_list = [item for sublist in line_1_coords_visited_list for item in sublist[1:]]
line_2_coords_visited_list = get_coordinates_visited(line_2)
line_2_coords_visited_flat_list = [item for sublist in line_2_coords_visited_list for item in sublist[1:]]

line_1_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(line_1_coords_visited_flat_list):
    if tuple(coord) in line_1_intersection_costs:
        line_1_intersection_costs[tuple(coord)] = i + 1

"""
backward_line_1_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(reversed(line_1_coords_visited_flat_list + [[0, 0]])):
    if tuple(coord) in backward_line_1_intersection_costs:
        backward_line_1_intersection_costs[tuple(coord)] = i

line_1_intersection_costs = {key: min(value, backward_line_1_intersection_costs[key]) for key, value in forward_line_1_intersection_costs.items()}
"""


line_2_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(line_2_coords_visited_flat_list):
    if tuple(coord) in line_2_intersection_costs:
        line_2_intersection_costs[tuple(coord)] = i + 1

"""
backward_line_2_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(reversed(line_2_coords_visited_flat_list + [[0, 0]])):
    if tuple(coord) in backward_line_2_intersection_costs:
        backward_line_2_intersection_costs[tuple(coord)] = i

line_2_intersection_costs = {key: min(value, backward_line_2_intersection_costs[key]) for key, value in forward_line_2_intersection_costs.items()}
"""

final_intersection_costs = {key: value + line_2_intersection_costs[key] for key, value in line_1_intersection_costs.items()}
min_key = min(final_intersection_costs, key=final_intersection_costs.get)
min_value = min(final_intersection_costs.values())

#
#min_index, min_value = min(enumerate(distances_from_centre), key=operator.itemgetter(1))

###

test_line_1 = "R8,U5,L5,D3".split(',')
test_line_2 = "U7,R6,D4,L4".split(',')

test_line_1_coords_visited_set = get_coordinates_visited_set(test_line_1)
test_line_2_coords_visited_set = get_coordinates_visited_set(test_line_2)

intersection_points = test_line_1_coords_visited_set.intersection(test_line_2_coords_visited_set)
intersection_points.remove((0, 0 ))

distances_from_centre = { coords : abs(coords[0] - 0) + abs(coords[1] - 0) for coords in intersection_points}
nearest_intersect_coords = min(distances_from_centre, key=distances_from_centre.get)
minimum_distance = min(distances_from_centre.values())


test_line_1_coords_visited_list = get_coordinates_visited(test_line_1)
test_line_1_coords_visited_flat_list = [item for sublist in test_line_1_coords_visited_list for item in sublist[1:]]
test_line_2_coords_visited_list = get_coordinates_visited(test_line_2)
test_line_2_coords_visited_flat_list = [item for sublist in test_line_2_coords_visited_list for item in sublist[1:]]

forward_test_line_1_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(test_line_1_coords_visited_flat_list):
    if tuple(coord) in forward_test_line_1_intersection_costs:
        forward_test_line_1_intersection_costs[tuple(coord)] = i + 1

backward_test_line_1_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(reversed(test_line_1_coords_visited_flat_list + [[0, 0]])):
    if tuple(coord) in backward_test_line_1_intersection_costs:
        backward_test_line_1_intersection_costs[tuple(coord)] = i + 1

test_line_1_intersection_costs = {key: min(value, backward_test_line_1_intersection_costs[key]) for key, value in forward_test_line_1_intersection_costs.items()}


forward_test_line_2_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(test_line_2_coords_visited_flat_list):
    if tuple(coord) in forward_test_line_2_intersection_costs:
        forward_test_line_2_intersection_costs[tuple(coord)] = i + 1

backward_test_line_2_intersection_costs = {coords : 0 for coords in intersection_points}
for i, coord in enumerate(reversed(test_line_2_coords_visited_flat_list + [[0, 0]])):
    if tuple(coord) in backward_test_line_2_intersection_costs:
        backward_test_line_2_intersection_costs[tuple(coord)] = i + 1

test_line_2_intersection_costs = {key: min(value, backward_test_line_2_intersection_costs[key]) for key, value in forward_test_line_2_intersection_costs.items()}

final_intersection_costs = {key: value + test_line_2_intersection_costs[key] for key, value in test_line_1_intersection_costs.items()}
min_key = min(final_intersection_costs, key=final_intersection_costs.get)
min_value = min(final_intersection_costs.values())
