import json
def fich():
    with open(r"configuration//test_extraction_information.json", "r",) as fil:
        #ata = json.load(fil)
        try:
            return json.load(fil)
        except ValueError as e:
            print("invalid json: "+  e)
            return None  # or: raise





a=fich()