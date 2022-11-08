import utilisation as ut
from extraction_information import formProf
from extraction_information import formMoule
from convrtir import convertirToCsv
import json
import pytest

@pytest.fixture()
def fich():
    with open(r"configuration//test_extraction_information.json", "r",encoding="utf-8") as fil:
        try:
            return json.load(fil)
        except ValueError as e:
            print("invalid json: "+  e)
            return None  # or: raise




def test_dic_prof(fich):
    list=fich["test_dic_prof"]
    for i in list:
        assert formProf.dic_prof(i["value"]) ==i["result"]


def test_mise_ajour(fich):
    list =fich["test_mise_ajour"]
    for i in list :
        d=i["dic"]
        formProf.mise_ajour(d, i["value"])
        assert d == i["result"]
    dic = {'GUERAICHI': {'L1-S2-1': {'ALG02': {'COUR': 1, 'TD': 4, 'TP': 0}}},
           'FEREDJ': {'L1-S2-1': {'ALG02': {'COUR': 0, 'TD': 0, 'TP': 2}},
                      'L2-ACAD-S4-C': {'ARCHIT': {'COUR': 1, 'TD': 3, 'TP': 0}}},
           'IBELAIDEN': {'L1-S2-1': {'ALG02': {'COUR': 0, 'TD': 0, 'TP': 2}}}
           }
    # test la foncyion mise a jour si le prof n'existe pas

def test_form_final(fich):
    list=fich["test_form_final"]
    for i in list :

        org_s1=i["value"][0]

        org_s2 = i["value"][1]
        b = formProf()
        b.form_final(org_s1, org_s2)
        assert b.get__structure() ==i["result"]





def test_ligne_modul(fich):
    list = fich["test_ligne_modul"]
    for i in list:
        assert formMoule.ligne_modul(i["value"]) ==i["result"]



def test_form_modul(fich):
    list=fich["test_form_modul"]
    for i in list :
        a = convertirToCsv()
        a.csvToList(i["value"])
        b = ut.transformer(a.get__data())
        d = formMoule()
        d.form_modul(b)
        assert d.get__structureModule() == i["result"]

