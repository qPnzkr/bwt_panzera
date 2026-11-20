# bwt panzera
## Trasformata di Burrows-Wheeler (BWT)
La BWT e' un algoritmo che permette di cambiare l'ordine dei caratteri di una parola.

Il programma funziona in questo modo:

Prende una parola inserita dall'utente.
Aggiunge il simbolo $ alla fine.
Crea tutte le possibili rotazioni della parola.
Ordina tutte le righe in ordine alfabetico.
Prende l'ultimo carattere di ogni riga.
Unisce tutti i caratteri e ottiene la trasformata finale.
Esempio
Parola inserita:

banana

Risultato:

annb$aa

Scopo del progetto
Lo scopo e' creare un programma in Python che calcola la BWT. Inoltre, il progetto permette di inviare una parola da un client a un server tramite socket TCP. Il server calcola la trasformata e restituisce il risultato al client.



