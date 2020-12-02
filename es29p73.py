listacitta=[]
listatmax=[]
listatmin=[]
dacambiare=0
n=0
while True:
    n+=1
    print("Inserisci il nome della città numero", n)
    nomecitta=input()
    listacittà.append(nomecitta)
    print("Inserisci il valore massimo della temperatura giornaliera di", nomecitta)
    vmaxt=int(input())
    listatmax.append(vmaxt)
    print("Digita il valore minimo della temperatura giornaliera di", nomecitta)
    vmint=int(input())
    listatmin.append(vmint)
    fine=input("Inserisci fine se hai finito le città da inserire, inserisci qualsiasi altra cosa per continuare ")
    if fine== "fine":
        break
    else:
        pass

print("Inserisci il valore massimo dell'escursione termica che può accettare il contatore")
escursionemax=int(input())
for i in range(n):
    escursionecittà = listatmax[i]-listatmin[i]
    if escursionemax<escursionecittà:
        dacambiare+=1
        print("I valori delle città che non rientrano nel range del contatore sono:", dacambiare)
    else:
        pass
print("Ora tutti i valori  delle città rientrano nel range del contatore")
