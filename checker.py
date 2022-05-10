import os, httpx, time, random, sys, ctypes, json
from colorama import Fore
from threading import Thread

domain = 'http://ip-api.com/json/'
counter = [0,0,0,0,0]

def correctSingleQuoteJSON(s):
    rstr = ""
    escaped = False

    for c in s:
    
        if c == "'" and not escaped:
            c = '"'
        
        elif c == "'" and escaped:
            rstr = rstr[:-1]
        
        elif c == '"':
            c = '\\' + c
   
        escaped = (c == "\\")
        rstr += c
    return rstr
    
def xx(PROXY,url):
        with httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0','accept-language': 'en'},follow_redirects=True,proxies='http://' + PROXY) as client:
            try:
                    req2 = client.get(url)
                    correctJson = correctSingleQuoteJSON(str(req2.json()))
                    m = json.loads(correctJson)
                    if req2.status_code == 200 and 'success' in str(req2.content):
                        print (Fore.GREEN + '[Valid] ' + PROXY + ' ' + str(req2.status_code) + ' ' + m["country"] + ' ' + m["as"])
                        counter[1] = counter[1] + 1
                        counter[4] = counter[4] + 1
                        with open('http.txt', 'a') as xX:
                            xX.write(PROXY + '\n')
                    elif req2.status_code == 403:
                        print (Fore.YELLOW + '[Blocked] ' + PROXY + ' ' + str(req2.status_code))
                        counter[2] = counter[2] + 1
                        counter[4] = counter[4] + 1
                    else:
                        print(Fore.RED + '[Bad] ' + PROXY + ' ' + str(req2.status_code))
                        counter[3] = counter[3] + 1
                        counter[4] = counter[4] + 1
            except httpx.HTTPError as exc:
                counter[3] = counter[3] + 1
                counter[4] = counter[4] + 1            
            except:
                counter[3] = counter[3] + 1
                counter[4] = counter[4] + 1
                #print(Fore.RED + '[Bad] ' + PROXY)
                
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
    Threads = []
    for proxy in prox:
        t = Thread(target=xx, args=(proxy,domain),daemon=True)
        t.start()
        Threads.append(t)
        counter[0] = counter[0] + 1
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('Proxies: ' + str(counter[4]) +'/'+ str(counter[0]) + ' | Valid: ' + str(counter[1]) + ' | Blocked: ' + str(counter[2]) + ' | Bad: ' + str(counter[3]))
        else:
            sys.stdout.write("\x1b]2;"+'Proxies: ' + str(counter[4]) +'/'+ str(counter[0]) + ' | Valid: ' + str(counter[1]) + ' | Blocked: ' + str(counter[2]) + ' | Bad: ' + str(counter[3])+"\x07")
        time.sleep(0.01)
    for i in Threads:
        i.join()
        if os.name == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW('Proxies: ' + str(counter[4]) +'/'+ str(counter[0]) + ' | Valid: ' + str(counter[1]) + ' | Blocked: ' + str(counter[2]) + ' | Bad: ' + str(counter[3]))
        else:
            sys.stdout.write("\x1b]2;"+'Proxies: ' + str(counter[4]) +'/'+ str(counter[0]) + ' | Valid: ' + str(counter[1]) + ' | Blocked: ' + str(counter[2]) + ' | Bad: ' + str(counter[3])+"\x07")
        
if __name__ == "__main__":
    main()
