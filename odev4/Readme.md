STORED PROCEDURE VE TRİGGER

Stored procedure ve trigger veri tabanı sistemleriyle etkileşim kurmak için önemli araçlardır. Her ne kadar kullanımları yazılım şekilleri farklı olsa da ikisi de veri tabanı işlemlerini otomatikleştirmeye ve veri bütünlüğünü sağlamaya yardımcı olur.

Stored procedure neden kullanılır çünkü Veritabanı işlemlerinin merkezi bir noktada toplanmasını sağlar. Bir stored procedure, birden fazla SQL sorgusunu içerebilir ve bir seferde çalıştırılabilir. Bu, tekrar eden kod bloklarının tekrar yazılması yerine, kodun bir kez yazılıp gerektiğinde çağrılmasını sağlar.Performans için faydalıdır. Sorguları veri tabanında saklayıp önceden derleyerek zaman tasarrufu sağlar ve ağ trafiğini azaltmak için tek bir çağrı ile birden fazla sorgu yapabilir . Güvenlik için idealdir. Stored procedurler daha karmaşık yapılara olanak sağlar. Mesela döngüler koşullar gibi yapıları destekler. Böylece daha fazla kontrol ve işleyişi daha sağlıklı kontrol edebiliriz.

Stored procedure olumsuz etkileri de vardır tabiki mesela bakımı zordur. Karmaşık yapı desteklediği için bu karmaşıklığı kontrol etmek bakımını yapmak zordur. Hataların bakılıp düzeltilmesi zaman alabilir.

Trigger ise bir nevi veri tabanı olaylarına tepki verir. Bir trigger, belirli bir tabloya veya veritabanı olayına bağlı olarak otomatik olarak tetiklenen bir veritabanı nesnesidir. Örneğin, bir tabloya yeni bir kayıt eklendiğinde veya bir kayıt güncellendiğinde bir trigger çalıştırılabilir. Veri bütünlüğünü sağlar . Triggerlar ayrıca iş kurallarını otomatik olarak uygulamak için kullanılabilir.

Trigger’ın olumsuz etkileri ise karmaşık trigger yapıları kullanıldığında birçok trigger’ın etkileşimi triggerların birbirlerini tetiklemesi sonucu beklenmedik davranışlar ortaya çıkabilir. Yanlış kullanıldığında performans sorunları ortaya çıkar. Yanlış yapılandırılmış kötü niyetli triggerlar güvenlik açıklarına sebep olabilir. 




