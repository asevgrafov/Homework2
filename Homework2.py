path1 = '1.txt'
path2 = '2.txt'
path3 = '3.txt'
path4 = '4.txt'
path5 = '5.txt'
path6 = '6.txt'


def read_file(path: str) -> list:
    """Открываем файл на чтение и записываем значения в массив"""
    with open(path, 'r') as file:
        lines = file.readlines()
    a = [[int(n) for n in x.split()] for x in lines]
    print(a)
    return a


def calculate(a: list) -> int:
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                count += 1
                check(a, i, j)
    print(count)
    return count


def check(a: list, i: int, j: int) -> int:
    if i < 0 or i >= len(a):
        return 0
    if j < 0 or j >= len(a[i]):
        return 0
    if a[i][j] == 0:
        return 0
    else:
        a[i][j] = 0
        check(a, i, j + 1)
        check(a, i - 1, j)
        check(a, i + 1, j)
        check(a, i, j - 1)
    return 1


calculate(read_file(path1))
calculate(read_file(path2))
calculate(read_file(path3))
calculate(read_file(path4))
calculate(read_file(path5))
calculate(read_file(path6))

