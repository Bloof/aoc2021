import numpy as np
import pandas as pd

with open("/Users/markus/Documents/Git/Python/2021/day03/day03.txt", "r") as fp:
    file = fp.readlines()

array = []

for line in file:
    temp = line.strip("\n")
    array.append([*temp])


def part_01(binary_array):
    gamma = ""
    epsilon = ""
    df = pd.DataFrame(binary_array)
    transformed_array = df.transpose().to_numpy()

    for i in transformed_array:
        count = dict(zip(*np.unique(i, return_counts=True)))
        if count['0'] > count['1']:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else:
            gamma = gamma + '1'
            epsilon = epsilon + '0'

    return gamma, epsilon


def find_oxygen_bit(bit_sequence):
    count = dict(zip(*np.unique(bit_sequence, return_counts=True)))
    if count['0'] > count['1']:
        return '1'
    elif count['0'] < count['1']:
        return '0'
    else:
        return 'even'


def find_c02_bit(bit_sequence):
    count = dict(zip(*np.unique(bit_sequence, return_counts=True)))
    if count['0'] < count['1']:
        return '1'
    elif count['0'] > count['1']:
        return '0'
    else:
        return 'even'


def part_02(binary_array):
    df_oxygen = pd.DataFrame(binary_array)
    df_c02 = pd.DataFrame(binary_array)

    for idx, j in enumerate(range(0, len(binary_array[0]))):
        if len(df_oxygen) == 1:
            break

        vertical_oxygen = df_oxygen.transpose().to_numpy()

        oxygen_length = len(df_oxygen)
        counter = 0
        oxygen_drop_array = []
        oxygen_to_remove = find_oxygen_bit(vertical_oxygen[idx])

        for i in range(0, oxygen_length):

            if counter >= oxygen_length:
                continue

            if oxygen_to_remove == 'even':
                oxygen_to_remove = '0'

            oxygen_cell = df_oxygen.iloc[counter][idx]
            if oxygen_cell == oxygen_to_remove:
                oxygen_drop_array.append(df_oxygen.iloc[counter].name)

            counter += 1

        df_oxygen = df_oxygen.drop(oxygen_drop_array)

    for idx, j in enumerate(range(0, len(binary_array[0]))):
        if len(df_c02) == 1:
            break

        vertical_c02 = df_c02.transpose().to_numpy()
        c02_length = len(df_c02)
        counter = 0
        c02_drop_array = []
        c02_to_remove = find_c02_bit(vertical_c02[idx])

        for i in range(0, c02_length):

            if counter >= c02_length:
                continue

            if c02_to_remove == 'even':
                c02_to_remove = '1'

            c02_cell = df_c02.iloc[counter][idx]
            if c02_cell == c02_to_remove:
                c02_drop_array.append(df_c02.iloc[counter].name)

            counter += 1

        df_c02 = df_c02.drop(c02_drop_array)

    return df_oxygen, df_c02


g, e = part_01(array)
print(int(g, 2) * int(e, 2))  # Part 1

oxygen, c02 = part_02(array)
decimal_oxygen = int(oxygen.iloc[0, :].to_string(header=False, index=False).replace("\n", ""), 2)
decimal_c02 = int(c02.iloc[0, :].to_string(header=False, index=False).replace("\n", ""), 2)
print(decimal_oxygen*decimal_c02)
