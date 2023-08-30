# FileFuzzer
## URL fuzzing tool made with Python 3.

filefuzzer is a simple python script that can fuzz multiple file types contained in URLs.

Disclaimer: FOR EDUCATIONAL PURPOSE ONLY! The contributors do not assume any responsibility for the use of this tool.

#### Tool and Commands 🧰
```bash
-h, --help             shows the help menu
-u, --url URL          Target Url to fuzz
-w, --wordlist         Wordlist Path
-f, --file-types       Comma-separated list of file types
-o, --display-output   Displays output for found files
-n, --no-download      Stops automatic file downloads
```

#### Sample Usage

#### Fuzzzing for files
```bash
python3 filefuzzer.py -u http://127.0.0.1 -w wordlist -f txt,pdf -o -n  

    _______ __     ______                         
   / ____(_) /__  / ____/_  __________  ___  _____
  / /_  / / / _ \/ /_  / / / /_  /_  / / _ \/ ___/
 / __/ / / /  __/ __/ / /_/ / / /_/ /_/  __/ /    
/_/   /_/_/\___/_/    \__,_/ /___/___/\___/_/     
                                                  

File found at URL: http://127.0.0.1/1.txt
File found at URL: http://127.0.0.1/1.pdf
```
#### Fuzzing for Files and automatically downloading them
```bash
python3 filefuzzer.py -u http://127.0.0.1 -w wordlist -f txt,pdf       

    _______ __     ______                         
   / ____(_) /__  / ____/_  __________  ___  _____
  / /_  / / / _ \/ /_  / / / /_  /_  / / _ \/ ___/
 / __/ / / /  __/ __/ / /_/ / / /_/ /_/  __/ /    
/_/   /_/_/\___/_/    \__,_/ /___/___/\___/_/     
                                                  

Downloaded file: 1.txt
Downloaded file: 1.pdf
```

# Installation 

```bash
git clone https://github.com/RidgeHack/filefuzzer.git
```










