
def filmsilme():
    isim = input("Sileceğiniz film adını giriniz:")
    with open("filmler.txt","r") as f:
        satirlar = f.readlines()
    with open("filmler.txt","w") as f:
        for satir in satirlar:
            bilgiler = satir.split(":")
            ad = bilgiler[0]
            if ad.lower() != isim.lower():#filmi burada girilen isim ile bulanan isim karşılaştırma ve eğer isim aynı değilse dosyaya yazdırma aynı ise yazdırmama yani silme işlemi.
                f.write(satir)


