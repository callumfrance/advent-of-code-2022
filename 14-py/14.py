from typing import Final

SAND_ORIGIN: Final = [500, 0]

SAND_MOVES: Final = [(0, 1), (-1, 1), (1, 1)]


def get_boundaries(rock_shapes: list[list[tuple[int, int]]]) -> tuple[int]:
    (min_x, max_x, min_y, max_y) = (SAND_ORIGIN[0], SAND_ORIGIN[0], SAND_ORIGIN[1], SAND_ORIGIN[1])

    for rock_shape in rock_shapes:
        for rock_segment in rock_shape:
            min_x = rock_segment[0] if min_x > rock_segment[0] else min_x
            max_x = rock_segment[0] if max_x < rock_segment[0] else max_x
            min_y = rock_segment[1] if min_y > rock_segment[1] else min_y
            max_y = rock_segment[1] if max_y < rock_segment[1] else max_y

    return (min_x, max_x, min_y, max_y)


def add_rock_shape(current_terrain: list[bool, bool],
        bounds: tuple[int],
        in_rock_shape: list[tuple[int, int]]):
    # Adds a new shape of rock into the terrain map
    segment_start = in_rock_shape[0]
    segment_end = in_rock_shape[1]

    delta_x = segment_end[0] - segment_start[0]
    delta_y = segment_end[1] - segment_start[1]

    print(delta_x, delta_y, segment_start, segment_end)

    if delta_x != 0 and delta_y != 0:
        raise ValueError('line segment is diagonal')

    if delta_x < 0 or delta_y < 0:
        temp = segment_start
        segment_start = segment_end
        segment_end = temp

    delta_x, delta_y = abs(delta_x), abs(delta_y)

    print(delta_x, delta_y, segment_start, segment_end)

    if delta_x > 0:
        for i in range(delta_x):
            print('\t', i, delta_x, segment_start[0] - bounds[0] + i, segment_start[1] - bounds[2])
            current_terrain[segment_start[0] - bounds[0] + i][segment_start[1] - bounds[2]] = True
    elif delta_y > 0:
        for i in range(delta_y):
            print('\t', i, delta_y, segment_start[0] - bounds[0], segment_start[1] - bounds[2] + i)
            current_terrain[segment_start[0] - bounds[0]][segment_start[1] - bounds[2] + i] = True

    return current_terrain


def generate_terrain(rock_shapes: list[list[tuple[int, int]]],
        bounds: tuple[int]) -> list[bool, bool]:
    terrain = [[False] * (bounds[1] - bounds[0])] * (bounds[3] - bounds[2])
    print(len(terrain), len(terrain[0]))

    for rock in rock_shapes:
        terrain = add_rock_shape(terrain, bounds, rock)

    return terrain


def move_one_sand_block(terrain: list[bool, bool], current_sand_coords: tuple[int, int]):
    # Moves sand one space
    # Return terrain and sand_space if valid
    # Return updated terrain and False if came to rest
    # Return terrain and True if exited the map
    pass


def simulate_sand_movement(start_terrain: list[bool, bool]) -> int:
    # Simulates all of the sand movement
    # Returns the number of sand units that come to rest before overflow
    pass


def read_from_input(filename: str = 'input.txt') -> list[list[tuple[int, int]]]:
    lines: list[str] = []
    all_rock_coords: list[list[tuple[int, int]]] = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        rock_coords: list[tuple[int, int]] = []
        segments = [segment for segment in (line.strip()).split(' -> ')]

        for segment in segments:
            coords = [int(coord) for coord in segment.split(',')]
            rock_coords.append(coords)

        all_rock_coords.append(rock_coords)

    return all_rock_coords


if __name__ == '__main__':
    rock_shapes = read_from_input()
    bounds = get_boundaries(rock_shapes)
    print(bounds)
    generate_terrain(rock_shapes, bounds)