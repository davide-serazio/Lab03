from datetime import datetime

from deposito_strumenti import DepositoStrumenti


def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")

    return input("Scegli un'opzione >> ").strip()


def main():
    deposito = DepositoStrumenti(
        "Deposito Strumenti Civico", "Alessandro Visconti"
    )

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            deposito.responsabile = nuovo_responsabile

            print(f"Responsabile aggiornato: {deposito.responsabile}")

        elif scelta == "2":
            file_path = input("Inserisci il percorso del file CSV: ").strip()

            try:
                deposito.carica_file_strumenti(file_path)
                print("Strumenti caricati correttamente.")

            except FileNotFoundError:
                print("Errore: file non trovato.")

            except Exception as errore:
                print(f"Errore durante il caricamento: {errore}")

        elif scelta == "3":
            tipo = input("Tipo di strumento: ")
            marca = input("Marca: ")

            try:
                anno_acquisto = int(input("Anno di acquisto: "))
                valore = float(input("Valore in euro: "))

            except ValueError:
                print("Errore: inserisci un anno intero e un valore numerico.")
                continue

            strumento = deposito.aggiungi_strumento(
                tipo, marca, anno_acquisto, valore
            )

            print(f"Strumento aggiunto: {strumento}")

        elif scelta == "4":
            strumenti = deposito.strumenti_ordinati_per_marca()

            for strumento in strumenti:
                print(strumento)

        elif scelta == "5":
            id_strumento = input("Codice dello strumento: ").strip()
            cognome_allievo = input("Cognome dell'allievo: ")
            data = datetime.now().date()

            try:
                prestito = deposito.nuovo_prestito(
                    data, id_strumento, cognome_allievo
                )

                print(f"Prestito creato: {prestito}")

            except ValueError as errore:
                print(errore)

        elif scelta == "6":
            id_prestito = input("Codice del prestito da terminare: ").strip()

            try:
                deposito.termina_prestito(id_prestito)
                print("Prestito terminato.")

            except ValueError as errore:
                print(errore)

        elif scelta == "7":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida.")


if __name__ == "__main__":
    main()