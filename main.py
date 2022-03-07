import sys, httpx
from threading import Thread
from fake_headers import Headers

proxiesFile = 'all.txt'


aliveFile = 'alive.txt'
aliveMode = 'w' # w=write, a=append

proxyType = 'http' # type of proxies to check ('socks5' or 'http')

proxylist = []
workingProxies = []
threads = []

def import_proxies(proxiesFile):
    print('[IMPORTING] Proxylist from ' + proxiesFile)
    proxies = open(proxiesFile)
    for x in proxies:
        tmp = x.strip().split(":")
        ip = tmp[0]
        port = tmp[1]

        proxy = {"ip": ip, "port": port}
        proxylist.append(proxy)
    proxies.close()
    print('[IMPORTED] Proxylist')
    return

def saveActive():
    print('[SAVING] Active proxies...')
    alive = open('./'+aliveFile, aliveMode)
    for proxy in workingProxies:
        alive.write(proxy['ip'] + ':' + proxy['port']+'\n')
    alive.close()
    print('[SAVED] Active proxies in ' + '"' + aliveFile + '".')
    return

def check_proxy(proxy):
    headers = Headers(headers=True).generate()
    proxies = {'https://': proxyType + '://' + proxy['ip'] + ':' + proxy['port']}
    with httpx.Client(http2=True,headers = headers, proxies=proxies) as client:
        try:
            req = client.get('https://1.1.1.1/')
            if req.status_code <= 400:
                print('[Alive] ' + proxy['ip'] + ':' + proxy['port'] + ' - ' + str(req.status_code))
                workingProxies.append(proxy)
            else:
                print('[Blocked] ' + proxy['ip'] + ':' + proxy['port'] + ' - ' + str(req.status_code))
        except httpx.HTTPError as exc:
            return exc
        return True

def check_proxyList():
    print('[CHECKING - Proxylist]')
    for proxy in proxylist:
        thread = Thread( target=check_proxy, args=(proxy, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print('[DONE CHECKING - Proxylist]')
    return


import_proxies(proxiesFile)
check_proxyList()
print('[STATUS] ' + str(len(workingProxies)) + ' proxies from ' + str(len(proxylist)) + ' alive.')
saveActive()
