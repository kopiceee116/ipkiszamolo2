ip = input("?.?.?.?\n")
maszk = input("/?\n")

def ipdolgok(ip :str,maszk:str):
    megoldas,osszesen,kiirosmaszk,felosztottmaszk = [],[],[],[]
    felosztva = ip.split(".")
    binmaszk = "1"*int(maszk)+((32-int(maszk))*"0")
    pontbinmaszk = [binmaszk[0:8],binmaszk[8:16],binmaszk[16:24],binmaszk[24:32]]

    for i in pontbinmaszk:
        felosztottmaszk.append(int(i,2))
        kiirosmaszk.append(f"{int(i,2)}")
    mekkora = [255-felosztottmaszk[0],255-felosztottmaszk[1],255-felosztottmaszk[2],255-felosztottmaszk[3],]

    for i in felosztva:
        osszesen.append(int(i))

    for i in range(0,4):
        megoldas.append(osszesen[i]+mekkora[i])
    osszesen[3]+=1
    megoldas[3]-=1
    elsokiadhato,megoldasfinal = [],[]
    for i in range(4):
        elsokiadhato.append(str(osszesen[i]))
        megoldasfinal.append(str(megoldas[i]))
    
    return ['.'.join(elsokiadhato),".".join(kiirosmaszk),".".join(megoldasfinal)]

print("\n\n\n\n\n\n\n")
ipadatok = ipdolgok(ip,maszk)
print(f"hálózati cím: {ip}")
print(f"első kiadható cím: {ipadatok[0]}")
print(f"maszk: {ipadatok[1]}")
print(f"utolsó kiadható cím: {ipadatok[2]}")