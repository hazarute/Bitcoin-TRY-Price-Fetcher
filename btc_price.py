import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=try"

def get_bitcoin_price():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # HTTP hataları için istisna fırlat
        data = response.json()
        bitcoin_price = data.get('bitcoin', {}).get('try')
        if bitcoin_price:
            print(f"Bitcoin Fiyatı: {bitcoin_price:,.2f} TRY")
        else:
            print("Bitcoin TRY fiyatı bulunamadı.")
    except requests.exceptions.RequestException as e:
        print(f"API isteği sırasında bir hata oluştu: {e}")
    except ValueError as e:
        print(f"JSON ayrıştırma hatası: {e}")

if __name__ == "__main__":
    get_bitcoin_price()