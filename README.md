# Bitcoin TRY Price Fetcher

Bu proje, [CoinGecko API](https://www.coingecko.com/en/api)'sini kullanarak Bitcoin'in anlık Türk Lirası (TRY) cinsinden fiyatını çeken basit bir Python scriptidir.

This project is a simple Python script that fetches the current price of Bitcoin in Turkish Lira (TRY) using the [CoinGecko API](https://www.coingecko.com/en/api).

---

##  Türkçe (Turkish)

### Proje Açıklaması
Bu proje, CoinGecko'nun ücretsiz API'sine basit bir istek atarak kripto para piyasasındaki en popüler varlık olan Bitcoin'in (BTC) Türkiye'deki güncel fiyatını konsola yazdıran temel bir otomasyon scriptidir. Proje, API kullanımı, HTTP istekleri ve JSON veri işleme gibi temel Python becerilerini göstermektedir.

### Teknolojiler
- Python
- Requests Kütüphanesi

### Temel Özellikler
- CoinGecko API'sine `requests` kütüphanesi ile bağlanır.
- Bitcoin'in (BTC) Türk Lirası (TRY) karşılığındaki anlık fiyatını getirir.
- Sonucu kullanıcı dostu bir formatta (örn: "Bitcoin Fiyatı: 1,234,567.89 TRY") konsola yazdırır.

### Kurulum ve Çalıştırma
1.  **Python Kurulumu**: Sisteminizde Python (3.6 veya üzeri) yüklü olduğundan emin olun.
2.  **Kütüphane Kurulumu**: Gerekli `requests` kütüphanesini yükleyin.
    ```bash
    pip install requests
    ```
3.  **Proje Dosyası**: Proje dosyasını (`btc_price.py`) bir dizine kaydedin.
4.  **Çalıştırma**: Terminali/komut istemini açıp ilgili dizine gidin ve scripti çalıştırın.
    ```bash
    python btc_price.py
    ```

### Kod Örneği
Script, belirtilen API endpoint'ine bir GET isteği atar, gelen JSON yanıtını ayrıştırır ve içinden fiyat bilgisini çekerek ekrana yazdırır.

### API Referansı
- **Kullanılan API**: CoinGecko Simple Price API
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=try`

### Notlar ve Uyarılar
- Bu proje eğitim amaçlıdır. Ticari kullanım için CoinGecko'nun API kullanım koşullarını kontrol ediniz.
- API'nin rate limit (istek sınırı) olabilir, lütfen buna dikkat edin.
- API'den gelen fiyat bilgisi anlık piyasa verilerine göre küçük gecikmeler içerebilir.

---

## English (İngilizce)

### Project Description
This project is a basic automation script that prints the current price of Bitcoin (BTC) in Turkey to the console by making a simple request to CoinGecko's free API. The project demonstrates fundamental Python skills such as API usage, HTTP requests, and JSON data processing.

### Technologies
- Python
- Requests Library

### Core Features
- Connects to the CoinGecko API using the `requests` library.
- Fetches the current price of Bitcoin (BTC) in Turkish Lira (TRY).
- Prints the result to the console in a user-friendly format (e.g., "Bitcoin Price: 1,234,567.89 TRY").

### Setup and Usage
1.  **Python Installation**: Ensure you have Python (3.6 or higher) installed on your system.
2.  **Library Installation**: Install the required `requests` library.
    ```bash
    pip install requests
    ```
3.  **Project File**: Save the project file (e.g., `btc_price.py`) to a directory.
4.  **Execution**: Open your terminal/command prompt, navigate to the directory, and run the script.
    ```bash
    python btc_price.py
    ```

### Code Example
The script sends a GET request to the specified API endpoint, parses the incoming JSON response, and extracts the price information to display it.

### API Reference
- **API Used**: CoinGecko Simple Price API
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=try`

### Notes & Disclaimers
- This project is for educational purposes. For commercial use, please check CoinGecko's API terms of service.
- The API may have a rate limit; please be mindful of this.
- The price information may have slight delays compared to real-time market data.

---

## License
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. / This project is licensed under the [MIT License](LICENSE).
