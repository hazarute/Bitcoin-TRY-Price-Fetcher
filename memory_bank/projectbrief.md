# Proje Özeti: Bitcoin TRY Price Fetcher

## 1. Ana Hedef
Bu projenin temel amacı, CoinGecko API'sini kullanarak Bitcoin'in (BTC) anlık Türk Lirası (TRY) fiyatını çeken ve sonucu konsola yazdıran basit, tekil bir Python scripti oluşturmaktır.

## 2. Proje Kapsamı
- **Veri Çekme:** CoinGecko'nun "Simple Price" API endpoint'ine bir GET isteği göndererek anlık fiyat verisini almak.
- **Veri İşleme:** Gelen JSON yanıtını ayrıştırarak (parse ederek) içinden Bitcoin'in TRY karşılığını çıkarmak.
- **Sonuç Gösterimi:** Elde edilen fiyat bilgisini, kullanıcı dostu ve okunabilir bir formatta (örn: "Bitcoin Fiyatı: 1,234,567.89 TRY") konsola yazdırmak.
- **Teknoloji:** Proje, standart Python kütüphaneleri ve `requests` paketi dışında ek bir bağımlılık içermeyecektir.
