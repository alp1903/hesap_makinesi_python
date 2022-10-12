from time import sleep
from os import system

while (True):
    print(30*"-")
    print(" __    __                                                __       __            __        __                               ")
    print("|  \  |  \                                              |  \     /  \          |  \      |  \                              ")
    print("| $$  | $$  ______    _______   ______    ______        | $$\   /  $$  ______  | $$   __  \$$ _______    ______    _______ ")
    print("| $$__| $$ /      \  /       \ |      \  /      \       | $$$\ /  $$$ |      \ | $$  /  \|  \|       \  |      \  /       \ ")
    print("| $$    $$|  $$$$$$\|  $$$$$$$  \$$$$$$\|  $$$$$$\      | $$$$\  $$$$  \$$$$$$\| $$_/  $$| $$| $$$$$$$\  \$$$$$$\|  $$$$$$$")
    print("| $$$$$$$$| $$    $$ \$$    \  /      $$| $$  | $$      | $$\$$ $$ $$ /      $$| $$   $$ | $$| $$  | $$ /      $$ \$$    \ ")
    print("| $$  | $$| $$$$$$$$ _\$$$$$$\|  $$$$$$$| $$__/ $$      | $$ \$$$| $$|  $$$$$$$| $$$$$$\ | $$| $$  | $$|  $$$$$$$ _\$$$$$$\ ")
    print("| $$  | $$ \$$     \|       $$ \$$    $$| $$    $$      | $$  \$ | $$ \$$    $$| $$  \$$\| $$| $$  | $$ \$$    $$|       $$")
    print(" \$$   \$$  \$$$$$$$ \$$$$$$$   \$$$$$$$| $$$$$$$        \$$      \$$  \$$$$$$$ \$$   \$$ \$$ \$$   \$$  \$$$$$$$ \$$$$$$$ ")
    print("                                        | $$                                                                               ")
    print("                                        | $$                                                                               ")
    print("                                         \$$                                                                               ")

    print(30*"-")
    print("(0) Çık")
    print("(1) Topla\n(2) Çıkar\n(3) Çarpma\n(4) Bölme ")
    print(30*"-")

    islem = int(input("Seçnek Nedir: "))

    if (islem == 0):
        break

    elif (islem == 1):
        sayi1 = int(input("1. Sayıyı Gir: "))
        sayi2 = int(input("2. Sayıyı Gir: "))
        sonuc = sayi1 + sayi2

        print(30 * "-")
        print("Toplam: ", str(sonuc))
        print(30 * "-")
        sleep(2)
        system("cls")

    elif (islem == 2):
        sayi1 = int(input("1. Sayıyı Gir: "))
        sayi2 = int(input("2. Sayıyı Gir: "))
        sonuc = sayi1 - sayi2

        print(30 * "-")
        print("Çıkan: ", str(sonuc))
        print(30 * "-")
        sleep(2)
        system("cls")

    elif (islem == 3):
        sayi1 = int(input("1. Sayıyı Gir: "))
        sayi2 = int(input("2. Sayıyı Gir: "))
        sonuc = sayi1 * sayi2

        print(30 * "-")
        print("Çarpan: ", str(sonuc))
        print(30 * "-")
        sleep(2)
        system("cls")

    elif (islem == 4):
        sayi1 = int(input("1. Sayıyı Gir: "))
        sayi2 = int(input("2. Sayıyı Gir: "))
        sonuc = sayi1 / sayi2

        print(30 * "-")
        print("Bölünen: ", str(sonuc))
        print(30 * "-")
        sleep(2)
        system("cls")

    else:
        print("\nLütfen yukarıdaki değerlerden birini giriniz...")
        sleep(2)
        system("cls")
