def main():
    sentence = "Now I need a drink, alcoholic of course, after the heavy " \
               "lectures involving quantum mechanics."
    sentence = sentence.replace(",", "").replace(".", "")
    print("".join(map(lambda s: str(len(s)), sentence.split(" "))))


if __name__ == '__main__':
    main()
