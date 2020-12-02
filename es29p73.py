from random import randint
listacitta=[]
listatempmax=[]
listatempmin=[]
escursionemax=randint(1, 100)
parte1=True
while parte1==True:
    n+=1
    print("Inserisci il nome della città:")
    nomecitta=input()
    listacitta.append(nomecitta)
    print("Inserisci il valore massimo dell'escursione termica di", nomecitta)
    etmax = int(input())
    listatempmax.append(etmax)
    print("Inserisci il valore minimo dell'escursione termica di", nomecitta)
    etmin = int(input())
    listatempmin.append(etmin)
    fermo=input("Se hai terminato le città da inserire, digita stop, altrimenti qualsiasi altro valore: ")
    if fermo=="stop":
        parte1=False
    else:
        pass
parte2=True
while parte2==True:
    print("Scegli un indice presente nelle 3 liste per selezionare una città con la sua escursione termica: ")
    indice=int(input())
    escursionetermica=etmax[indice]-etmin[indice]
    diffescursione=escursionemax-escursionetermica
    print("Valore massimo del contatore: ", escursionemax)
    if diffescursione>0:
        print("L'escursione termica di", listacittà[indice],"è di", escursionetermica,"°. E' compresa nel range che avevamo prefissato per", diffescursione,"°.")
        parte2=False
    else:
        print("L'escursione termica di", città[indice],"è di", escursionetermica,"°. Non è compresa nel range che avevamo prefissato per", diffescursione,"°.")
        parte3=True
        while parte3==True:
            print("Adesso alzerò il range del contatore per far entrare l'escursione termica di", città[indice], "nel range prefissato.")
                diffescursione+=1
                if diffescursione>0:
                    print("Adesso i valori rientrano nel range.")
                        parte1 = False
                        parte2 = False
                        parte3 = False
                else:
                    pass