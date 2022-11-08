import json
import os
import sys
from extraction_information import formProf
from extraction_information import formMoule
import utilisation as ut
from convrtir import convertirToCsv
from extraction_information import mise_a_jour
from calcul_des_heurs_supplimentaires import calcul

table=sys.argv[1]
list=table.split(",")

doc_sortie=list[2]
path_sortir=doc_sortie+"\\calcul.xlsx"
doc_csv=list[1]
path_org1=doc_csv+"\\org_s1.csv"
path_org2=doc_csv+"\\org_s2.csv"
path_nbr_s1=doc_csv+"\\nbr_s1.csv"
path_nbr_s2=doc_csv+"\\nbr_s2.csv"
path_reliquat=doc_csv+"\\reliquat.csv"


z=open(r"C:\Users\DELL_ISLAM\Desktop\sortie_json\ola.txt","w",encoding="utf-8")
z.write(path_org1)
z.close()
#organigram s1
a = convertirToCsv()

#a.csvToList(r"C:\Users\DELL_ISLAM\Desktop\sortie_json\org_s1.csv")
a.csvToList(path_org1)
s1 = ut.transformer(a.get__data())
#print(s1)
#organigram s2
b= convertirToCsv()
#b.csvToList(r"C:\Users\DELL_ISLAM\Desktop\sortie_json\org_s2.csv")
b.csvToList(path_org2)
s2 = ut.transformer(b.get__data())
#print(s2)
#structure prof
prf = formProf()
prf.form_final(s1,s2)
#print(prf.get__structure())
#print("*"*100)


# structure module s1
c = convertirToCsv()
#c.csvToList(r"C:\Users\DELL_ISLAM\Desktop\sortie_json\nbr_s1.csv")
c.csvToList(path_nbr_s1)
module_s1 = ut.transformer(c.get__data())

#print(module_s1)

mdl_1 = formMoule()
mdl_1.form_modul(module_s1)


#structure module s2
d = convertirToCsv()
#d.csvToList(r"C:\Users\DELL_ISLAM\Desktop\sortie_json\nbr_s2.csv")
d.csvToList(path_nbr_s1)
module_s2 = ut.transformer(d.get__data())


mdl_2 = formMoule()
mdl_2.form_modul(module_s2)

#mise à jour
form_prof_apdate = mise_a_jour()
form_prof_apdate.ajouter_nbr_seance(prf.get__structure(),mdl_1.get__structureModule(),mdl_2.get__structureModule())


a = convertirToCsv()
#a.csvToList(r"C:\Users\DELL_ISLAM\Desktop\sortie_json\reliquat.csv")
a.csvToList(path_reliquat)
b = a.get__data()

dd = formProf()
dd.form_reliquat(b)



clc = calcul()
clc.calculate(form_prof_apdate.get__strc(),dd.get__structure(),"fff")

ut.genere_xlsx(clc.get__colonne(),path_sortir)

