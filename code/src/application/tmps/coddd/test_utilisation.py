import pytest
import utilisation as ut
from convrtir import convertirToCsv
import json
@pytest.fixture()
def fich():
    with open(r"configuration//test_utilisation.json", "r") as fil:
        try:
            return json.load(fil)
        except ValueError as e:
            print("invalid json: "+  e)
            return None  # or: raise


def test_construireLIne(fich):
    l=fich["test_construireLIne"]
    for i in l:
        test=i
        valeur=test["value"]
        assert  ut.construireLIne(valeur[0],valeur[1])== test["result"]


def test_transformer(fich):
    l = fich["test_transformer"]
    for i in l:
        test = i
        a = convertirToCsv()
        a.csvToList(test["value"])
        b = ut.transformer(a.get__data())
        assert b == test["result"]






