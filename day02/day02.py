with open("/Users/markus/Documents/Git/Python/2021/day02/day02.txt", "r") as fp:
    file = fp.readlines()


def steer_submarine(array):
    x, y, y2, aim = 0, 0, 0, 0

    for action in array:
        match action[0]:
            case "forward":
                x += int(action[1])
                if aim > 0:
                    y2 = y2 + (int(action[1]) * aim)
                else:
                    continue
            case "down":
                y += int(action[1])
                aim += int(action[1])
            case "up":
                y -= int(action[1])
                aim -= int(action[1])
    return (x * y), (x * y2)


commands = []
for row in file:
    temp = row.split()
    commands.append(temp)

part1, part2 = steer_submarine(commands)
print(part1)
print(part2)
