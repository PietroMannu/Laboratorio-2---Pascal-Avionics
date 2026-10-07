# riepilogo.py

from apparati import STATI_AMMESSI

def crea_riepilogo(registro):
    riepilogo = {"TOTALE": len(registro)}
    for stato in STATI_AMMESSI:
        riepilogo[stato] = sum(1 for v in registro.values() if v["stato"] == stato)
    return riepilogo