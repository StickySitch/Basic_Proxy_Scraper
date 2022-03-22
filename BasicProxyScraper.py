import requests
import re
from bs4 import BeautifulSoup
from proxy_checker import ProxyChecker
from requests.api import request
import concurrent.futures
from pyfiglet import Figlet


URLx = []
AllProxies = []
AllProxiesFull = []
uncheckedProxies = []
checkedProxies = []
httpProxies = []
httpProxiesFull = []
sock4ProxiesFull = []
sock4Proxies = []
sock5ProxiesFull = []
sock5Proxies = []
anonProxies = []
anonProxiesFull = []
transparentProxies = []
transparentProxiesFull = []
eliteProxiesFull = []
eliteProxies = []
inputSaveFull = str
workerCount = int




f = Figlet(font='speed')
print(f.renderText('Basic Proxy Scraper'))


print('Anwsers are case sensitive...')
inputCheckProxies = input('Check proxies for quality? Yes or No? ')
workerCountInput = input('How many threads do you want to run? ')

workerCount = int(workerCountInput)

if inputCheckProxies.strip() == 'Yes' or 'yes':
    inputCheckProxiesBool = True
        
if inputCheckProxies.strip() == 'No':
     inputCheckProxiesBool = False






def proxyScraper():
    #Opens and reads users URL Addresses
    with open("URLS.txt", 'r') as f:
        URLList = f.readlines()

    #Opens and reads all proxies already saved
    with open("Proxy Saves\AllProxies.txt") as f:
        AllProxies = f.read()
   
    

    #Starts looping through the list of URLS provided; Grabbing the HTML, parsing, and then searching for proxies.
    for ress in URLList:
        URLx.append(ress.strip())
        
    for res in URLx:
        html = requests.get(str(res))
        soup = BeautifulSoup(html.content, "html.parser")
        results = str(soup)
        prox = re.findall("[0-9]+(?:\.[0-9]+){3}:[0-9]+", results)

        #Starts looping through the found proxies, checking if they already exist on the Users saved list and if not, adding it.
        for proxy in prox:
            if proxy not in AllProxies:
                uncheckedProxies.append(proxy)
        
    f = open('UncheckedProxies.txt', 'w')
    for res in uncheckedProxies:
        f.write(str(res) + '\n')
    f.close()
    
    print('Your URLS: '+ '\n' + str(URLx))
        
    print('Scraping Complete.')

proxyScraper()




checker = ProxyChecker()

def ProxyCheck(ip):
    # Using input IP and checking it with proxy-checker
    groupAnswer = checker.check_proxy(ip)
    
    addIP = {"IP:Port":ip}    
    if groupAnswer != False:
        
        groupAnswer.update(addIP)
        AllProxiesFull.append(groupAnswer)
        AllProxies.append(ip)
       
        
       ### Checking for protocol type and appending to the corresponding list

        if 'http' in list(groupAnswer.items())[0][1]:
            httpProxiesFull.append(groupAnswer)
            httpProxies.append(ip)


        
        if 'socks4' in list(groupAnswer.items())[0][1]:
            sock4ProxiesFull.append(groupAnswer)
            sock4Proxies.append(ip)

        
        if 'socks5' in list(groupAnswer.items())[0][1]:
            sock5ProxiesFull.append(groupAnswer)
            sock5Proxies.append(ip)



        
        if 'Anonymous' in list(groupAnswer.items())[1][1]:
            anonProxiesFull.append(groupAnswer)
            anonProxies.append(ip)

        
        if 'Elite' in list(groupAnswer.items())[1][1]:
            eliteProxiesFull.append(groupAnswer)
            eliteProxies.append(ip)

        if 'Transparent' in list(groupAnswer.items())[1][1]:
            transparentProxiesFull.append(groupAnswer)
            transparentProxies.append(ip)


        print('\n' + 'Checked: ' + ip)
        print(groupAnswer)
            
# Function for multithreading using concurrent.futures.ThreadPoolExecutor
def runThread():
    
    print('Beginning Proxy Check...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=workerCount) as executor:
        executor.map(ProxyCheck, uncheckedProxies)

# Checking if user wants proxies checked. If so, threads start
if inputCheckProxiesBool == True: runThread()




# Fuction to write the results to text files
def SaveToText():


    f = open('Proxy Saves\AllProxies.txt', 'w+')
    for res in AllProxies:
        f.write(str(res)+ '\n')
    f.close()


    f = open('Full Proxy Saves\AllProxiesFull.txt', 'w+')  
    for res in AllProxiesFull:
        f.write(str(res) + '\n')
    f.close()
    




    f = open('Proxy Saves\HttpProxies.txt', 'w+')
    for res in httpProxies:
        f.write(str(res) + '\n')
    f.close()

    f = open('Full Proxy Saves\HttpProxiesFull.txt', 'w+')
    for res in httpProxiesFull:
        f.write(str(res) + '\n')
    f.close()





    f = open('Proxy Saves\Sock4Proxies.txt', 'w+')
    for res in sock4Proxies:
        f.write(str(res) + '\n')
    f.close()

    f = open('Full Proxy Saves\Sock4ProxiesFull.txt', 'w+')
    for res in sock4ProxiesFull:
        f.write(str(res) + '\n')
    f.close()




    f = open('Proxy Saves\Sock5Proxies.txt', 'w+')
    for res in sock5Proxies:
        f.write(str(res) + '\n')
    f.close()

    f = open('Full Proxy Saves\Sock5ProxiesFull.txt', 'w+')
    for res in sock5ProxiesFull:
        f.write(str(res) + '\n')
    f.close()





    f = open('AnonLevels\AnonProxies.txt', 'w+')
    for res in anonProxies:
        f.write(str(res) + '\n')
    f.close()

    f = open('AnonLevels\AnonProxiesFull.txt', 'w+')
    for res in anonProxiesFull:
        f.write(str(res) + '\n')
    f.close()



    f = open('AnonLevels\EliteProxies.txt', 'w+')
    for res in eliteProxies:
        f.write(str(res) + '\n')
    f.close()

    f = open('AnonLevels\EliteProxiesFull.txt', 'w+')
    for res in eliteProxiesFull:
        f.write(str(res) + '\n')
    f.close()


    f = open('AnonLevels\TransProxies.txt', 'w+')
    for res in transparentProxies:
        f.write(str(res) + '\n')
    f.close()

    f = open('AnonLevels\TransProxiesFull.txt', 'w+')
    for res in transparentProxiesFull:
        f.write(str(res) + '\n')
    f.close()

    print('Check out your .txt files for the scraped data.')
    input('Press ENTER to exit.')
    

SaveToText()