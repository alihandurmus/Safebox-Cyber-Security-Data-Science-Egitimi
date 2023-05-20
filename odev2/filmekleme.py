import film

def ekle(film=film):
    film1 = film.obj()

    with open("filmler.txt","a") as f:
        f.write(film1.isim+":"+film1.yil+":"+film1.yonetmen+":"+film1.tur + "\n")#filmi burada dosyaya ekleme.
    print("Film eklendi")
