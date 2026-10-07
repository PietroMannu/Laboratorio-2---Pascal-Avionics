

def filtra_per_stato(registro, stato_cercato):
    stato_upper = stato_cercato.upper()
    codici = [k for k, v in registro.items() if v["stato"] == stato_upper]
    return {k: registro[k] for k in codici}

def filtra_per_bus(registro, bus_cercato):
    bus_upper = bus_cercato.upper()
    codici = [k for k, v in registro.items() if v["bus"] == bus_upper]
    return {k: registro[k] for k in codici}