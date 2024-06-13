from utils import show_last
import pytest
import json
def test_show_last_1():
    with open('..\operations.json', "r", encoding="utf-8") as file:
        x = json.load(file)
    assert show_last(x)[0]["id"] == x[-1]["id"]

def test_show_last_2():
    with open('..\operations.json', "r", encoding="utf-8") as file:
        x = json.load(file)
    assert show_last(x)[1]["id"] == x[-2]["id"]

def test_show_last_3():
    with open('..\operations.json', "r", encoding="utf-8") as file:
        x = json.load(file)
    assert show_last(x)[2]["id"] == x[-3]["id"]

def test_show_last_4():
    with open('..\operations.json', "r", encoding="utf-8") as file:
        x = json.load(file)
    assert show_last(x)[3]["id"] == x[-4]["id"]

def test_show_last_5():
    with open('..\operations.json', "r", encoding="utf-8") as file:
        x = json.load(file)
    assert show_last(x)[4]["id"] == x[-6]["id"]
