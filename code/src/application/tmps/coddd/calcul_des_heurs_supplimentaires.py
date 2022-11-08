import config as cnf
class calcul:

    def __init__(self):
        self.__colonne = None

    def get__colonne(self):
        return self.__colonne



    def calculate (self,form_prof,form_reliquat,configuration):
        list_heure_supp = []
        for enseignant in form_prof.keys():
            struct_heures_supp = {}
            struct_heures_supp["ENSEIGNANT"]=enseignant
            struct_enseignant = form_prof[enseignant]  # récupere les valeurs de la structure enseignant
            for config in cnf.heures_sup_config.keys():
                config_function = cnf.heures_sup_config[config]
                struct_heures_supp[config] = config_function(struct_enseignant, struct_heures_supp,form_reliquat,configuration)
            list_heure_supp.append(struct_heures_supp)
        self.__colonne=list_heure_supp











