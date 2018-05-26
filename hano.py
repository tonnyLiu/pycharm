def hano(n: object, a: object, b: object, c: object) -> object:
    '''
    :param n: 盘子的总数
    :param a: 起始的塔
    :param b: 过渡塔:
    :param c: 目标塔
    :return: 无
    '''
    if(n<1):
        return None
    hano(n-1, a, c, b)
    print(a, "-->", c)
    hano(n-1, b, a, c)

a = "A"
b = "B"
c = "C"

hano(2, a, b, c)