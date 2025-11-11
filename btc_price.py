import requests

def get_btc_price():
    API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=try"
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # HTTP hataları için istisna fırlat
        data = response.json()
        bitcoin_price = data.get('bitcoin', {}).get('try')
        return bitcoin_price
    except requests.exceptions.RequestException as e:
        print(f"API isteği sırasında bir hata oluştu: {e}")
        return None
    except ValueError as e:
        print(f"JSON ayrıştırma hatası: {e}")
        return None

def get_price(coin_id, currency):
    API_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        price = data.get(coin_id, {}).get(currency)
        return price
    except requests.exceptions.RequestException as e:
        print(f"API isteği sırasında bir hata oluştu: {e}")
        return None
    except ValueError as e:
        print(f"JSON ayrıştırma hatası: {e}")
        return None

if __name__ == "__main__":
    btc_price = get_btc_price()
    if btc_price:
        print(f"Bitcoin Fiyatı: {btc_price:,.2f} TRY")
    else:
        print("Bitcoin TRY fiyatı bulunamadı.")

    eth_usd_price = get_price("ethereum", "usd")
    if eth_usd_price:
        print(f"Ethereum Fiyatı: {eth_usd_price:,.2f} USD")
    else:
        print("Ethereum USD fiyatı bulunamadı.")