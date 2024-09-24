# author                 :fathulkhair

# 1. Variabel Declaration

Variabel1 = 10
Variabel2 = 10.5
Variabel3 = "sepuluh"
Variabel4 = True

#2. Operatian ->  +, -, /, %,



# 3. perulangan -> Loopig
# for statement
# index data -> dimulai 0

for baris in range(5):
    for kolom in range(5):
        print("*",end="")
    print()

print("==============")

# while interation -> Need 
baris2 = 0
tengah = 5
while baris2 < 5 :
    kolom2 = 0
    if(baris2 % 2 == 1):
        while kolom2 < 5:
            if(kolom2 == int(round(tengah/2))):
                print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5 :
            print("*",end="")
            kolom2 +=1
    print()
    baris2 += 1