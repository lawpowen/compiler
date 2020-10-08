import re
import sys


def serial_of_words(str):
    if str == "BEGIN":
        return "Begin"
    elif str == "END":
        return "End"
    elif str == "FOR":
        return "For"
    elif str == "IF":
        return "If"
    elif str == "THEN":
        return "Then"
    elif str == "ELSE":
        return "Else"
    elif ident(str):
        return "Ident(" + str + ")"
    elif isint(str):
        return "Int(" + str + ")"
    elif str == ":":
        return "Colon"
    elif str == "+":
        return "Plus"
    elif str == "*":
        return "Star"
    elif str == ",":
        return "Comma"
    elif str == "(":
        return "LParenthesis"
    elif str == ")":
        return "RParenthesis"
    elif str == ":=":
        return "Assign"
    else:
        return False


def ident(str):  # 正则表达标识符
    pattern = re.compile(r'([a-zA-Z]+)(\d*)')
    if re.match(pattern, str, 0):
        return True
    else:
        return False


def isint(str):
    if str.isdigit(str):
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
        if isint(letter):
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
