import numpy as np
import pandas as pd

with open("/Users/markus/Documents/Git/Python/2021/day03/test.txt", "r") as fp:
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


def find_removable_bit(bit_sequence) -> str:
    count = dict(zip(*np.unique(bit_sequence, return_counts=True)))
    if count['0'] > count['1']:
        return '1', '0'
    elif count['0'] < count['1']:
        return '0', '1'
    else:
        return 'even'


def part_02(binary_array):
    df_oxygen = pd.DataFrame(binary_array)

    for idx, j in enumerate(range(0, len(binary_array[0]))):
        if idx == len(binary_array[0]):
            break

        transformed_array = df_oxygen.transpose().to_numpy()
        oxygen_length = len(df_oxygen)
        counter = 0
        oxygen_drop_array = []
        starting_bit_to_remove = find_removable_bit(transformed_array[idx])
        for i in range(0, oxygen_length):

            if counter >= oxygen_length:
                continue

            if starting_bit_to_remove == 'even':
                starting_bit_to_remove = '0'

            cell = df_oxygen.iloc[counter][idx]
            if cell == starting_bit_to_remove:
                oxygen_drop_array.append(df_oxygen.iloc[counter].name)

            counter += 1

        df_oxygen = df_oxygen.drop(oxygen_drop_array)

    return df_oxygen


g, e = part_01(array)
print(int(g, 2) * int(e, 2))  # Part 1

oxygen = part_02(array)
decimal_oxygen = int(oxygen.iloc[0, :].to_string(header=False, index=False).replace("\n", ""), 2)
print("jee")
