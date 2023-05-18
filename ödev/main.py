def kullanici_kayit():
    kullanici_bilgi = {}
    kullanici_adi = input("Kullanıcı adını girin: ")
    kullanici_sifre = input("Kullanıcı şifresini girin: ")

    kullanici_bilgi["kullanici_adi"] = kullanici_adi
    kullanici_bilgi["kullanici_sifre"] = kullanici_sifre

    with open("kullanici_bilgileri.txt", "a") as f:
        f.write(kullanici_bilgi["kullanici_adi"] + "," + kullanici_bilgi["kullanici_sifre"] + "\n")
    print("Kullanıcı kaydedildi.")

def giris(kullanici_adi, kullanici_sifre):
    with open("kullanici_bilgileri.txt", "r") as f:
        for satir in f.readlines():
            kayit = satir.strip().split(",")
            if kullanici_adi == kayit[0] and kullanici_sifre == kayit[1]:
                print("Giriş başarılı!")
                return

    print("Hatalı kullanıcı adı veya şifre!")

while True:
    secim = input("1-Kayıt 2-Giriş 3-Çıkış: ")

    if secim == "1":
        kullanici_kayit()
    elif secim == "2":
        kullanici_adi = input("Kullanıcı Adı: ")
        kullanici_sifre = input("Şifre: ")
        giris(kullanici_adi, kullanici_sifre)
    elif secim == "3":
        print("Çıkış başarılı")
        break
    else:
        print("Yanlış seçim yaptınız!")