#!/usr/bin/python3

from colorama import Fore
from rich.console import Console
import argparse, os, random, time, readline, json, datetime

version = 0.1
output_file = 'XSScanner-{}-output.json'.format(datetime.datetime.now().strftime("%x-%X").replace('/','').replace(':',''))



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
    return scan_php_files_for_xss(php_files)

def get_php_file(file):
    if file.endswith(".php"):
        php_file = [file]
        return scan_php_files_for_xss(php_file)
    print(Fore.RED + "File is not a PHP file")
    exit()
    
            

def scan_php_files_for_xss(files):
    console = Console()
    tasks = [f"task {n}" for n in files]
    sources = ['GET','POST', 'REQUEST', "SERVER\['PHP" "SERVER\['PATH_" "SERVER\['REQUEST_U"]
    sinks = ['echo', 'die', 'print', 'printf', 'print_r', 'var_dump']
    vulnerable = []
    files_count = len(files)
    with console.status("[bold green] Scanning {0} {1} ...".format(files_count, 'Files' if (files_count > 1) else 'File')) as status:
        time.sleep(2)
        for file_path in files:
            with open(file_path, 'r', errors="ignore") as f:
                for n, line in enumerate(f, 1):
                    for source in sources:
                        if source in line:
                            for sink in sinks:
                                if sink in line:
                                    vulnerable.append({'file': file_path, 'line #': n, 'code': line.lstrip().rstrip() ,'source': source, 'sink': sink})
                                    break
    return vulnerable


def main(argv):
    vulnerable = []
    if (argv['path'] is not None):
        folder_path = argv['path']
        vulnerable = get_php_files_from_folder(folder_path)
        if vulnerable:
            with open(output_file, 'w+') as f:
                    f.write(json.dumps(vulnerable) + '\n')
    elif (argv['path'] is not None):
        file_path = argv['path']
        vulnerable = get_php_file(file_path)
        if(len(vulnerable) > 1):
            with open(output_file, 'w+') as f:
                    f.write(json.dumps(vulnerable) + '\n')
    print(Fore.RED + '\n[-] {} Potential XSS Vulnerabilities Found.\n'.format(len(vulnerable)))
    if(argv['output']):
        if vulnerable:
            for vuln in vulnerable:
                print(Fore.RESET + '-' * 40,end='\n')
                print(Fore.RED + '\n[-] File: ' + vuln['file'])
                print(Fore.RED + '\n[-] Line #: ' + str(vuln['line #']))
                print(Fore.RED + '\n[-] Code: ' + vuln['code'])
                print(Fore.RED + '\n[-] Source: ' + vuln['source'])
                print(Fore.RED + '\n[-] Sink: ' + vuln['sink'], end='\n\n')
    
    print(Fore.RESET + '-' * 40,end='\n')
    print(Fore.GREEN + '\n[-] Scan Completed!')
    if vulnerable: print(Fore.LIGHTCYAN_EX + '\n[+] Scan Result Saved in: ' + output_file)
    print('\n')
            
                    


if __name__ == "__main__":
    banner_color = random.choice(list(vars(Fore).values()))
    print(banner_color + ascii_art())
    print(banner_color + 'Scanning PHP Files for XSS Vulnerabilities Never Been Any Easier!\n')
    print(banner_color + 'v{} - Written By: @b4zb0z\n\n'.format(version))


    print(Fore.RESET)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f','--file', help='Used To Define The Path of a Single File To Scan')
    group.add_argument('-p','--path', help='Used To Define The Path of a Folder To Scan')
    parser.add_argument("-o",'--output', help='Print Scan Output on Screen (default=false)', action='store_true',required=False, default=False)
    args = vars(parser.parse_args())
    readline.parse_and_bind('tab:complete')
    main(args)