listanomi=[]
listalanci=[]
print("Per fermare il programma inserire stop")
while True:
    print("Inserisci il nome dello studente: ")
    nome=input()
    if nome=="stop":
        break
    else:
        listanomi.append(nome)
        lancio=int(input("Inserisci il valore in metri del lancio: "))
        listalanci.append(lancio)
massimo=max(listalanci)
print(massimo)
