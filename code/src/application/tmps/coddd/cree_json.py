import sys
import json

table=sys.argv[1]
list=table.split(",")

dic={

    "xls_org_s1":list[0],
    "sheet_org_s1":list[1],
    "xls_org_s2": list[2],
	"sheet_org_s2":list[3],
    "nbr_s1_xlsx": list[4],
    "nbr_s1": list[5],
    "nbr_s2_xlsx": list[6],
    "nbr_s2": list[7],
    "sortie_json":list[8],
    "charge_max":int(list[9]),
    "heur_supp_max":int(list[10]),
    "S1_moi1":int(list[11]),
    "S1_moi2":int(list[12]),
    "S1_moi3":int(list[13]),
    "S1_moi4":int(list[14]),
    "S1_moi5":int(list[15]),
    "S1_moi6":int(list[16]),
    "S2_moi1":int(list[17]),
    "S2_moi2":int(list[18]),
    "S2_moi3":int(list[19]),
    "S2_moi4":int(list[20]),
    "S2_moi5":int(list[21]),
    "S2_moi6":int(list[22]),
    "fich_reliqaut":list[23],
    "sheet_reliqaut":list[24]
}
path=dic["sortie_json"]
out_put=json.dumps(dic,indent=2)
with open(path+"/sor.json","w",encoding="utf-8") as fil:

    json.dump(dic,fil,indent=2)

fil.close()