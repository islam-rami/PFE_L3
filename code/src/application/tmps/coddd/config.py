import re
def calcul_nbr_td1(dic_prof, a=None, reliqua=None,structur=None):
    td = 0
    for section in dic_prof.keys():
        my_search = re.search(r"S[135]", section)
        if my_search != None:
            for module in dic_prof[section]:
                td = td + dic_prof[section][module]['TD']
    return td

def calcul_nbr_td2(dic_prof, a=None, reliqua=None,structur=None):

    td = 0

    for section in dic_prof:
        my_search = re.search(r"S[246]", section)
        if my_search != None:
            for module in dic_prof[section]:
                td = td + dic_prof[section][module]['TD']
    return td

def calcul_nbr_cour1(dic_prof, a=None, reliqua=None,structur=None):
    cour1 = 0
    for section in dic_prof:
        my_search = re.search(r"S[135]", section)
        if my_search != None:
            for module in dic_prof[section]:
                cour1 = cour1 + dic_prof[section][module]['COUR']
    return cour1

def calcul_nbr_cour2(dic_prof, a=None, reliqua=None,structur=None):
    cour2 = 0
    for section in dic_prof:
        my_search = re.search(r"S[246]", section)
        if my_search != None:
            for module in dic_prof[section]:
                cour2 = cour2 + dic_prof[section][module]['COUR']
    return cour2

def calcul_nbr_tp1(dic_prof, a=None, reliqua=None,structur=None):
    tp1 = 0
    for section in dic_prof:
        my_search = re.search(r"S[135]", section)
        if my_search != None:
            for module in dic_prof[section]:
                tp1 = tp1 + dic_prof[section][module]['TP']
    return tp1

def calcul_nbr_tp2(dic_prof, a=None, reliqua=None,structur=None):
    tp2 = 0
    for section in dic_prof:
        my_search = re.search(r"S[246]", section)
        if my_search != None:
            for module in dic_prof[section]:
                tp2 = tp2 + dic_prof[section][module]['TP']
    return tp2


def volum_cour1(a,struct, reliqua=None,structur=None):
    return struct["COUR1"] * 3

def volum_cour2(a, struct, reliqua=None,structur=None):
    return struct["COUR2"] * 3

def volum_td1(a, struct, reliqua=None,structur=None):
    return struct["TD1"] * 2


def volum_td2(a, struct, reliqua=None,structur=None):
    return struct["TD2"] * 2

def volum_tp1(a, struct, reliqua=None,structur=None):
    return struct["TP1"] * 1.5


def volum_tp2(a, struct, reliqua=None,structur=None):
    return struct["TP2"] * 1.5

def total_s2(a,struct, reliqua=None,structur=None):
    return (struct["VOLUM_COUR_2"]+struct["VOLUM_TD_2"]+struct["VOLUM_TP_2"])

def total_s1(a,struct, reliqua=None,structur=None):
    return (struct["VOLUM_COUR_1"]+struct["VOLUM_TD_1"]+struct["VOLUM_TP_1"])


def heures_supp_totale(a,struct, reliqua=None,structur=None):
    if (struct["TOTAL_S1"]+struct["TOTAL_S2"])-24 >=0:
        return  (struct["TOTAL_S1"]+struct["TOTAL_S2"])-24
    else:
        return 0


def heure_supp_s1(a, struct, reliqua=None, structur=None):
    if (struct["HEURES_SUPP_TOTALE"] > 0 and struct["TOTAL_S1"] > 12):
        if (struct["TOTAL_S2"] > 12):
            if struct["ENSEIGNANT"] in reliqua.keys():
                return struct["TOTAL_S1"] - 12 + reliqua[struct["ENSEIGNANT"]]
            else:
                return struct["TOTAL_S1"] - 12
        else:
            if struct["ENSEIGNANT"] in reliqua.keys():
                return (struct["HEURES_SUPP_TOTALE"] + reliqua[struct["ENSEIGNANT"]])
            else:
                return (struct["HEURES_SUPP_TOTALE"])
    else:
        if struct["ENSEIGNANT"] in reliqua.keys():
            return 0 + reliqua[struct["ENSEIGNANT"]]
        else:
            return 0

def heure_supp_s2(a,struct, reliqua=None,structur=None):
    if (struct["HEURES_SUPP_TOTALE"]>0 and struct["TOTAL_S2"]>12):

        if struct["HEURE_SUPP_S1"] - 8 > 0:
            add = struct["HEURE_SUPP_S1"] - 8
        else:
            add = 0
        if(struct["TOTAL_S1"]>12):

            return struct["TOTAL_S2"] - 12 + add
        else:
            return struct["HEURES_SUPP_TOTALE"]
    else:
        if struct["HEURE_SUPP_S1"] - 8 > 0:
            add = struct["HEURE_SUPP_S1"] - 8
        else:
            add = 0
        return add

def heure_supp_s1_max(a,struct, reliqua=None,structur=None):
    if (struct["HEURE_SUPP_S1"] -8) >0:
        return 8
    else:
        return struct["HEURE_SUPP_S1"]
def heure_supp_s2_max(a,struct, reliqua=None,structur=None):
    if (struct["HEURE_SUPP_S2"] -8) >0:
        return 8
    else:
        return struct["HEURE_SUPP_S2"]

def calcul_reliquat(a,struct, reliqua=None,structur=None):
    if (struct["HEURE_SUPP_S2"] - 8) > 0:
        return (struct["HEURE_SUPP_S2"] - 8)
    else:
        return 0
heures_sup_config = {
    "COUR1": calcul_nbr_cour1,
    "COUR2": calcul_nbr_cour2,
    "TD1": calcul_nbr_td1,
    "TD2": calcul_nbr_td2,
    "TP1": calcul_nbr_tp1,
    "TP2": calcul_nbr_tp2,
    "VOLUM_COUR_1": volum_cour1,
    "VOLUM_COUR_2": volum_cour2,
    "VOLUM_TD_1": volum_td1,
    "VOLUM_TD_2": volum_td2,
    "VOLUM_TP_1": volum_tp1,
    "VOLUM_TP_2": volum_tp2,
    "TOTAL_S1": total_s1,
    "TOTAL_S2": total_s2,
    "HEURES_SUPP_TOTALE":heures_supp_totale,
    "HEURE_SUPP_S1":heure_supp_s1,
    "HEURE_SUPP_S2":heure_supp_s2,
    "HEURE_SUPP_S1_max":heure_supp_s1_max,
    "HEURE_SUPP_S2_max":heure_supp_s2_max,
    "RELIQUAT":calcul_reliquat
}


