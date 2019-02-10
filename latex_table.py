import numpy as np

string = """
a & 1.1 & 2 \\
b & 2.2 & 3 \\
"""

def stress(string):
    lines = string.split('\n')
    all_numbers = [[float(v.strip()) for v in line.strip('\\').split('&')[1:] if v.strip() != ''] for line in lines]

    num = max([len(numbers) for numbers in all_numbers])
    max_numbers = np.array([numbers for numbers in all_numbers if len(numbers) == num]).max(0)
    for numbers, line in zip(all_numbers, lines):
        if len(numbers) != num:
            new_line = line
        else:
            numbers = ['%0.3f'%(number) if number != max_numbers[index] else '\stress{' + '%0.3f'%(number) + '}' for index, number in enumerate(numbers)]
            new_line = line.split('&')[0].strip() + ' & ' + ' & '.join(numbers) + ' \\\\'
            pass
        print(new_line)
        continue
    #print(numbers)
    return

stress(string)
