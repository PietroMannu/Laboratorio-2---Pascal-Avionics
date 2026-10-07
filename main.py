# main.py

from apparati import APPARATI, aggiungi_apparato, aggiorna_stato
from report import filtra_per_stato, filtra_per_bus
from riepilogo import crea_riepilogo

def mostra_registro(registro):
    print("\n--- REGISTRO APPARATI ---")
    for codice, dati in registro.items():
        print(f"[{codice}] {dati['nome']} | Bus: {dati['bus']} | Stato: {dati['stato']}")

def main():
    print("=== PASCAL AVIONICS ===")
    
    mostra_registro(APPARATI)
    
    # Prova modifica
    aggiungi_apparato(APPARATI, "RAD-04", "Radar altimetro", "BUS-B", "ok")
    aggiorna_stato(APPARATI, "COM-02", "ok")
    
    mostra_registro(APPARATI)
    
    # Report
    print("\nBus A:", list(filtra_per_bus(APPARATI, "BUS-A").keys()))
    print("Stato OK:", list(filtra_per_stato(APPARATI, "OK").keys()))
    
    # Riepilogo
    print("\nRiepilogo:", crea_riepilogo(APPARATI))

if __name__ == "__main__":
    main()