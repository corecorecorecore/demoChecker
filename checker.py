import os, httpx, time, random
from colorama import Fore
from fake_useragent import UserAgent
from threading import Thread

ua = UserAgent()
headers_list = [
{
'User-Agent':str(ua.firefox),
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Referer": "https://www.google.com/",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
},
{
'User-Agent':str(ua.firefox),
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://www.google.com/",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
},
{
"Connection": "keep-alive",
"DNT": "1",
"Upgrade-Insecure-Requests": "1",
'User-Agent':str(ua.chrome),
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Dest": "document",
"Referer": "https://www.google.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
},
{
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
'User-Agent':str(ua.chrome),
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Referer": "https://www.google.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9"
}
]
domain = 'https://1.1.1.1/'
def xx(PROXY,url):
    proxies = {'https://': 'http://' + PROXY}
    headers = random.choice(headers_list)
    with httpx.Client(http2=True,headers = headers, proxies=proxies) as client:
        try:
            req = client.get(url)
            if req.status_code <= 300:
                print (Fore.GREEN + '[Valid] ' + PROXY + ' ' + str(req.status_code))
                with open('http.txt', 'a') as xX:
                    xX.write(PROXY + '\n')
            else:
                print(Fore.YELLOW + '[Blocked] ' + PROXY + ' ' + str(req.status_code))
        except httpx.HTTPError as exc:
            #print(exc)
            pass

def main():
    if os.path.exists('http.txt'):
        os.remove('http.txt')
    else:
        pass
    try:
        fileproxy = input('File: ')
    except:
        print('Error : Enter Your Proxy List!')
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    print('Starting Threads')
    time.sleep(1)
    for proxy in prox:
        t = Thread(target=xx, args=(proxy,domain),daemon=True).start()
        time.sleep(0.01)
    print('ending')
    time.sleep(10)
    input('Exit')
if __name__ == "__main__":
    main()
