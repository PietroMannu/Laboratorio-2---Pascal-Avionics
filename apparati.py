# apparati.py

STATI_AMMESSI = ["OK", "ATTENZIONE", "OFFLINE"]

APPARATI = {
    "NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
    "COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
    "SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}

def aggiungi_apparato(registro, codice, nome, bus, stato):
    if codice in registro:
        print(f"Errore: Codice '{codice}' già presente.")
        return False
    if stato not in STATI_AMMESSI:
        print(f"Errore: Stato '{stato}' non valido.")
        return False
    
    registro[codice] = {"nome": nome, "bus": bus, "stato": stato}
    return True

def aggiorna_stato(registro, codice, nuovo_stato):
    if codice not in registro:
        print(f"Errore: Apparato '{codice}' non trovato.")
        return False
    if nuovo_stato not in STATI_AMMESSI:
        print(f"Errore: Stato '{nuovo_stato}' non valido.")
        return False
    
    registro[codice]["stato"] = nuovo_stato
    return True