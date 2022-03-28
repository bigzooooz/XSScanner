[![Python 3.6](https://img.shields.io/badge/Require-Python_3.x-blue)](https://www.python.org/downloads/)
[![Python 3.6](https://img.shields.io/badge/Require-pip-blue)](https://www.pypi.org/project/pip/)

 ```__   __ _____ _____                                 
 \ \ / // ____/ ____|                                
  \ V /| (___| (___   ___ __ _ _ __  _ __   ___ _ __ 
   > <  \___ \\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  / . \ ____) |___) | (_| (_| | | | | | | |  __/ |   
 /_/ \_\_____/_____/ \___\__,_|_| |_|_| |_|\___|_|  

    Scanning PHP Files for XSS Vulnerabilities Never Been Any Easier!
 ```    
Current Version: 1.2.0

-----



## Installation:

1. `git clone https://github.com/bigzooooz/XSScanner`
2. `cd XSScanner`
3. `pip install requirements.txt`
4. `python XSScanner.py -d <PATH>`

-----


## Usage:

#### Copy the directory you want to scan into `SCAN` folder then provide path with the `-d` flag
`python XSScanner.py -d SCAN/exampleDirectory`

#### To Scan and Validate Vulnerablity Against Live Target

`python XSScanner.py -d SCAN/exampleScript -t http://localhost/sameScript`

*Output:*
```
[-] 3 Potential XSS Vulnerabilities Found.

----------------------------------------
[+] 200 - Vulnerable: http://localhost/sameScript/admin/index.php?page=XSS_PAYLOAD
[+] 200 - Vulnerable: http://localhost/sameScript/admin/index.php?s=XSS_PAYLOAD
----------------------------------------

[-] Scan Completed!

[+] Scan Result Saved in: Results/exampleScript/XSScanner-032822-182205-output.json

```


#### flags and usage help

```
usage: XSScanner.py [-h] (-f FILE | -p PATH) [-o]

options:
  -h, --help            show this help message and exit
  -d PATH, --directory PATH  Used To Define The Path of a Folder To Scan
  -t TARGET, --target TARGET Used To Define a Target URI To Test Against
  -o, --output          Print Scan Output on Screen (default=false)
  --update              Update XSScanner
```

All Results Will Be Stored in `Results/{target_folder_name}/XSS-{timestamp}-output.json` file.

Adding `-o` flag will STDOUT print results on screen.

-----
## License
The XXScanner is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
