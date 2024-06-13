def show_last(file):
    res = []
    flag = 0
    for i in range(100):
        if file[-i -1]["state"] == "EXECUTED":
            res.append(file[-i -1])
            flag += 1
            if flag >= 5:
                break
    return res

def make_numb(text):
    numb = ""
    j = 0

    for i in text:
        numb += i
        j += 1

        if j == 4:
            numb += " "

        if j == 6:
            break

    numb += "** **** "
    numb += text[:4]

    return numb
