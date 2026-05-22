from bluepy.btle import Scanner
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

cibles = []

logging.info("Scan en cours...")
appareils = Scanner().scan(10.0)

with open("resultats.csv", "w") as f:
    f.write("Heure;MAC;Signal\n") # En-tête du fichier
    
    for dev in appareils:
        if dev.addr in cibles:
            f.write(f"{time.strftime('%H:%M:%S')};{dev.addr};{dev.rssi}\n")
            logging.info(f"Trouvé : {dev.addr} ({dev.rssi} dBm)")

logging.info("Fini ! Regardez le fichier resultats.csv")
