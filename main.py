from bs4 import BeautifulSoup
import requests 
import schedule

def botSendText(botMessage):
    bot_token = 'TOKEN'  
    bot_chat_ID = 'CHAT_ID' 
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_ID + '&parse_mode=Markdown&text=' + botMessage

    response = requests.get(send_text)
    return response


def btc_scrapping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text

    return format_result


def eth_scrapping():                                                                                                                                                                    
    url = requests.get('https://awebanalysis.com/es/coin-details/ethereum/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td',  {'class': 'wbreak_word align-middle coin_price' }) #Buscamos especificamente el precio
    format_result = result.text

    return format_result

    

def message():
    btc_price = f'El precio de Bitcoin es de {btc_scrapping()}'
    eth_price = f'El precio de Ethereum es de {eth_scrapping()}'
    botSendText(btc_price)
    botSendText(eth_price)


if __name__ == '__main__':
    #Set alert time
    schedule.every().day.at("10:00").do(message)

    while True:
        schedule.run_pending()
