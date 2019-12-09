
map_data = list(map(lambda x: x.rstrip(), open('input.txt').readlines()))
#map_data = list(map(lambda x: x.rstrip(), open('test_input_2.txt').readlines()))

class Node:
    def __init__(self, name, orbits=None, orbited_by=None):
        self.name = name
        if orbits is not None:
            self.orbits = orbits
        else:
            self.orbits = None
        if orbited_by is not None:
            self.orbited_by = orbited_by
        else:
            self.orbited_by = []

objects_str_in_space = {}

for entry in map_data:
    orbited, orbiter = entry.split(')')
    if orbited not in objects_str_in_space:
        objects_str_in_space[orbited] = Node(orbited, orbited_by=[orbiter])
    else:
        print('appending', orbiter, 'to oribted list for', orbited)
        objects_str_in_space[orbited].orbited_by.append(orbiter)
    if orbiter not in objects_str_in_space:
        objects_str_in_space[orbiter] = Node(orbiter, orbits=orbited)
    else:
        objects_str_in_space[orbiter].orbits = orbited


def count_n_orbits_to_root(node_str, n=0):
    if objects_str_in_space[node_str].orbits is None:
        return n
    return count_n_orbits_to_root(objects_str_in_space[node_str].orbits, n+1)

#count_n_orbits_to_root('L')
sum(map(lambda x: count_n_orbits_to_root(x), objects_str_in_space.keys()))


def breadth_first_search(start_node_str):
    san_found = False
    visited_node_strs = set()
    queue = [start_node_str, None]
    #queue = [start_node_str]
    count = -1
    while len(queue) > 0:
        #print(queue)
        node_str = queue.pop(0)
        if node_str is None:
            count += 1
            queue.append(None)
            continue
        if node_str not in visited_node_strs:
            visited_node_strs.update([node_str])
            node = objects_str_in_space[node_str]
            if 'SAN' in node.orbited_by:
                san_found = True
                break
            if node.orbits is not None:
                queue.append(node.orbits)
            for orbiter in node.orbited_by:
                if orbiter not in visited_node_strs:
                    queue.append(orbiter)
    if san_found:
        print('Found SAN!')
        return count
    else:
        return None

num_orbital_transfers = breadth_first_search('YOU')
print('Number of orbital transfers required:', num_orbital_transfers)
