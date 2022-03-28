import os, httpx, time, random
from colorama import Fore
from fake_useragent import UserAgent
from threading import Thread

uafile = 'uas.txt'
domain = 'https://1.1.1.1'
def xx(PROXY,url):
    with httpx.Client(http2=True,headers = {'user-agent':random.choice(list(map(lambda x:x.strip(),open(uafile)))),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','accept-encoding': 'gzip, deflate, br','accept-language': 'en'}, proxies={'https://': 'http://' + PROXY},follow_redirects=True) as client:
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
    time.sleep(60)
    input('Exit')
if __name__ == "__main__":
    main()
