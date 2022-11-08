from calcul_des_heurs_supplimentaires import calcul
import config as con
import pytest
import json
@pytest.fixture()
def fich():
    with open(r"configuration//test_calcul_des_heurs_supplimentaires.json", "r",encoding="utf-8") as fil:
        try:
            return json.load(fil)
        except ValueError as e:
            print("invalid json: "+  e)
            return None  # or: raise

def test_calcul_nbr_td1(fich):
    list=fich["test_calcul_nbr_td1"]
    for i in list :
        assert con.calcul_nbr_td1(i["value"]) == i["result"]


def test_calcul_nbr_td2(fich):
    list=fich["test_calcul_nbr_td2"]
    for i in list :
        assert con.calcul_nbr_td2(i["value"]) == i["result"]


def test_calcul_nbr_tp1(fich):
    list=fich["test_calcul_nbr_tp1"]
    for i in list :
        assert con.calcul_nbr_tp1(i["value"]) == i["result"]

def test_calcul_nbr_tp2(fich):
    list =fich["test_calcul_nbr_tp2"]
    for i in list:
        assert con.calcul_nbr_tp2(i["value"]) == i["result"]




def test_calcul_nbr_cour1(fich):
    list=fich["test_calcul_nbr_cour1"]
    for i in list :
        assert con.calcul_nbr_cour1(i["value"]) ==i["result"]




def test_calcul_nbr_cour2(fich):
    list=fich["test_calcul_nbr_cour2"]
    for i in list:
        assert con.calcul_nbr_cour2(i["value"]) == i["result"]



def test_volum_cour1(fich):
    list=fich["test_volum_cour1"]
    for i in list:
        b = None
        assert con.volum_cour1(b, i["value"]) == i["result"]

def test_volum_cour2(fich):
    list=fich["test_volum_cour2"]
    for i in list :
        b = None
        assert con.volum_cour2(b, i["value"]) == i["result"]


def test_volum_td1(fich):
    list=fich["test_volum_td1"]
    for i in list:
        b = None
        assert con.volum_td1(b, i["value"]) == i["result"]


def test_volum_td2(fich):
    list=fich["test_volum_td2"]
    for i in list :
        b = None
        assert con.volum_td2(b, i["value"]) == i["result"]



def test_volum_tp1(fich):
    list=fich["test_volum_tp1"]
    for i in list :
        b = None
        assert con.volum_tp1(b, i["value"]) == i["result"]


def test_volum_tp2(fich):
    list=fich["test_volum_tp2"]
    for i in list :
        b = None

        assert con.volum_tp2(b, i["value"]) == i["result"]

def test_total_s1(fich):
    list=fich["test_total_s1"]
    for i in list :
        b = None
        assert con.total_s1(b, i["value"]) == i["result"]


def test_total_s2(fich):
    list=fich["test_total_s2"]
    for i in list :
        b = None
        assert con.total_s2(b, i["value"]) == i["result"]





def test_calculate(fich):
    list=fich["test_calculate"]
    relicat={}
    for i in list:
        calc = calcul()
        calc.calculate(i["value"],relicat,"config.json")
        assert calc.get__colonne() ==i["result"]