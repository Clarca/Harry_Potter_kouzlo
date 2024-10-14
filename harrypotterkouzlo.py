kouzlo="Wingardium Leviosa"
print(kouzlo)
kouzla=["Alohomora!" " Wingardium Lewiosa!"  " Lumos!"  " Accio!"]
for kouzlo in kouzla:
    print(kouzlo)

s1="Nox"
s2=s1
s1="Lumox"
print(s1)
print(s2)

print("Zadejte počet svrčků: ")
a = float(input())
galeon=a//493+1
print(f"Ke koupi nového koštěte budete potřebovat {galeon} galeonů." )

print("Zadej počet svrčků:")
cena=float(input())
galeon=cena//493
zbytek=cena-(galeon*493)

srpec=zbytek//29
zbytek=cena-(srpec*29)-(galeon*493)
svrcek=zbytek
print(f"Za koště zaplatíš {galeon} galeonů, {srpec} srpeců a  {svrcek} svrčků.")





