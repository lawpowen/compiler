import re
import sys


def serial_of_words(_str):
    if _str == "BEGIN":
        return "Begin"
    elif _str == "END":
        return "End"
    elif _str == "FOR":
        return "For"
    elif _str == "IF":
        return "If"
    elif _str == "THEN":
        return "Then"
    elif _str == "ELSE":
        return "Else"
    elif ident(_str):
        return "Ident(" + _str + ")"
    elif str.isdigit(_str):
        return "Int(" + str(int(_str)) + ")"
    elif _str == ":":
        return "Colon"
    elif _str == "+":
        return "Plus"
    elif _str == "*":
        return "Star"
    elif _str == ",":
        return "Comma"
    elif _str == "(":
        return "LParenthesis"
    elif _str == ")":
        return "RParenthesis"
    elif _str == ":=":
        return "Assign"
    else:
        return False


def ident(_str):  # 正则表达标识符
    pattern = re.compile(r'([a-zA-Z]+)(\d*)')
    if re.match(pattern, _str, 0):
        return True
    else:
        return False


def output(_str):
    print(serial_of_words(_str))


f = open(sys.argv[1], 'r')
code = f.read()  # 读入文件
blank = " \n\r\t"

for line in code.split("\n"):  # 处理每一行
    word = ""  # 缓冲区
    digit = False
    skip = False
    for index, letter in enumerate(line):
        if skip:
            skip = False
            continue
        if str.isdigit(letter):
            digit = not bool(word)  # word空，当前读到数字
            word += letter
            continue
        elif str.isalpha(letter):
            if digit:
                output(word)
                word = ""
                digit = False
            word += letter
            continue
        else:
            if word:
                output(word)
                word = ""
                digit = False
            if letter in blank:
                continue
            if index != len(line) - 1 and serial_of_words(line[index:index + 2]):
                output(line[index:index + 2])
                skip = True
            else:
                if not serial_of_words(letter):
                    print("Unknown")
                    exit(0)
                output(letter)
            word = ""
    if word != "":
        output(word)
f.close()
