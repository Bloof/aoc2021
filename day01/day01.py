with open("/Users/markus/Documents/Git/Python/2021/day01/day01.txt", "r") as fp:
    file = fp.readlines()

    def calc_depths(array):
        depth_increased = 0
        for idx, depth in enumerate(array):
            if idx == 0:
                continue;

            if array[idx - 1] < depth:
                depth_increased += 1

        return depth_increased


# Part 1 -----

    depths = [int(i.split("\n")[0]) for i in file]
    result = 0
    result = calc_depths(depths)

    print(result)  # Part 1

# Part 2 -----

    part2 = []
    counter = 0
    length = len(depths)
    for idx, depth in enumerate(depths):
        if counter + 2 >= length:
            finalElement = depths[length - 1] + depths[length - 2] + depths[length - 3]
            part2.append(finalElement)
            break;
        element = depths[counter] + depths[counter + 1] + depths[counter + 2]
        part2.append(element)
        counter += 1

    result2 = calc_depths(part2)
    print(result2) # Part 2


