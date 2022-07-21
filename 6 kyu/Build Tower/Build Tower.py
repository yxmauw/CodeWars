def tower_builder(n_floors):
    floors = []
    for i in range(1, n_floors*2, 2):
        floor = (' '*(n_floors-1)) + ('*'*i) + (' '*(n_floors-1))
        n_floors -= 1
        floors.append(floor)
    return floors
