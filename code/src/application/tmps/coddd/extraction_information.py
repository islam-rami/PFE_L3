import re
class formProf:
    def __init__(self):
        self.__structure_prof = None

#construire un dictionaire  où la clé est un nom de prof

    @staticmethod
    def dic_prof(dic_line):
        dic={}
        dic_upper={}
        for i in dic_line.keys():
            dic_upper[i.upper()]=dic_line[i]

        for i in  dic_upper.keys():
            if i !="SECTION" and i!="MODULE":
                if dic_upper[i] not in dic and len(dic_upper[i].replace(" ","")) >1:
                    prof = dic_upper[i]
                    cour = 0
                    td = 0
                    tp = 0
                    for j in dic_upper.keys():
                        if dic_upper[j] == prof:
                            if j[:2] == "TD":
                                td = td + 1
                            if j[:2] == "TP":
                                tp = tp + 1
                            if j[:4]=="COUR":
                                cour=cour+1
                    my_search = re.search(r"(.*:)", dic_upper["MODULE"])
                    if my_search != None:
                        my_s = my_search.group()
                        my_s = my_s.replace(" ", "")
                        my_s = my_s.replace(":","")
                    else:
                        my_s=dic_upper["MODULE"].replace(" ", "")
                        my_s = my_s.replace("\n", "")


                    dic[prof]={dic_upper["SECTION"]:{ my_s:{"COUR":cour,"TD":td,"TP":tp}   }}

        return dic

# mise_à_jour dant le dictionnaire qui contient les profs
    @staticmethod
    def mise_ajour(dic_final,dic_lin):
        for i in dic_lin.keys():
            if i  in dic_final.keys(): # si le prof exist
                dic_section_line=dic_lin[i]
                ke= [j for j in dic_section_line.keys()]
                key1=ke[0]
                if key1 in dic_final[i].keys(): #si la section exist
                    dic_modul_line = dic_section_line[key1]
                    k = [j for j in dic_modul_line.keys()]
                    key2 = k[0]
                    if key2 in dic_final[i][key1].keys(): #si le modul exist
                        dic_final[i][key1][key2]["COUR"] +=dic_modul_line[key2]["COUR"]
                        dic_final[i][key1][key2]["TD"] += dic_modul_line[key2]["TD"]
                        dic_final[i][key1][key2]["TP"] += dic_modul_line[key2]["TP"]
                    else:
                        dic_final[i][key1][key2]=dic_modul_line[key2]
                else:
                    dic_final[i][key1]=dic_section_line[key1]
            else:
                dic_final[i]=dic_lin[i]

# un dictionnaire qui contient tous les profs comme clé et les valeurs sont les modules aves les sections qui sont affecter à chaque prof
    def form_final(self,list1,list2):
        dic={}
        for i in list1:
            d = formProf.dic_prof(i)
            formProf.mise_ajour(dic,d)
        for i in list2:
            d = formProf.dic_prof(i)
            formProf.mise_ajour(dic, d)
        self.__structure_prof = dic

    def get__structure(self):
        return self.__structure_prof

    def form_reliquat(self,list):
        dic = {}

        for i in range(1,len(list)):
            p=list[i]
            #print(p)
            dic[p[0]] = int(p[1])
        self.__structure_prof = dic


class formMoule:

    def __init__(self):
        self.__structureModule = None


    # cree  une ligne de module avec le nombre de seance qui lui a corespend en tp td et en cour
    @staticmethod
    def ligne_modul(dic):
        dic_nbr_seance = {}
        dic_upper = {}
        for i in dic.keys():
            if i.upper() == "COURS":
                dic_upper["COUR"] = dic[i]


            else:
                dic_upper[i.upper()] = dic[i]

        my_search = re.search(r"(.*:)", dic_upper["MODULE"])
        if my_search != None:
            my_s = my_search.group()
            my_s = my_s.replace(" ", "")
            my_s = my_s.replace(":", "")
        else:
            my_s = dic_upper["MODULE"].replace(" ", "")
            my_s = my_s.replace("\n", "")

        dic_nbr_seance[my_s] = {"COUR": dic_upper["COUR"]}
        if "TD" in dic_upper.keys():
            dic_nbr_seance[my_s]["TD"] = dic_upper["TD"]
        if "TP" in dic_upper.keys():
            dic_nbr_seance[my_s]["TP"] = dic_upper["TP"]
        return dic_nbr_seance


    def form_modul(self,list_modul):
        dic = {}
        for i in list_modul:
            d = formMoule.ligne_modul(i)
            k = [j for j in d.keys()]
            key = k[0]
            if key not in dic.keys():
                dic[key]=d[key]

        self.__structureModule = dic

    def get__structureModule(self):
        return self.__structureModule


class mise_a_jour:
    def __init__(self):
        self.__strc=None

    def get__strc(self):
        return self.__strc
    # mise a jour nombre de seance dans le dictionaire des enseignant

    def ajouter_nbr_seance(self,p, modul1 ,modul2):
        prof=p
        for i in prof:
            for j in prof[i]:

                if re.search(r"S[246]", j) != None:

                    for k in prof[i][j]:
                        if k in modul2:

                            prof[i][j][k]["COUR"] *= int(modul2[k]["COUR"][0])
                            prof[i][j][k]["TP"] *= int(modul2[k]["TP"][0])
                            prof[i][j][k]["TD"] *= int(modul2[k]["TD"][0])

                elif re.search(r"S[135]", j) != None:
                    for k in prof[i][j]:

                        if k in modul1:

                            prof[i][j][k]["COUR"] *= int(modul1[k]["COUR"][0])
                            prof[i][j][k]["TP"] *= int(modul1[k]["TP"][0])
                            prof[i][j][k]["TD"] *= int(modul1[k]["TD"][0])

        self.__strc = prof

