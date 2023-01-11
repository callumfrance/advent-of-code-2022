from typing import Final

SIGNAL_CYCLE_CHECKS: Final = (
    20,
    60,
    100,
    140,
    180,
    220
)


INITIAL_CRT = ['.' * 40] * 6

def noop(x_history: list[int], curr_x: int):
    x_history.append(curr_x)

    return x_history


def addx(x_change: int, x_history: list[int], curr_x: int):
    x_history.append(curr_x)
    x_history.append(curr_x + x_change)

    return x_history


def perform_operation(instruction: list[str, int], x_history: list[int]):
    if instruction[0] == 'noop':
        x_history = noop(x_history, x_history[-1])
    else:
        x_history = addx(instruction[1], x_history, x_history[-1])

    return x_history


def perform_operations(instructions: list[list[int, str]], x_history: list[int]) -> list[int]:
    for instruction in instructions:
        x_history = perform_operation(instruction, x_history)

    return x_history


def perform_signal_cycle_checks(x_history: list[str]) -> int:
    x_check_sum = 0

    for cycle_number in SIGNAL_CYCLE_CHECKS:
        x_check = cycle_number * x_history[cycle_number - 1]
        print(x_check, '=', cycle_number, '*', x_history[cycle_number - 1])
        x_check_sum += x_check

    return x_check_sum


def parse_input(filename: str = 'input.txt') -> list[list[str, int]]:
    lines = []
    instructions: list[list[str, int]] = []

    with open(filename, 'r') as fn:
        lines = fn.readlines()

    for line in lines:
        pieces = (line.strip()).split(' ')

        if len(pieces) == 2:
            pieces[1] = int(pieces[1])

        instructions.append(pieces)

    return instructions


def draw_crt(crt: list[list[str]], x_history: list[str]):
    pixel_row_length = len(crt[0]) # 40
    pixel_col_height = len(crt) # 6
    total_pixels = pixel_col_height * pixel_row_length # 240

    final_crt = []

    for index, row in enumerate(crt):
        pixel_offset = index * pixel_row_length

        for pixel in range(pixel_row_length):
            # pixel positions 0 to 39 for one row
            # get current sprite location
            sprite_location = x_history[pixel_offset + pixel]

            if abs(pixel - sprite_location) <= 1:
                # we can print here
                row = row[:pixel] + '#' + row[(pixel + 1):]

        final_crt.append(row)

    return final_crt


def print_crt(crt: list[list[str]] = INITIAL_CRT):
    for row in crt:
        print(row)


if __name__ == '__main__':
    instructions = parse_input()
    x_history = perform_operations(instructions, [1])
    print(x_history)
    x_check_sum = perform_signal_cycle_checks(x_history)
    print(x_check_sum)

    print_crt()
    crt = draw_crt(INITIAL_CRT, x_history)
    print_crt(crt)