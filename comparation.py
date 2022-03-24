
def takeSecond(ele):
    """

    :param ele:
    :return: ele[0]
    """
    return ele[0]


random = [(2, 2), (4, 8), (10, 8), (1, 10)]
random.sort(key=takeSecond)
print(random)


