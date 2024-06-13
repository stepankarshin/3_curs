import show_last
import pytest
import json

def check_show_last():
    file = open('3_curs\operations.json')
    x = json.load(file)
    assert show_last() == x[:5]
