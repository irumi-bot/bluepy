from bluepy.btle import Scanner
import time

cibles = {
    "mac":"nom"
}

appareils = Scanner().scan(10.0)

with open("resultats.csv", "w") as f:
    f.write("Heure;Nom;MAC;Signal\n")
    
    for dev in appareils:
        mac = dev.addr.lower()
        if mac in cibles:
            f.write(f"{time.strftime('%H:%M:%S')};{cibles[mac]};{mac};{dev.rssi}\n")
            # C'est cette ligne qui a été modifiée pour ajouter la variable {mac} :
            print(f"Trouvé : {cibles[mac]} ({mac}) | Signal : {dev.rssi} dBm")
