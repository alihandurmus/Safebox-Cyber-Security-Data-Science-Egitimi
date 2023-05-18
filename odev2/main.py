import filmsilme
import filmekleme
import arama
if __name__ == "__main__":
    while(True):
        islem = int(input("(1-Film Ekleme 2-Film arama 3-Film silme 4-Cikis) Islemi seciniz :"))
        if islem == 1:
            filmekleme.ekle()
        elif islem == 2:
            arama.filmarama()
        elif islem == 3:
            filmsilme.filmsilme()
        elif islem == 4:
            print("Cikis Yaptiniz!")
            break
        else:
            print("Yanlıs islem secimi (1,2,3,4)")
