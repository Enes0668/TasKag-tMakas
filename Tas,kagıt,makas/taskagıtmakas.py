import random
rastgele = None

secim = input("tas, kagit, makas ?: ")
sonuc = random.randint(0,2)

if sonuc == 0:
    rastgele = "tas"
if sonuc == 1:
    rastgele = "kagit"
if sonuc == 2:
    rastgele = "makas"

print(f"rakibin {rastgele} secti.")
try:
    if rastgele == secim:
        print("Oyun berabere")
    if rastgele == "tas" and secim == "kagit":
        print("Kazandin")
    if rastgele == "tas" and secim == "makas":
        print("Kaybettin")
    if rastgele == "kagit" and secim == "makas":
        print("Kazandin")
    if rastgele == "kagit" and secim == "tas":
        print("Kaybettin")
    if rastgele == "makas" and secim == "tas":
        print("Kazandin")
    if rastgele == "makas" and secim == "kagit":
        print("Kaybettin")
except:
    print("Geçerli bir ifade girin")
       