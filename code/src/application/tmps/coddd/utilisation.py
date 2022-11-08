
import xlsxwriter
import os
# fonction qui prend e entrée le premier element de la liste (header de fichier xlxs) et  rond un dic {clé: valeur}  la clé: valeurs de header
def construireLIne(header, list):
    dic = {}

    for i in range(len(list)):

        dic[header[i]] = list[i]
    return dic

#retourne une liste des dictionnaires précédents
def transformer(list):
    list_final=[]
    for i in range(1,len(list)):
        if list[i][0] !='':
            d = construireLIne(list[0], list[i])
            list_final.append(d)

    return list_final



def genere_xlsx(list,name):

    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()
    i = 0
    for j in list[0]:
        worksheet.write(0, i, j)
        i = i + 1

    for i in range(len(list)):
        k = 0
        for j in list[i]:
            worksheet.write(i + 1, k, list[i][j])
            k = k + 1
    workbook.close()
