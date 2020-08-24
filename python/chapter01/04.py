def main():
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New " \
        "Nations Might Also Sign Peace Security Clause. Arthur King Can."
    single_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    sentence = sentence.replace(".", "")
    res = dict()
    for i, w in enumerate(sentence.split(" "), start=1):
        if i in single_list:
            res[w[0]] = i
        else:
            res[w[0:2]] = i
    return res


if __name__ == "__main__":
    print(main())
