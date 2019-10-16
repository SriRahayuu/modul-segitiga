import segitigaSamaSisi

def main():
    #Keliling segitiga
    s = 6

    keliling = segitigaSamaSisi.kelilingSegitigaSamaSisi(s)

    print("KELILING SEGITIGA")
    print("sisi\t: ", s)
    print("keliling\t: ", keliling)

    #luas segitiga
    a = 4
    t = 8

    luas = segitigaSamaSisi.luasSegitigaSamaSisi(a, t)

    print("\nLUAS SEGITIGA")
    print("alas\t: ", a)
    print("tinggi\t: ", t)
    print("luas\t: ", luas)

    #tinggi segitiga
    a = 4
    l = 10

    tinggi = segitigaSamaSisi.tinggiSegitigaSamaSisi(l, a)

    print("\nTINGGI SEGITIGA")
    print("alas\t: ", a)
    print("tinggi\t: ", t)
    print("luas\t: ", luas)

if __name__ == "__main__":
    main()
