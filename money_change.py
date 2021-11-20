# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    tens = int(money / 10)
    money -= tens * 10
    fives = int(money / 5)
    money -= fives * 5
    return tens + fives + money


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
