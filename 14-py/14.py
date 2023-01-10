from typing import Final

SAND_ORIGIN: Final = [500, 0]

SAND_MOVES: Final = [(0, 1), (-1, 1), (1, 1)]


def get_boundaries(rock_shapes: list[list[tuple[int, int]]]):
    (min_x, max_x, min_y, max_y) = (SAND_ORIGIN[0], SAND_ORIGIN[0], SAND_ORIGIN[1], SAND_ORIGIN[1])

    for rock_shape in rock_shapes:
        for rock_segment in rock_shape:
            min_x = rock_segment[0] if min_x > rock_segment[0] else min_x
            max_x = rock_segment[0] if max_x < rock_segment[0] else max_x
            min_y = rock_segment[1] if min_y > rock_segment[1] else min_y
            max_y = rock_segment[1] if max_y < rock_segment[1] else max_y

    return min_x, max_x, min_y, max_y


def add_rock_shape(current_terrain: list[bool, bool], in_rock_shape: list[tuple[int, int]]):
    # Adds a new shape of rock into the terrain map
    pass


def generate_terrain(min_x: int, max_x: int, min_y: int, max_y: int) -> list[bool, bool]:
    # Build the terrain from scratch using known boundaries
    pass


def move_sand_one_block(terrain: list[bool, bool], current_sand_coords: tuple[int, int]):
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
    min_x, max_x, min_y, max_y = get_boundaries(rock_shapes)
    print((get_boundaries(rock_shapes)))