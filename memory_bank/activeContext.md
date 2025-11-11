# Aktif Bağlam (Strateji Defteri)

## 1. Mevcut Çalışma Odağı
**Script Yeniden Kullanılabilir Modül Haline Getirildi:** `btc_price.py` scripti, `get_btc_price()` ve `get_price(coin_id, currency)` fonksiyonları ile başka projelerde kolayca kullanılabilecek modüler bir yapıya dönüştürüldü.

## 2. Aktif Kararlar ve Gerekçeler
- **Karar:** Proje, tek bir Python script dosyası (`btc_price.py`) olarak geliştirilecektir.
  - **Gerekçe:** Projenin eğitim amaçlı ve basit yapısı, karmaşık bir dosya hiyerarşisi veya modüler bir yapı gerektirmiyor. Tek dosya, yeni başlayanlar için takibi en kolay yaklaşımdır.
- **Karar:** Harici bağımlılık olarak yalnızca `requests` kütüphanesi kullanılacaktır.
  - **Gerekçe:** Projenin temel ihtiyacı olan HTTP isteğini bu kütüphane güvenilir bir şekilde karşılamaktadır. Ek bağımlılıklar eklemek, projenin basitlik hedefine aykırı olacaktır.
- **Karar:** `btc_price.py` scripti, `get_btc_price()` ve `get_price(coin_id, currency)` fonksiyonları ile yeniden kullanılabilir bir modül haline getirildi.
  - **Gerekçe:** Bu, script'in Botpress gibi başka projelerde veya farklı kripto para birimleri için kolayca entegre edilmesini ve kullanılmasını sağlar, böylece kod tekrarını önler ve esnekliği artırır.

## 3. Öğrenilenler ve İçgörüler
- Proje henüz başlamadığı için bu aşamada kaydedilmiş bir içgörü bulunmamaktadır.

## 4. Stratejik Sonraki Yön
Modüler yapı sayesinde, gelecekte farklı API entegrasyonları veya ek özellikler (örn: geçmiş fiyat verileri, grafikler) kolayca eklenebilir. Script, Botpress gibi platformlarda bir eklenti olarak kullanılmaya hazırdır.
