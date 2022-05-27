def calculator(key):
    try:
        return int(eval(key))
    except:
        s = 'Invalid Input'
        return s


if __name__ == '__main__':
    # string123 = '(2 +-+* 3)'
    # #string123 = 'hello'
    # rule = re.compile("[\d\W]")
    # if rule.fullmatch(string123) is not None:
    #     print("match")
    # else:
    #     print("NO")
    print(calculator("hello"))
