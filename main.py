import os, httpx, time, threading
from colorama import Fore
from fake_useragent import UserAgent

ua = UserAgent()
def xx(PROXY, url):
    proxies = {'https://': 'http://' + PROXY}
    headers = {'User-Agent':str(ua.chrome)}
    with httpx.Client(http2=True,headers = headers, proxies=proxies) as client:
        try:
            req = client.get('https://1.1.1.1/')
            if req.status_code <= 400:
                print (Fore.GREEN + '[Valid] ' + PROXY + ' ' + str(req.status_code))
                with open('valid.txt', 'w') as xX:
                    xX.write(PROXY + '\n')
            else:
                print(Fore.YELLOW + '[Blocked] ' + PROXY + ' ' + str(req.status_code))
        except httpx.HTTPError as exc:
            print(Fore.RED + '[Bad] ' + PROXY) 
        return True

def main():
    try:
        fileproxy = input(' [+] File: ')
    except:
        print('  [-] Error : Enter Your Proxy List!')
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    print('starting threads')
    time.sleep(1)
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, 'https://1.1.1.1/'))
        t.start()
        thread.append(t)
        time.sleep(0.05)
    print('ending')
    for i in thread:
        i.join()
    print('stopped ' + i + ' threads')
main()
