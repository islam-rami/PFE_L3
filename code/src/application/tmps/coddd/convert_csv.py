import sys
import json
from convrtir import convertirToCsv

table=sys.argv[1]
list=table.split(",")
conf=list[0]
with open(conf,"r",encoding="utf-8") as fil:
    data = json.load(fil)

path=list[1]
convertirToCsv.convertirToCsv(data["xls_org_s1"],data["sheet_org_s1"],path+"\\org_s1.csv")
convertirToCsv.convertirToCsv(data["xls_org_s2"],data["sheet_org_s2"],path+"\\org_s2.csv")
convertirToCsv.convertirToCsv(data["nbr_s1_xlsx"],data["nbr_s1"],path+"\\nbr_s1.csv")
convertirToCsv.convertirToCsv(data["nbr_s2_xlsx"],data["nbr_s2"],path+"\\nbr_s2.csv")
convertirToCsv.convertirToCsv(data["fich_reliqaut"],data["sheet_reliqaut"],path+"\\reliquat.csv")