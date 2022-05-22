[![Python 3.6](https://img.shields.io/badge/Require-Python_3.x-blue)](https://www.python.org/downloads/)
[![Python 3.6](https://img.shields.io/badge/Require-pip-blue)](https://www.pypi.org/project/pip/)
<!--![GitHub All Releases](https://img.shields.io/github/downloads/lewdev/hw-gen/total)*/-->
 ```__   __ _____ _____                                 
 \ \ / // ____/ ____|                                
  \ V /| (___| (___   ___ __ _ _ __  _ __   ___ _ __ 
   > <  \___ \\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  / . \ ____) |___) | (_| (_| | | | | | | |  __/ |   
 /_/ \_\_____/_____/ \___\__,_|_| |_|_| |_|\___|_|  

    Scanning PHP Files for XSS Vulnerabilities Never Been Any Easier!
 ```    
Current Version: 1.2.2

-----



## Installation:

1. `git clone https://github.com/bigzooooz/XSScanner`
2. `cd XSScanner`
3. `pip install -r requirements.txt`
4. `python XSScanner.py -d <PATH>`



## Usage:

#### Place the directory you want to scan into `SCAN` folder then provide path with the `-d` flag
`python XSScanner.py -d SCAN/exampleDirectory`

-----

#### To Scan and Validate Vulnerablity Against Live Target Add `-t` flag

**As of the currnet version (1.2.2), Attacking live target only:**

**1. Works with _GET_ and _REQUEST_ methods**

**2. Supports targets that requires not more than a single input _parameter_**

**3. Able to validate against single target**


`python XSScanner.py -d SCAN/exampleScript -t http://localhost/sameScript`

*Output:*
```Shell
[-] 3 Potential XSS Vulnerabilities Found.

----------------------------------------
[+] 200 - Vulnerable: http://localhost/sameScript/admin/index.php?page=XSS_PAYLOAD
[+] 200 - Vulnerable: http://localhost/sameScript/admin/index.php?s=XSS_PAYLOAD
----------------------------------------

[-] Scan Completed!

[+] Scan Result Saved in: Results/exampleScript/XSScanner-032822-182205-output.json

```


#### flags and usage help

```Shell
usage: XSScanner.py [-h] [-d DIRECTORY] [-t TARGET] [-o] [--update]

options:
  -h, --help            show this help message and exit
  -d PATH, --directory PATH  Used To Define The Path of a Folder To Scan
  -t TARGET, --target TARGET Used To Define a Target URI To Test Against
  -o, --output          Print Scan Output on Screen (default=false)
  --update              Update XSScanner
```

All Results Will Be Stored in `Results/{target_folder_name}/XSS-{timestamp}-output.json` file.

Adding `-o` flag will STDOUT print results on screen.


#### Output file
```json
[
  {
    "file": "/exampleScript/admin/inc/navigation.php",
    "line #": 116,
    "code": "var page = '<?php echo isset($_GET['page']) ? $_GET['page'] : 'home' ?>';",
    "source": "GET",
    "sink": "echo",
    "exploitation": [
      {
        "file": "admin/index.php?page=XSS_PAYLOAD",
        "code": "<?php require_once('inc/navigation.php') ?>",
        "parameter": "page"
      }
    ]
  }
]
```
-----

## CVEs Discoverd Using This Tool:

| CVE | Researcher | Publication
|-----------|------------|---------|
| [CVE-2022-28077](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28077) | [@b4zb0z](https://twitter.com/b4zb0z) | [Github](https://github.com/bigzooooz/CVE-2022-28077)
| [CVE-2022-28078](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28078) | [@b4zb0z](https://twitter.com/b4zb0z) | [Github](https://github.com/bigzooooz/CVE-2022-28078)

_Add your findings by sending a DM to [@b4zb0z](https://twitter.com/b4zb0z) on Twitter_

-----
## License
The XXScanner is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
