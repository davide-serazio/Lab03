from csv import reader
from operator import attrgetter

from strumento import Strumento
from prestito import Prestito


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self._strumenti = {}
        self._prestiti = {}
        self._ultimo_id_prestito = 0

    def carica_file_strumenti(self, file_path):
        # Se il file non esiste, open solleva FileNotFoundError.
        with open(file_path, "r", encoding="utf-8") as file:
            for riga in reader(file):
                if len(riga) == 0:
                    continue

                codice = riga[0]
                tipo = riga[1]
                marca = riga[2]
                anno_acquisto = int(riga[3])
                valore = float(riga[4])

                strumento = Strumento(
                    codice, tipo, marca, anno_acquisto, valore
                )

                self._strumenti[codice] = strumento

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        ultimo_numero = 0

        # Si confronta la parte numerica dei codici già presenti.
        for codice in self._strumenti:
            numero = int(codice[1:])

            if numero > ultimo_numero:
                ultimo_numero = numero

        nuovo_codice = f"S{ultimo_numero + 1}"

        strumento = Strumento(
            nuovo_codice, tipo, marca, anno_acquisto, valore
        )

        self._strumenti[nuovo_codice] = strumento
        return strumento

    def strumenti_ordinati_per_marca(self):
        lista_strumenti = []

        for codice in self._strumenti:
            lista_strumenti.append(self._strumenti[codice])

        return sorted(lista_strumenti, key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        if id_strumento not in self._strumenti:
            raise ValueError("Lo strumento non è presente nel deposito.")

        for codice in self._prestiti:
            prestito = self._prestiti[codice]

            if prestito.id_strumento == id_strumento:
                raise ValueError("Lo strumento è già in prestito.")

        self._ultimo_id_prestito += 1
        nuovo_codice = f"P{self._ultimo_id_prestito}"

        prestito = Prestito(
            nuovo_codice, data, id_strumento, cognome_allievo
        )

        self._prestiti[nuovo_codice] = prestito
        return prestito

    def termina_prestito(self, id_prestito):
        if id_prestito not in self._prestiti:
            raise ValueError("Il prestito non esiste.")

        self._prestiti.pop(id_prestito)
