from bs4 import BeautifulSoup
import requests 
import schedule

def botSendText(botMessage):
    bot_token = 'TOKEN'  
    bot_chat_ID = 'CHAT_ID' 
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_ID + '&parse_mode=Markdown&text=' + botMessage

    response = requests.get(send_text)
    return response


def coin_scrapper(coin_url):
    url = requests.get(coin_url)
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text

    return format_result


def message():
    btc_price = f'El precio de Bitcoin es de {btc_scrapping('https://awebanalysis.com/es/coin-details/bitcoin/')}'
    eth_price = f'El precio de Ethereum es de {eth_scrapping('https://awebanalysis.com/es/coin-details/ethereum/')}'
    botSendText(btc_price)
    botSendText(eth_price)


if __name__ == '__main__':
    #Set alert time
    schedule.every().day.at("10:00").do(message)

    while True:
        schedule.run_pending()
