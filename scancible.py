from bluepy.btle import Scanner
import time

cibles = ["MAC"]

print("Scan en cours...")
appareils = Scanner().scan(10.0)

with open("resultats.csv", "w") as f:
    f.write("Heure;MAC;Signal\n") # En-tête du fichier
    
    for dev in appareils:
        if dev.addr in cibles:
            f.write(f"{time.strftime('%H:%M:%S')};{dev.addr};{dev.rssi}\n")
            print(f"Trouvé : {dev.addr} ({dev.rssi} dBm)")

print("Fini ! Regardez le fichier resultats.csv")
