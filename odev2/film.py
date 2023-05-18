class Film():
    def __init__(self,isim,yil,yonetmen,tur):
        self.isim = isim
        self.yil = yil
        self.yonetmen = yonetmen
        self.tur = tur

def obj():
    isim = input("Film ismi giriniz:")
    yil = input("Yapim yilini giriniz:")
    yonetmen = input("Yonetmen ismini giriniz:")
    tur = input("Film turunu giriniz:")

    film1 = Film(isim, yil, yonetmen, tur)

    return film1
