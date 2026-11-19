
def BWT(parola):

    arrParola = list(parola)
    arrFinale = []

    arrParola.append("$")

    for i in range(0, len(arrParola)):

        arrFinale.append(arrParola.copy())

        arrParola.append(arrParola[0])
        arrParola.pop(0)

    arrFinale.sort()

    print("Matrice ordinata:")

    for riga in arrFinale:
        print(riga)

    lunghezza = len(arrParola) - 1

    trasformata = ""

    for i in range(0, len(arrFinale)):

        trasformata = trasformata + arrFinale[i][lunghezza]

    return trasformata


if __name__ == "__main__":

    parola = input("Dimmi la parola di cui vuoi sapere la trasformata di Burrows Wheeler: ")

    risultato = BWT(parola)

    print("La trasformata è:", risultato)
