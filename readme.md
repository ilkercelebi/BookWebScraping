Kitap Web Scraping Projemde
https://books.toscrape.com/ adresindeki kitapları tarayarak kitap detaylarını toplar. Kullanıcıların Travel ve Nonfiction kategorilerindeki kitap bilgilerini elde etmelerini sağlar. Toplanan veriler bir pandas DataFrame'e dönüştürülür.

Özellikler
Kategorilere göre kitapların URL'lerini bulur.
Her kitabın detaylarını toplar (fiyat, ad, yıldız derecesi, açıklama).
Verileri bir pandas DataFrame'e dönüştürür.
Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki kütüphaneleri kurmanız gerekir:

selenium
pandas
chromedriver (Google Chrome için)
Gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

bash
Kodu kopyala
pip install selenium pandas
Ayrıca, ChromeDriver'ı indirip kurmanız gerekiyor. ChromeDriver İndir

Kullanım
Kodun Çalıştırılması

Kodu çalıştırmak için Python betiğini (project.py gibi) çalıştırın. Kod, Travel ve Nonfiction kategorilerindeki kitapları tarar, her kitap için detayları toplar ve verileri bir pandas DataFrame olarak yazdırır.
python project.py

Kod Açıklaması

find_category_urls(driver, category_url, is_nonfiction): Verilen kategori URL'sindeki kitapların URL'lerini toplar. Eğer kategori "Nonfiction" ise, sayfalandırmayı da yönetir.
product_details(link): Verilen kitap URL'sinden kitap detaylarını (fiyat, ad, yıldız derecesi, açıklama) toplar.
convert_to_df(books_details): Toplanan kitap detaylarını pandas DataFrame'e dönüştürür ve ekrana yazdırır.
XPaths ve Elemanlar

Fiyat: //p[@class="price_color"]
Kitap Adı: //h1
Yıldız Derecesi: //p[contains(@class, "star-rating")]
Açıklama: //*[@id="content_inner"]/article/p
Notlar
Kodun doğru çalışabilmesi için ChromeDriver'ın sistem PATH'inde olması veya webdriver.Chrome() ile doğru yolu belirlemeniz gerekir.
Tarayıcı ve ChromeDriver versiyonlarının uyumlu olması önemlidir.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için Lisans dosyasına bakabilirsiniz.
