import pandas as pd
import csv


class convertirToCsv:
    def __init__(self):
        self.__data = None

# convertir fichier xlsx en csv
    @staticmethod
    def convertirToCsv(file_xlsx,partie,file_csv):
        read_file = pd.read_excel(file_xlsx,sheet_name=partie)
        read_file.to_csv(file_csv,index= None, header= True)

#fonction qui tronsforme un fichier csv en un liste ou chaque ligne de csv est une liste

    def csvToList(self,file, sep=","):
        f = open(file, 'r',encoding="utf-8")
        r = csv.reader(f, delimiter=sep)

        lignes = list(r)

        f.close()
        self.__data = lignes

    def get__data(self):
        return self.__data
