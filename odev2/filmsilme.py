
def filmsilme():
    isim = input("Sileceğiniz film adını giriniz:")
    with open("filmler.txt","r") as f:
        satirlar = f.readlines()
    with open("filmler.txt","w") as f:
        for satir in satirlar:
            bilgiler = satir.split(":")
            ad = bilgiler[0]
            if ad.lower() != isim.lower():
                f.write(satir)


