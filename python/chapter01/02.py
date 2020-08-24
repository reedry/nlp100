from functools import reduce


def main():
    p = "パトカー"
    t = "タクシー"
    print(reduce(lambda acc, s: acc + s[0] + s[1], zip(p, t), ""))


if __name__ == '__main__':
    main()
