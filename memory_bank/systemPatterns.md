# Sistem Mimarisi ve Desenleri

## 1. Genel Sistem Mimarisi
Bu proje, **Tek Dosyalı Script Mimarisi** kullanır. Herhangi bir sunucu, veritabanı veya kullanıcı arayüzü bileşeni yoktur. Çalıştırıldığında görevini yerine getiren ve sonlanan basit bir komut satırı uygulamasıdır.

## 2. Uygulanan Tasarım Desenleri
**Tek Yönlü API Çağrısı (One-Way API Call):**
Projenin temel çalışma prensibi bu desene dayanır.
- **Başlatma:** Kullanıcı script'i manuel olarak çalıştırır.
- **İstek (Request):** Script, harici bir veri kaynağı olan CoinGecko API'sine bir HTTP GET isteği gönderir.
- **Yanıt (Response):** API'den gelen JSON yanıtını alır.
- **İşleme ve Sonlandırma:** Yanıtı işler, sonucu konsola yazdırır ve çalışmasını sonlandırır.

Bu mimaride kalıcı bir durum (state) yönetimi veya bileşenler arası karmaşık bir etkileşim bulunmaz.

## 3. Veri Akış Şeması

```mermaid
graph TD
    A[Kullanıcı 'python btc_price.py' komutunu çalıştırır] --> B{btc_price.py Script'i};
    B -->|GET İsteği| C(CoinGecko API Endpoint);
    C -->|JSON Yanıtı| B;
    B -->|Fiyat bilgisini işler| D[Formatlanmış Çıktı];
    D -->|'print()' fonksiyonu| E(Kullanıcı Konsolu);
```
