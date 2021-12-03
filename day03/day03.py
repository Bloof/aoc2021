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


def part_02(binary_array):
    df = pd.DataFrame(binary_array)

    df_oxygen = gas_diagnostics(binary_array, df, False)
    df_c02 = gas_diagnostics(binary_array, df, True)

    return df_oxygen, df_c02


def find_removable_bit(bit_sequence):
    count = dict(zip(*np.unique(bit_sequence, return_counts=True)))
    if count['0'] > count['1']:
        return '1'
    elif count['0'] < count['1']:
        return '0'
    else:
        return 'even'


def switch_bit(bit, is_c02):
    if bit == '1' and is_c02:
        return '0'
    elif bit == '0' and is_c02:
        return '1'


def gas_diagnostics(binary_array, df, is_c02):
    for idx, j in enumerate(range(0, len(binary_array[0]))):
        if len(df) == 1:
            break

        vertical_oxygen = df.transpose().to_numpy()

        df_length = len(df)
        counter = 0
        drop_array = []
        bit_to_remove = find_removable_bit(vertical_oxygen[idx])

        if bit_to_remove == 'even':
            bit_to_remove = '0'

        bit_to_remove = switch_bit(bit_to_remove, is_c02) if is_c02 else bit_to_remove

        for i in range(0, df_length):

            if counter >= df_length:
                continue

            cell = df.iloc[counter][idx]
            if cell == bit_to_remove:
                drop_array.append(df.iloc[counter].name)

            counter += 1

        df = df.drop(drop_array)
    return df


g, e = part_01(array)
print(int(g, 2) * int(e, 2))  # Part 1

oxygen, c02 = part_02(array)
decimal_oxygen = int(oxygen.iloc[0, :].to_string(header=False, index=False).replace("\n", ""), 2)
decimal_c02 = int(c02.iloc[0, :].to_string(header=False, index=False).replace("\n", ""), 2)
print(decimal_oxygen * decimal_c02)
