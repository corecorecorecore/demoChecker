import os, httpx, time, threading
from colorama import Fore
from fake_useragent import UserAgent

ua = UserAgent()
domain = input('URL(with https://): ')
def xx(PROXY, url):
    proxies = {'https://': 'http://' + PROXY}
    headers = {'User-Agent':str(ua.chrome)}
    with httpx.Client(http2=True,headers = headers, proxies=proxies) as client:
        try:
            req = client.get(url)
            if req.status_code <= 400:
                print (Fore.GREEN + '[Valid] ' + PROXY + ' ' + str(req.status_code))
                with open('valid.txt', 'a') as xX:
                    xX.write(PROXY + '\n')
            else:
                print(Fore.YELLOW + '[Blocked] ' + PROXY + ' ' + str(req.status_code))
        except httpx.HTTPError as exc:
            pass
        return True

def main():
    if os.path.exists('valid.txt'):
        os.remove('valid.txt')
    else:
        pass
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
        t = threading.Thread(target=xx, args=(proxy, domain))
        thread.append(t)
        t.start()
        time.sleep(0.01)
    print('ending')
    for i in thread:
        i.join()
    print('stopped')
if __name__ == "__main__":
    main()
