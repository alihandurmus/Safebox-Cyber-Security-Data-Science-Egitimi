

def filmarama():
    isim = input("Arayacağınız film adını giriniz:")
    with open("filmler.txt","r") as f:
        for satir in f:
            bilgiler = satir.split(":")

            ad = bilgiler[0]
            if ad.lower() == isim.lower():
                print("Bulundu")
                print("Film ismi:"+bilgiler[0])
                print("Yapim yili:"+bilgiler[1])
                print("Yonetmen:"+bilgiler[2])
                print("Tur:"+bilgiler[3])
                return 0
        print("Bulunamadı")
        return -1



