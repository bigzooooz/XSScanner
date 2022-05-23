#!/usr/bin/python3

from colorama import Fore
from flask import jsonify
from rich.console import Console
import requests, argparse, os, random, time, readline, json, datetime, re, sys
with open('VERSION', 'r', errors="ignore") as f:
    version = f.readline()

def update_check():
    try:
        response = requests.get('https://raw.githubusercontent.com/bigzooooz/XSScanner/master/VERSION')
        if response.status_code == 200:
            if response.text > version:
                print(Fore.MAGENTA + " New version available!")
                time.sleep(1)
                print(Fore.GREEN + " Add --update To Update")
                time.sleep(2)
                return True
            else:
                return False
    except:
        return False
    return False




def ascii_art():
    art = ['''\n\n /$$   /$$  /$$$$$$   /$$$$$$                                                             
| $$  / $$ /$$__  $$ /$$__  $$                                                            
|  $$/ $$/| $$  \__/| $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
 \  $$$$/ |  $$$$$$ |  $$$$$$  /$$_____/ |____  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
  >$$  $$  \____  $$ \____  $$| $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
 /$$/\  $$ /$$  \ $$ /$$  \ $$| $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$  \ $$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$$| $$      
|__/  |__/ \______/  \______/  \_______/ \_______/|__/  |__/|__/  |__/ \_______/|__/      
''',
'''\n\n                                                                                        
 ,--,     ,--,  .--.--.    .--.--.                                                                     
 |'. \   / .`| /  /    '. /  /    '.                                                                   
 ; \ `\ /' / ;|  :  /`. /|  :  /`. /                              ,---,      ,---,             __  ,-. 
 `. \  /  / .';  |  |--` ;  |  |--`                           ,-+-. /  | ,-+-. /  |          ,' ,'/ /| 
  \  \/  / ./ |  :  ;_   |  :  ;_       ,---.     ,--.--.    ,--.'|'   |,--.'|'   |   ,---.  '  | |' | 
   \  \.'  /   \  \    `. \  \    `.   /     \   /       \  |   |  ,"' |   |  ,"' |  /     \ |  |   ,' 
    \  ;  ;     `----.   \ `----.   \ /    / '  .--.  .-. | |   | /  | |   | /  | | /    /  |'  :  /   
   / \  \  \    __ \  \  | __ \  \  |.    ' /    \__\/: . . |   | |  | |   | |  | |.    ' / ||  | '    
  ;  /\  \  \  /  /`--'  //  /`--'  /'   ; :__   ," .--.; | |   | |  |/|   | |  |/ '   ;   /|;  : |    
./__;  \  ;  \'--'.     /'--'.     / '   | '.'| /  /  ,.  | |   | |--' |   | |--'  '   |  / ||  , ;    
|   : / \  \  ; `--'---'   `--'---'  |   :    :;  :   .'   \|   |/     |   |/      |   :    | ---'     
;   |/   \  ' |                       \   \  / |  ,     .-./'---'      '---'        \   \  /           
`---'     `--`                         `----'   `--`---'                             `----'         
''',
'''\n\n \o       o/   o__ __o        o__ __o                                                                         
  v\     /v   /v     v\      /v     v\                                                                        
   <\   />   />       <\    />       <\                                                                       
     \o/    _\o____        _\o____            __o__    o__ __o/  \o__ __o   \o__ __o     o__  __o   \o__ __o  
      |          \_\__o__       \_\__o__     />  \    /v     |    |     |>   |     |>   /v      |>   |     |> 
     / \               \              \    o/        />     / \  / \   / \  / \   / \  />      //   / \   < > 
   o/   \o   \         /    \         /   <|         \      \o/  \o/   \o/  \o/   \o/  \o    o/     \o/       
  /v     v\   o       o      o       o     \\         o      |    |     |    |     |    v\  /v __o   |        
 />       <\  <\__ __/>      <\__ __/>      _\o__</   <\__  / \  / \   / \  / \   / \    <\/> __/>  / \       
''',
'''\n\n
$$\   $$\  $$$$$$\   $$$$$$\                                                             
$$ |  $$ |$$  __$$\ $$  __$$\                                                            
\$$\ $$  |$$ /  \__|$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
 \$$$$  / \$$$$$$\  \$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
 $$  $$<   \____$$\  \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$  /\$$\ $$\   $$ |$$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
$$ /  $$ |\$$$$$$  |\$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|  \__| \______/  \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|      
''',
'''\n\n
 __   __ _____ _____                                 
 \ \ / // ____/ ____|                                
  \ V /| (___| (___   ___ __ _ _ __  _ __   ___ _ __ 
   > <  \___ \\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  / . \ ____) |___) | (_| (_| | | | | | | |  __/ |   
 /_/ \_\_____/_____/ \___\__,_|_| |_|_| |_|\___|_|     
'''
]

    return random.choice(art)


def get_php_files_from_folder(folder_path):
    php_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".php"):
                php_files.append(os.path.join(root, file))
    return php_files  

def scan_php_files_for_xss(folder_path):
    console = Console()
    files = get_php_files_from_folder(folder_path)
    tasks = [f"task {n}" for n in files]
    sources = ['GET','POST', 'REQUEST', "SERVER\['PHP" "SERVER\['PATH_" "SERVER\['REQUEST_U"]
    sinks = ['echo', 'die', 'print', 'printf', 'print_r', 'var_dump']
    vulnerable = {}
    files_count = len(files)
    if files_count == 0:
        console.print(" \n [bold red][!] No PHP files found in the folder\n")
        return False
    with console.status("[bold green] Scanning {0} {1} ...".format(files_count, 'Files' if (files_count > 1) else 'File')) as status:
        time.sleep(2)
        for file_path in files:
            scanned_path = file_path.split("/")[-1]
            with open(file_path, 'r', errors="ignore") as f:
                for n, line in enumerate(f, 1):
                    for source in sources:
                        if source in line:
                            for sink in sinks:
                                if sink in line:
                                    exploitable_files = locate_exploitable_file(file_path.split("/")[-1],files)
                                    if(exploitable_files is None): break
                                    exploit = {}
                                    for exploitable in exploitable_files:
                                        exploitable_path = exploitable['file'].split("SCAN")[-1]
                                        start = "$_"+source+"['"
                                        end = "']"
                                        parameter = line.lstrip().rstrip().partition(start)[2].partition(end)[0]
                                       
                                        if source == "GET":
                                            if exploitable_path.split('/')[1] not in exploit:
                                                exploit[exploitable_path.split('/')[1]] = [{'file':exploitable_path.lstrip('/') +'?'+parameter+'=XSS_PAYLOAD', 'code':exploitable['code'], 'parameter':parameter}]
                                            else:
                                                exploit[exploitable_path.split('/')[1]].append({'file':exploitable_path.lstrip('/') +'?'+parameter+'=XSS_PAYLOAD', 'code':exploitable['code'], 'parameter':parameter})
                                        else:
                                            if exploitable_path.split('/')[1] not in exploit:
                                                exploit[exploitable_path.split('/')[1]] = [{'file':exploitable_path.lstrip('/'), 'code':exploitable['code'], 'parameter':parameter}]
                                            else:
                                                exploit[exploitable_path.split('/')[1]].append({'file':exploitable_path.lstrip('/'), 'code':exploitable['code'], 'parameter':parameter})
                                    if file_path.split("/")[1] not in vulnerable:
                                        vulnerable[file_path.split("/")[1]] = [{'file': scanned_path, 'line #': n, 'code': line.lstrip().rstrip() ,'source': source, 'sink': sink, 'exploitation': exploit[file_path.split("/")[1]]}]
                                    else:
                                        vulnerable[file_path.split("/")[1]].append({'file': scanned_path, 'line #': n, 'code': line.lstrip().rstrip() ,'source': source, 'sink': sink, 'exploitation': exploit[file_path.split("/")[1]]})
    return vulnerable

def locate_exploitable_file(file_name,files):
    console = Console()
    exploitable = []
    for file in files:
        with open(file, 'r', errors="ignore") as f:
            for n, line in enumerate(f, 1):
                if(re.search(file_name,line) is not None):
                    exploitable.append({'file': file, 'code': line.lstrip().rstrip()})
    return exploitable
   

def scan_remote_target(target, vuln_list):
    console = Console()
    payload='XSS_PAYLOAD'
    with console.status("[bold green] Scanning {0} for XSS ...".format(target)) as status:
        time.sleep(2)
        for key in vuln_list:
            for v in vuln_list[key]:
                for exploit in v['exploitation']:
                    url = '{0}{1}'.format(target,exploit['file'])
                    http_status_errors = {
                        400: "Bad Request",
                        401: "Unauthorized",
                        403: "Forbidden",
                        404: "Not Found",
                        405: "Method Not Allowed",
                        408: "Request Timeout",
                        500: "Internal Server Error",
                        502: "Bad Gateway",
                        503: "Service Unavailable",
                        504: "Gateway Timeout",
                    }
                    try:
                        if v['source'] == 'GET' or v['source'] == 'SERVER["PHP"]' or v['source'] == 'SERVER["PATH_"]' or v['source'] == 'SERVER["REQUEST_U"]' or v['source'] == 'REQUEST':
                            response = requests.get(url)
                        if response.status_code == 200:
                            if payload in response.text:
                                print(Fore.GREEN + "[+] {0} - Vulnerable: {1}".format(response.status_code,url))
                        else:
                            print(Fore.RED + "[!] {1} - {2} - Try Manually: {0}".format(url,response.status_code,http_status_errors[response.status_code]))
                    except requests.exceptions.ConnectionError:
                        print(Fore.RED + "[!] DNS Error, Check your internet connection or target")
                        return


def main(argv):

    if(argv['update']):
        console = Console()
        with console.status("Checking for Updates...") as status:
            if(update_check()):
                print(Fore.CYAN + "Current Version: {0}".format(version))
                status.update(Fore.GREEN + "Update Found ...")
                time.sleep(2)
                status.update(Fore.GREEN + " Updating...")
                print(Fore.GREEN + "[+]  Initiating git pull ...")
                os.popen("git pull").read()
                print(Fore.GREEN + "[+] Update Downloaded Successfully!")
                print(Fore.GREEN + "[!] Please Restart ...")
                status.update(Fore.GREEN + " Exiting...")
                time.sleep(2)
                exit()    
            else:
                print(Fore.MAGENTA + "[-] No Updates Available")
                print(Fore.CYAN + "[-] Current Version: {0}".format(version))
                status.update(Fore.GREEN + " Exiting...")
                time.sleep(2)
                exit()

    update_check()

    if not os.path.exists('SCAN'):
                    os.makedirs('SCAN')
    folder_path = 'SCAN/' + argv['directory'] if argv['directory'] is not None else 'SCAN'
    count = 0
    vulnerable = scan_php_files_for_xss(folder_path)
    if vulnerable:
        for vuln in vulnerable:
            if(len(vuln) > 0):
                count += len(vulnerable[vuln])  
                if not os.path.exists('Results/{0}/'.format(vuln)):
                    os.makedirs('Results/{0}/'.format(vuln))            
                with open('Results/{0}/XSScanner-{1}-output.json'.format(vuln,vuln+'-'+ datetime.datetime.now().strftime("%x-%X").replace('/','').replace(':','')), 'w+') as f:
                    json.dump(vulnerable[vuln],f)
    if(count > 0):
        print(Fore.GREEN + '\n[-] {} Potential XSS Vulnerabilities Found.\n'.format(count))
    else:
        print(Fore.RED + '\n[-] No Vulnerabilities Found.\n')
    if(argv['output']):
        if vulnerable:
            for vuln in vulnerable:
                for vuln in vulnerable[vuln]:
                    print(Fore.RESET + '-' * 40,end='\n')
                    print(Fore.RED + '\n[-] File: ' + vuln['file'])
                    print(Fore.RED + '\n[-] Line #: ' + str(vuln['line #']))
                    print(Fore.RED + '\n[-] Code: ' + vuln['code'])
                    print(Fore.RED + '\n[-] Source: ' + vuln['source'])
                    print(Fore.RED + '\n[-] Sink: ' + vuln['sink'], end='\n\n')

    if (argv['target'] is not None):
        if argv['directory'] is None:
            print(Fore.RED + "[!] Please specify a directory using the flag -d if you wish to scan a remote target", end='\n\n')
            print(Fore.WHITE + "\n")
            parser.print_help()
            print(Fore.WHITE + "\n")
            exit()
        target = argv['target'].rstrip(argv['directory'])
        if vulnerable:
            print(Fore.RESET + '-' * 40,end='\n')
            scan_remote_target(target, vulnerable)
        
    
    print(Fore.RESET + '-' * 40,end='\n')
    print(Fore.GREEN + '\n[-] Scan Completed!')
    if vulnerable: print(Fore.LIGHTCYAN_EX + '\n[+] Scan Result Saved in Results Folder')
    print('\n')
            
                    


if __name__ == "__main__":
    banner_color = random.choice(list(vars(Fore).values()))
    print(banner_color + ascii_art())
    print(banner_color + 'Scanning PHP Files for XSS Vulnerabilities Never Been Any Easier!\n')
    print(banner_color + 'v{} - Written By: @b4zb0z\n\n'.format(version))


    print(Fore.RESET)

    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--directory', help='Used To Define a Directory Path To Scan (all folders will be scan if not provided a name)', required=False)
    parser.add_argument('-t','--target', help='Used To Define a Target URI To Test Against', type=str)
    parser.add_argument("-o",'--output', help='Print Scan Output on Screen (default=false)', action='store_true',required=False, default=False)
    parser.add_argument('--update', help='Update XSScanner', default=False, action='store_true')
    args = vars(parser.parse_args())
    readline.parse_and_bind('tab:complete')
    main(args)