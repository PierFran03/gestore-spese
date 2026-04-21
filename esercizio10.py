class Transazione:
    def __init__(self, tipo, descrizione, importo):
        self.tipo = tipo
        self.descrizione = descrizione
        self.importo = importo

    def mostra(self):
        return f"{self.tipo} - {self.descrizione}: {self.importo}"
    


def aggiungi_transazione():
    tipo = input("Che tipo di transazione (entrata o uscita) devi effettuare? ")
    descrizione = input("Descrivi la transazione che vuoi effettuare: ")
    importo = float(input("Inserisci l'importo della transazione: "))

    pagamento = Transazione(tipo, descrizione, importo)

    with open ("transazione.txt", "a") as f:
        f.write(f"{pagamento.tipo},{pagamento.descrizione},{pagamento.importo}\n")


def visualizza_transazioni():
    try:
        with open("transazione.txt", "r") as f:
            for riga in f:
                valori = riga.strip().split(",")
                transazione = Transazione(valori[0], valori[1], valori[2])
                print(transazione.mostra())

    except FileNotFoundError:
        print("Nessun file trovato!")

def visualizza_saldo():
    saldo = 0
    try:
        with open ("transazione.txt", "r") as f:
            for riga in f:
                valori = riga.strip().split(",")
                transazione = Transazione(valori[0], valori[1], valori[2])
                importo = float(valori[2])

                if valori[0] == "entrata":
                    saldo += importo
                elif valori[0] == "uscita":
                    saldo -= importo
        
        print(f"Saldo attuale: {saldo}€")

    except FileNotFoundError:
        print("Nessuna transazione trovata!")

def visualizza_statistiche():
    totale_entrate = 0
    totale_uscite = 0

    try:
        with open("transazione.txt", "r") as f:
            for riga in f:
                valori = riga.strip().split(",")
                transazione = Transazione(valori[0], valori[1], valori[2])
                importo = float(valori[2])

                if valori[0] == "entrata":
                    totale_entrate += importo

                elif valori[0] == "uscita":
                    totale_uscite += importo
        
        print(f"Totale entrate: {totale_entrate}€")
        print(f"Totale uscite: {totale_uscite}€")

    except FileNotFoundError:
        print("Nessuna transazione trovata!")                      

        

while True:
    print("1 - Aggiungi transazione")
    print("2 - Visualizza saldo")
    print("3 - Visualizza statistiche")
    print("4 - Visualizza transazioni")
    print("5 - Esci")

    scelta = input("Cosa vuoi fare?")

    if scelta == "1":
        aggiungi_transazione()
    elif scelta == "2":
        visualizza_saldo()
    elif scelta == "3":
        visualizza_statistiche()
    elif scelta == "4":
        visualizza_transazioni()
    else:
        break