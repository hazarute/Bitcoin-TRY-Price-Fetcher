# Teknik Detaylar ve Kurulum

## 1. Teknolojiler ve Sürümler
- **Programlama Dili:** Python (Sürüm 3.6 veya üzeri)
- **Kütüphaneler:**
  - `requests`: Harici API'lere HTTP istekleri yapmak için kullanılır.

## 2. Geliştirme Ortamı Kurulumu
1.  **Python Yüklü Olmalı:** Sisteminize Python 3.6 veya daha yeni bir sürümün yüklü olduğundan emin olun. Terminalde `python --version` veya `python3 --version` komutu ile kontrol edebilirsiniz.
2.  **Bağımlılıkların Yüklenmesi:** Projenin çalışması için gerekli olan `requests` kütüphanesini `pip` (Python paket yöneticisi) kullanarak yükleyin:
    ```bash
    pip install requests
    ```

## 3. API Referansı
- **Kullanılan API:** CoinGecko Simple Price API
- **API Endpoint:**
  ```
  https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=try
  ```
- **Metot:** `GET`

## 4. Proje Çalıştırma
Proje dosyalarının bulunduğu dizine terminal üzerinden gidin ve aşağıdaki komutu çalıştırın:
```bash
python btc_price.py
```

## 5. Lisans
Bu proje **MIT Lisansı** altında lisanslanmıştır.
