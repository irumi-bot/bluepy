from bluepy.btle import Scanner, DefaultDelegate
import time

# Ajout de DEMO4 à la fin du dictionnaire
cibles = {
    "mac": "nom"
}

class E(DefaultDelegate):
    def handleDiscovery(self, dev, isNew, isNewD):
        if dev.addr in cibles:
            for (t, d, v) in dev.getScanData():
                if d == "16b Service Data" and v.startswith("ffcb"):
                    try:
                        b, t_val, h = int(v[20:22], 16), int(v[24:28], 16) / 100, int(v[28:32], 16) / 100
                        hr, nom = time.strftime('%H:%M:%S'), cibles[dev.addr]
                        
                        # Affichage classique via print (remplace le logging)
                        print(f"{hr} - {nom} ({dev.addr}) | {t_val} C | {h} % | Bat: {b} %")
                        
                        with open("res.csv", "a") as f: 
                            f.write(f"{hr};{nom};{dev.addr};{t_val};{h};{b}\n")
                    except Exception as err: 
                        # Affichage des erreurs éventuelles sans logging
                        print(f"[{time.strftime('%H:%M:%S')}] Erreur de décodage pour {dev.addr}: {err}")

with open("res.csv", "w") as f: 
    f.write("Heure;Nom;MAC;Temp;Hum;Bat\n")
    
print("Scan continu en cours (Appuyez sur Ctrl+C pour stopper)...")
Scanner().withDelegate(E()).scan(0)
