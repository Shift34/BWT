def encoding(text: str):
    sort_list = []
    for n in range(0, len(text)):
        text1 = text[n:] + text[:n]
        sort_list.append(text1)
    sort_list.sort()
    list_last_symbol = []
    for n in sort_list:
        list_last_symbol.append(n[-1])
    text1 = ""
    number = 1
    for n in range(1, len(list_last_symbol)):
        if list_last_symbol[n - 1] == list_last_symbol[n]:
            number += 1
        else:
            text1 += list_last_symbol[n - 1] + str(number)
            number = 1
    text1 += list_last_symbol[n] + str(number)
    index = sort_list.index(text)
    text1 = text1 + "," + str(index)
    return text1


def decoding(text: tuple):
    my_list = []
    text1 = ""
    text_ = ""
    m = 1
    n = 0
    while n < len(text[0]):
        text_ = text[0][n]
        while str(text[0][n + 1:m + 1]).isdigit() and m < len(text[0]):
            m += 1
        text1 += text[0][n] * int(text[0][n + 1:m])
        n = m
        m = n + 1
    text2 = sorted(text1)
    my_list = list(text2)
    massiv = my_list.copy()
    n = 1
    start = 0
    char = ""
    for n in range(n, len(text2) - 1):
        for i in range(0, len(text2)):
            if char != massiv[i][0]:
                start = 0
            text3 = massiv[i][0]
            index = text1.index(text3, start)
            start = index + 1
            my_list[i] += massiv[index][-1]
            char = massiv[i][0]
            pass
        massiv = my_list.copy()
        start = 0
    for i in range(0, len(text1)):
        my_list[i] += text1[i]
    return my_list[int(text[1])]


input = open("Input.txt", 'r', encoding="utf-8")
text = input.read()
input.close()

f = open("Encoding.txt", "w", encoding="utf-8")
text = encoding(text)
f.write(text)
f.close()

f = open("Encoding.txt", "r", encoding="utf-8")
text = f.read()
rle = text[0:text.rfind(",")]
index = text[text.rfind(",") + 1 :]
list1 = [rle, index]
t = tuple(list1)
f.close()

f1 = open("Decoding.txt", "w", encoding="utf-8")
f1.write(decoding(t))
f1.close()
