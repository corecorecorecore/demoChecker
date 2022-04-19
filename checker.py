import os, httpx, time, random, sys, ctypes
from colorama import Fore
from threading import Thread

uafile = 'uas.txt'
domain = 'https://1.1.1.1'
counter = [0,0,0,0]
def xx(PROXY,url):
    try:
        with httpx.Client(http2=True,headers = {'user-agent':random.choice(list(map(lambda x:x.strip(),open(uafile)))),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','accept-encoding': 'gzip, deflate, br','accept-language': 'en'}, proxies={'all://': 'http://' + PROXY},follow_redirects=True) as client:
            try:
                req = client.get(url)
                if req.status_code <= 300:
                    print (Fore.GREEN + '[Valid] ' + PROXY + ' ' + str(req.status_code))
                    counter[1] = counter[1] + 1
                    with open('http.txt', 'a') as xX:
                        xX.write(PROXY + '\n')
                else:
                    print(Fore.YELLOW + '[Blocked] ' + PROXY + ' ' + str(req.status_code))
                    counter[2] = counter[2] + 1
            except httpx.HTTPError as exc:
                counter[3] = counter[3] + 1
                #print(exc)
                pass
    except:
        pass
def main():
    if os.path.exists('http.txt'):
        os.remove('http.txt')
    else:
        pass
    try:
        fileproxy = 'all.txt'
    except:
        print('Error : Enter Your Proxy List!')
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    print('Starting Threads')
    time.sleep(1)
    for proxy in prox:
        t = Thread(target=xx, args=(proxy,domain),daemon=True).start()
        counter[0] = counter[0] + 1
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('Proxies: ' + str(counter[0]) + ' | Valid: ' + str(counter[1]) + ' | Blocked: ' + str(counter[2]) + ' | Bad: ' + str(counter[3]))
        else:
            sys.stdout.write("\x1b]2;"+'Proxies: ' + str(counter[0]) + ' | Valid: ' + str(counter[1]) + ' | Blocked: ' + str(counter[2]) + ' | Bad: ' + str(counter[3])+"\x07")
        time.sleep(0.01)
    print('ending')
    time.sleep(60)
    input('Exit')
if __name__ == "__main__":
    main()
