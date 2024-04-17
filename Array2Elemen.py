print("Diberikan {a,b ∈ Z|1 ≤ a,b ≤ 9}")
nA = int(input("Banyak elemen A: "))
A = []
for i in range(nA):
    elemen = int(input(f"Elemen ke-{i + 1} : "))
    if 0 <= elemen <= 9:
        A.append(elemen)
    else:
        print("Elemen harus berupa bilangan bulat antara 0 dan 9!")
        break
print()

nB = int(input("Banyak elemen B: "))
B = []
for i in range(nB):
    elemen = int(input(f"Elemen ke-{i + 1}  : "))
    if 0 <= elemen <= 9:
        B.append(elemen)
    else:
        print("Elemen harus berupa bilangan bulat antara 0 dan 9!")
        break

Elemen_khususA = list(set(A) - set(B))
Elemen_khususB = list(set(B) - set(A))
Elemen_AdanB = list(set(A) & set(B))

print()
print("A\B = ", Elemen_khususA)
print("B\A = ", Elemen_khususB)
print("A∩B = ", Elemen_AdanB)
