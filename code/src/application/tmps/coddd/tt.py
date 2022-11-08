import json
import xlsxwriter
import os
from extraction_information import formProf
from extraction_information import formMoule
import utilisation as ut
from convrtir import convertirToCsv
from extraction_information import mise_a_jour
from calcul_des_heurs_supplimentaires import calcul



convertirToCsv.convertirToCsv("result/reliqua.xlsx","Sheet1","reliquat.csv")
a = convertirToCsv()
a.csvToList("reliquat.csv")
b = a.get__data()
print(b)
dd = formProf()
dd.form_reliquat(b)
print(dd.get__structure())

a={"GUERAICHI": {"L1-S2-1": {"ALG02": {"COUR": 1, "TD": 4, "TP": 0}}},
                            "FEREDJ": {"L1-S2-1": {"ALG02": {"COUR": 0, "TD": 0, "TP": 2}},
                            "L2-ACAD-S4-C": {"ARCHIT": {"COUR": 1, "TD": 3, "TP": 0}}},
                            "IBELAIDEN": {"L1-S2-1": {"ALG02": {"COUR": 0, "TD": 0, "TP": 2}}},
                            "KHETTAR": {"L1-S2-2": {"ALG02": {"COUR": 1, "TD": 4, "TP": 0}}},
                            "MEHDI": {"L1-S2-2": {"ALG02": {"COUR": 0, "TD": 0, "TP": 4}},
                            "L1-S2-9": {"ALG02": {"COUR": 100, "TD": 0, "TP": 4}}},
                            "BABA ALI R.": {"L1-S2-3": {"ALG02": {"COUR": 1, "TD": 0, "TP": 4}}}
                                   }
f = {}
clc = calcul()
clc.calculate(a,f,"fff")
print("\n"*10)
print(clc.get__colonne())
