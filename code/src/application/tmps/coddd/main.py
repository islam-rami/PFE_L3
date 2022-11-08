import json
import os
from extraction_information import formProf
from extraction_information import formMoule
import utilisation as ut
from convrtir import convertirToCsv
from extraction_information import mise_a_jour
from calcul_des_heurs_supplimentaires import calcul


#organigram s1
a = convertirToCsv()
a.convertirToCsv("Organigramme-modifie-2020-2021.xlsx","ORGANIGRAMME_S1",r"org1.csv")
a.csvToList(r"org1.csv")
s1 = ut.transformer(a.get__data())


#organigram s2
a = convertirToCsv()
a.convertirToCsv("Organigramme-modifie-2020-2021.xlsx","ORGANIGRAMME_S2",r"org2.csv")
a.csvToList(r"org2.csv")
s2 = ut.transformer(a.get__data())

#structure prof
prf = formProf()
prf.form_final(s1,s2)

#print(prf.get__structure())

#for i in prf.get__structure():
#    print(i)
 #   print(prf.get__structure()[i])

#structure module s1
c = convertirToCsv()
c.convertirToCsv("Organigramme-modifie-2020-2021.xlsx","NbSeances_S1",r"nbr_modul_s1.csv")
c.csvToList(r"nbr_modul_s1.csv")
module_s1 = ut.transformer(c.get__data())

mdl_1 = formMoule()
mdl_1.form_modul(module_s1)
# print(mdl_1.get__structureModule())

#structure module s2
c = convertirToCsv()
c.convertirToCsv("Organigramme-modifie-2020-2021.xlsx","NbSeances_S2",r"nbr_modul_s2.csv")
c.csvToList(r"nbr_modul_s2.csv")
module_s2 = ut.transformer(c.get__data())

mdl_2 = formMoule()
mdl_2.form_modul(module_s2)
#for i in mdl_2.get__structureModule():
#    print(i)
#    print(mdl_2.get__structureModule()[i])

#print(mdl_2.get__structureModule())

form_prof_apdate = mise_a_jour()
form_prof_apdate.ajouter_nbr_seance(prf.get__structure(),mdl_1.get__structureModule(),mdl_2.get__structureModule())
#for i in form_prof_apdate.get__strc():
#    print(i)
#    print(form_prof_apdate.get__strc()[i])
#print(form_prof_apdate.get__strc())

convertirToCsv.convertirToCsv("result/reliqua.xlsx","Sheet1","reliquat.csv")
a = convertirToCsv()
a.csvToList("reliquat.csv")
b = a.get__data()

dd = formProf()
dd.form_reliquat(b)

#calcul charge horaire et heures supplémentaires


clc = calcul()
clc.calculate(form_prof_apdate.get__strc(),dd.get__structure(),"structue")
for i in clc.get__colonne():
    print(i)
    print("\n")

ut.genere_xlsx(clc.get__colonne(),"prof.xlsx")

