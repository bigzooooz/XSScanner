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

-----


## Installation:

1. `git clone https://github.com/bigzooooz/XSScanner`
2. `cd XSScanner`
3. `pip install requirements.txt`
4. `python XSScanner.py -p <PATH>`

-----


## Usage:
```
usage: XSScanner.py [-h] (-f FILE | -p PATH) [-o]

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Used To Define The Path of a Single File To Scan
  -p PATH, --path PATH  Used To Define The Path of a Folder To Scan
  -o, --output          Print Scan Output on Screen (default=false)
```

All Results Will Be Stored in `XSS-{timestamp}-output.json` file.

Adding `-o` flag will print results on screen.

-----
## License
The XXScanner is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
