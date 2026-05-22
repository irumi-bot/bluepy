from bluepy.btle import Scanner
import time

print("Recherche en cours (5 secondes)...")

# 1. On scanne directement
appareils = Scanner().scan(5.0)

# 2. On ouvre un fichier (il sera créé ou écrasé à chaque scan)
with open("resultats.csv", "w") as fichier:
    fichier.write("Heure;Adresse MAC;Signal\n") # L'en-tête
    
    # 3. On note chaque appareil trouvé
    for dev in appareils:
        heure = time.strftime("%H:%M:%S")
        fichier.write(f"{heure};{dev.addr};{dev.rssi}\n")
        print(f"Détecté : {dev.addr}")

print("\nFini ! Les résultats sont dans le fichier 'resultats.csv'.")
