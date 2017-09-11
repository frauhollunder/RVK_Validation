# -*- coding: utf-8 -*-

import requests
import json
rvk = open("rvk-in-SISIS-Feld1701.txt","r")
rvk_Ergebnis = open("RVK-Notation.txt","w+")
rvk_Fehler = open("RVK-Fehler.txt","w+")
zahl = 0
for line in rvk:
    line = line.decode(encoding='ascii',errors='replace').encode('ascii','replace')
    print((line))
    zahl = zahl+1
    line = line.replace("\n","")
    line = line.replace("\r","")
    line2 = line
    line = line.replace(" ","+")

    success = False
    while success == False:
        try:
            Ergebnis = requests.get("https://rvk.uni-regensburg.de/apitest/json/ancestors/"+line)
            success = True
        except:
            success = False
    
    
    Ergebnis_json = json.loads(Ergebnis.text)
    if not Ergebnis_json.has_key("error-message"):
        print(str(zahl)+" "+line2)
        rvk_Ergebnis.write(str(zahl)+";"+line2+"\r\n")
        rvk_Ergebnis.flush()
    else:
        Fehlermeldung = Ergebnis_json["error-message"]
        Fehlermeldung = Fehlermeldung.replace("\n","")
        Fehlermeldung = Fehlermeldung.replace("\r","") 
        print(str(zahl)+" "+line2)
        rvk_Fehler.write(str(zahl)+";"+line2+";"+Fehlermeldung+"\r\n")
        rvk_Fehler.flush()
rvk.close()
rvk_Ergebnis.close()
rvk_Fehler.close()
#https://rvk.uni-regensburg.de/apitest/json/ancestors/
