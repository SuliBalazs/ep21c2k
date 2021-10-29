filepath = "valaszok.txt"
fileobject = open(filepath, "r")
max_length = 0
n = ""
db=0
megoldas = "BCCCDBBBBCDAAA"
elsomegold = "BXCDBBACACADBC"

print("kérem a versenyző kódját: ");
versenykod = input(str())
versenyindex = 0
vane=False
for line in fileobject:
    db=db+1
    if len(line) > max_length:
        n = line
        max_length = len(line)



    if(versenykod==line[0:5]):
            vane=True
            versenyindex = line[6:20]


db=db-1
#[5:20]

print("2. feladat: ")
print("a versenyen ",db,"db versenyző indult")


print("3. feladat: ")

if(vane == True):
    print("van ilyen versenyző, és a kódja: ")
    print(versenyindex)
else:
    print("Ilyen kóddal nem indult versenyző")

print("4. feladat: ")
print("a helyes megoldás: ", megoldas)
if (vane==True):

    if (megoldas[0]==versenyindex[0]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[1]==versenyindex[1]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[2]==versenyindex[2]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[3]==versenyindex[3]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[4]==versenyindex[4]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[5]==versenyindex[5]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[6]==versenyindex[6]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[7]==versenyindex[7]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[8]==versenyindex[8]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[9]==versenyindex[9]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[10]==versenyindex[10]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[11]==versenyindex[11]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[12]==versenyindex[12]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[13]==versenyindex[13]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
else:
    if (megoldas[0] == elsomegold[0]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[1] == elsomegold[1]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[2] == elsomegold[2]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[3] == elsomegold[3]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[4] == elsomegold[4]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[5] == elsomegold[5]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[6] == elsomegold[6]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[7] == elsomegold[7]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[8] == elsomegold[8]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[9] == elsomegold[9]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[10] == elsomegold[10]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[11] == elsomegold[11]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[12] == elsomegold[12]):
        print("+", end=" ")
    else:
        print(" ", end=" ")
    if (megoldas[13] == elsomegold[13]):
        print("+", end=" ")
    else:
        print(" ", end=" ")


print("5. feladat")
print("kérek egy feladat sorszámot : ")
sorszam=int(input())
jomegold=0
atlag=0

atlag=(jomegold/db)*100

for i in range(db):

    if(megoldas[sorszam]==n[sorszam+5]):
       jomegold=jomegold+1



print("a helyesen megadott válaszok száma a ",sorszam,". feladatra: ", jomegold)
print("a versenyzők százaléka atlaga: ", atlag,"%")

print("6. feladat")






fileobject.close()