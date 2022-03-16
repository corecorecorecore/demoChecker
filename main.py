import os, httpx, time, threading
from fake_useragent import UserAgent

ua = UserAgent()
def xx(PROXY, url):
    proxies = {'https://': 'http://' + PROXY}
    headers = {'User-Agent':str(ua.chrome)}
    with httpx.Client(http2=True,headers = headers, proxies=proxies) as client:
        try:
            req = client.get('https://1.1.1.1/')
            if req.status_code <= 400:
                print ('[Valid] ' + PROXY + str(req.status_code))
                with open('valid.txt', 'a') as xX:
                    xX.write(PROXY + '\n')
            else:
                print('[Blocked] ' + PROXY + str(req.status_code))
        except httpx.HTTPError as exc:
            print(exc)
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
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, 'https://1.1.1.1/'))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for i in thread:
        i.join()
main()
