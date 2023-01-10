def range_size(a: [int, int]):
    return a[1] - a[0] + 1


def sorted_ranges(a: [int, int], b: [int, int]):
    if range_size(a) > range_size(b):
        return [a, b]
    else:
        return [b, a]


def full_range_containment(bigger: [int, int], smaller: [int, int]):
    if bigger[0] <= smaller[0] and bigger[1] >= smaller[1]:
        return True
    else:
        return False


def range_check(line: [[int, int], [int, int]]):
    line = sorted_ranges(line[0], line[1])
    return 1 if full_range_containment(line[0], line[1]) else 0


def read_file(fname: str = 'input.txt'):
    values = []
    with open(fname, 'r') as f:
        raw_pairs = f.readlines()
        pairs = [i.split(',') for i in raw_pairs]

        for pair in pairs:
            clean_pair = []
            for pair_range in pair:
                clean_pair.append([int(i) for i in (pair_range.strip()).split('-')])

            values.append(clean_pair)

    return values


def main():
    lines: [[int, int], [int, int]] = read_file()
    contain_count = 0

    for line in lines:
        contain_count += range_check(line)

    return contain_count


if __name__ == '__main__':
    print(main())