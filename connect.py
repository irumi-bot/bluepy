from bluepy.btle import Peripheral, BTLEDisconnectError, ADDR_TYPE_RANDOM

cibles = {
    "mac":"nom"
}

for mac, nom in cibles.items():
    print(f"\nTentative de connexion à {nom} ({mac})...")
    
    try:
        # Ajout de addrType=ADDR_TYPE_RANDOM pour forcer le bon mode
        appareil = Peripheral(mac, addrType=ADDR_TYPE_RANDOM)
        print(f"Connecté à {nom} !")
        
        datas = appareil.getCharacteristics()
        print("Points de données trouvés :")
        
        for data in datas[:5]: 
            print(f" - UUID: {data.uuid} (Propriétés: {data.propertiesToString()})")
            
        appareil.disconnect()
        
    except BTLEDisconnectError:
        print(f"Impossible de se connecter à {nom}.")
    except Exception as erreur:
        print(f"Erreur inattendue avec {nom} : {erreur}")

print("\nFin du test de connexion.")
