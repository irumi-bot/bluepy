from bluepy.btle import Scanner, DefaultDelegate
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

# Ajout de DEMO4 à la fin du dictionnaire
cibles = {
    "mac":"nom"
}

class E(DefaultDelegate):
    def handleDiscovery(self, dev, isNew, isNewD):
        if dev.addr in cibles:
            for (t, d, v) in dev.getScanData():
                if d == "16b Service Data" and v.startswith("ffcb"):
                    try:
                        b, t_val, h = int(v[20:22],16), int(v[24:28],16)/100, int(v[28:32],16)/100
                        hr, nom = time.strftime('%H:%M:%S'), cibles[dev.addr]
                        
                        # Affichage via logging (l'heure est gérée par le formateur)
                        logging.info(f"{nom} ({dev.addr}) | {t_val} C | {h} % | Bat: {b} %")
                        
                        with open("res.csv", "a") as f: 
                            f.write(f"{hr};{nom};{dev.addr};{t_val};{h};{b}\n")
                    except Exception as err: 
                        logging.debug(f"Erreur de décodage pour {dev.addr}: {err}")

with open("res.csv", "w") as f: 
    f.write("Heure;Nom;MAC;Temp;Hum;Bat\n")
    
logging.info("Scan continu en cours (Appuyez sur Ctrl+C pour stopper)...")
Scanner().withDelegate(E()).scan(0)
