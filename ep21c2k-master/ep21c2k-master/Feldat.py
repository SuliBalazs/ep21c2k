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

gyoztes=0
segito=0
pontszam=0
gyoztesindex=0
for line in fileobject:

    #6/7-es feladatokhoz
    if(megoldas[0]==line[0]):
        pontszam=pontszam+3
    if (megoldas[1] == line[1]):
        pontszam = pontszam + 3
    if (megoldas[2] == line[2]):
        pontszam = pontszam + 3
    if (megoldas[3] == line[3]):
        pontszam = pontszam + 3
    if (megoldas[4] == line[4]):
        pontszam = pontszam + 3
        # 4 pont
    if (megoldas[5] == line[5]):
        pontszam = pontszam + 4
    if (megoldas[6] == line[6]):
        pontszam = pontszam + 4
    if (megoldas[7] == line[7]):
        pontszam = pontszam + 4
    if (megoldas[8] == line[8]):
        pontszam = pontszam + 4
    if (megoldas[9] == line[9]):
        pontszam = pontszam + 4
    if (megoldas[10] == line[10]):
        pontszam = pontszam + 4
        #5 pont
    if (megoldas[11] == line[11]):
        pontszam = pontszam + 5
    if (megoldas[12] == line[12]):
        pontszam = pontszam + 5
        # 6
    if (megoldas[13] == line[13]):
        pontszam = pontszam + 5

        if(pontszam>segito):
            gyoztes=pontszam
            gyoztesindex=n




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

    if(megoldas[sorszam]==n[sorszam]):
       jomegold=jomegold+1



print("a helyesen megadott válaszok száma a ",sorszam,". feladatra: ", jomegold)
print("a versenyzők százaléka atlaga: ", atlag,"%")

print("6. feladat")

print("a győztes: ", gyoztesindex,"és a pontszáma:",gyoztes)




fileobject.close()