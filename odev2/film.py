class Film():#film sınıfı oluşturma
    def __init__(self,isim,yil,yonetmen,tur):
        self.isim = isim#özelliklerini belirleme
        self.yil = yil
        self.yonetmen = yonetmen
        self.tur = tur

def obj():#film sınıfı için nesne oluşturma fonskiyonu
    isim = input("Film ismi giriniz:")#özellikleri için kullanıcıdan değer alma
    yil = input("Yapim yilini giriniz:")
    yonetmen = input("Yonetmen ismini giriniz:")
    tur = input("Film turunu giriniz:")

    film1 = Film(isim, yil, yonetmen, tur)#film sınıfı için nesne oluşturma kısmı

    return film1
