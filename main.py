from utils import show_last
from utils import make_numb
import json


with open('operations.json', "r", encoding="utf-8") as file:
    x = json.load(file)

res = show_last(x)

for i in range(4, -1, -1):
    flag_from = 0;
    flag_to = 0;
    print(f"{res[i]["date"][:10]} {res[i]["description"]}")

    if res[i]["description"] == "Открытие вклада":

        for a in res[i]["to"]:

            if a.isdigit():
                break

            flag_to += 1

        numb_to = make_numb(res[i]["to"][flag_to:])
        print(f"{res[i]["to"][:flag_to]}{numb_to}")

    else:

        for a in res[i]["from"]:

            if a.isdigit():
                break

            flag_from += 1

        for a in res[i]["to"]:

            if a.isdigit():
                break

            flag_to += 1

            numb_to = make_numb(res[i]["to"][flag_to:])
            numb_from = make_numb(res[i]["from"][flag_from:])

        print(f"{res[i]["from"][:flag_from]}{numb_from} -> {res[i]["to"][:flag_to]}{numb_to}")

    print(f"{res[i]["operationAmount"]["amount"]} {res[i]["operationAmount"]["currency"]["name"]}\n")
