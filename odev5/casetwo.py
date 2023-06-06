import pymongo

if __name__ == "__main__":
    connection = pymongo.MongoClient("mongodb+srv://alihandurmus1907:aF2QbJmfM65bZgkW@flaskmongodb.zt7t68i.mongodb.net/")
    db = connection['flaskmongodb']
    UsersCollection = db['Users']
    isim = input("Bir isim belirleyin:")
    #Users collectionında belirlediğiniz isimdeki kişiyi getiren (İsmi Ahmet olanları getir) sorgu
    print("-------------1.SORGU------------------")
    for i in UsersCollection.find({"name":isim}):
        print(i)
    #Users collectionında yaşı 20'den fazla olanları getiren sorgu
    print("-------------2.SORGU------------------")
    for i in UsersCollection.find({"age":{"$gt":20}}):
        print(i)
    #Users collectionında yaşı 25'den fazla olanların description'ı 0 olacak.
    print("-------------3.SORGU------------------")
    for i in UsersCollection.find({"age":{"$gt":25}},{"Description":0}):
        print(i)
    #Users collectionında yaşı 45-48 yaş aralığında olan kişileri silen sorgu
    print("-------------4.SORGU------------------")
    for i in UsersCollection.find({"age":{"$gt":45,"$lt":48}},{"Description":0}):
        UsersCollection.delete_one(i)
        print(f"{i} verisi silindi")

