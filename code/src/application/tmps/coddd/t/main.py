import json
import os
from extraction_information import formProf
from extraction_information import formMoule
import utilisation as ut
from convrtir import convertirToCsv
from extraction_information import mise_a_jour
from calcul_des_heurs_supplimentaires import calcul

with open(r"configuration//config.json","r",encoding="utf-8") as fil:
    data = json.load(fil)
path = r"csv2"
if not os.path.exists(path):
    os.mkdir(r"csv2")

#organigram s1
a = convertirToCsv()
a.convertirToCsv(data["xlsx"],data["sheet_org_s1"],r"csv2\org1.csv")
a.csvToList(r"csv2\org1.csv")
s1 = ut.transformer(a.get__data())
#print(s1)
#organigram s2
b= convertirToCsv()
b.convertirToCsv(data["xlsx"],data["sheet_org_s2"],r"csv2\org2.csv")
b.csvToList(r"csv2\org2.csv")
s2 = ut.transformer(b.get__data())
#print(s2)
#structure prof
prf = formProf()
prf.form_final(s1,s2)
#print(prf.get__structure())
#print("*"*100)


#structure module s1
c = convertirToCsv()
c.convertirToCsv(data["xlsx"],data["nbr_s1"],r"csv2\nbr_modul_s1.csv")
c.csvToList(r"csv2\nbr_modul_s1.csv")
module_s1 = ut.transformer(c.get__data())

#print(module_s1)

mdl_1 = formMoule()
mdl_1.form_modul(module_s1)
#print("\n "*300)
#print("modulllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
#print(mdl_1.get__structureModule())


#structure module s2
d = convertirToCsv()
d.convertirToCsv(data["xlsx"],data["nbr_s2"],r"csv2\nbr_modul_s2.csv")
d.csvToList(r"csv2\nbr_modul_s2.csv")
module_s2 = ut.transformer(d.get__data())
#print(module_s2)

mdl_2 = formMoule()
mdl_2.form_modul(module_s2)
#print(mdl_2.get__structureModule())

#print("*"*100)

#mise à jour
form_prof_apdate = mise_a_jour()
form_prof_apdate.ajouter_nbr_seance(prf.get__structure(),mdl_1.get__structureModule(),mdl_2.get__structureModule())
#print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
#print(form_prof_apdate.get__strc())
#for i in form_prof_apdate.get__strc():
#    print(i)
#    print(form_prof_apdate.get__strc()[i])
#print("\n"*1)
#print("*"*100)

convertirToCsv.convertirToCsv("result/reliqua.xlsx","Sheet1","reliquat.csv")
a = convertirToCsv()
a.csvToList("reliquat.csv")
b = a.get__data()

dd = formProf()
dd.form_reliquat(b)
print("dd =")
print(dd.get__structure())



#calcul charge horaire
clc = calcul()
clc.calculate(form_prof_apdate.get__strc(),dd.get__structure(),"fff")
for i in clc.get__colonne():
    print(i)


ut.genere_xlsx(clc.get__colonne(),"prof.xlsx")



