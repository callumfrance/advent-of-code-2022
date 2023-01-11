from typing import Final

SIGNAL_CYCLE_CHECKS: Final = (
    20,
    60,
    100,
    140,
    180,
    220
)


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


if __name__ == '__main__':
    instructions = parse_input()
    x_history = perform_operations(instructions, [1])
    print(x_history)
    x_check_sum = perform_signal_cycle_checks(x_history)
    print(x_check_sum)