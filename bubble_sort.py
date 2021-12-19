def sort(data):
    """

    :param data:
    :return:
    """
    iteration = len(data)

    while iteration > 0:

        for i in range(0, iteration - 1):

            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

        iteration -= 1

    return data


if __name__ == "__main__":
    sort_this = [10, 2, 7, 4, 8, 42, 11, 35, 0, 3, 6, 15, 12]
    print(sort(sort_this))