from bluepy.btle import Peripheral, BTLEDisconnectError, ADDR_TYPE_RANDOM
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

cibles = {
    "mac":"nom"
}

for mac, nom in cibles.items():
    logging.info(f"Tentative de connexion à {nom} ({mac})...")
    
    try:
        # Ajout de addrType=ADDR_TYPE_RANDOM pour forcer le bon mode
        appareil = Peripheral(mac, addrType=ADDR_TYPE_RANDOM)
        logging.info(f"Connecté à {nom} !")
        
        datas = appareil.getCharacteristics()
        logging.info("Points de données trouvés :")
        
        for data in datas[:5]: 
            logging.info(f" - UUID: {data.uuid} (Propriétés: {data.propertiesToString()})")
            
        appareil.disconnect()
        
    except BTLEDisconnectError:
        logging.warning(f"Impossible de se connecter à {nom} (Bluetooth déconnecté).")
    except Exception as erreur:
        logging.error(f"Erreur inattendue avec {nom} : {erreur}")

logging.info("Fin du test de connexion.")
