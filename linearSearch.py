from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


if __name__ == '__main__':
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    sequence = [int(item) for item in user_input.split(',')]

    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    result = linear_search(sequence, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
