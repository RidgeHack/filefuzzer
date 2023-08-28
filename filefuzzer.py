import argparse
import requests

# ASCII art
ascii_art = r"""
    _______ __     ______                         
   / ____(_) /__  / ____/_  __________  ___  _____
  / /_  / / / _ \/ /_  / / / /_  /_  / / _ \/ ___/
 / __/ / / /  __/ __/ / /_/ / / /_/ /_/  __/ /    
/_/   /_/_/\___/_/    \__,_/ /___/___/\___/_/     
                                                  
"""

def fuzz_files(url, wordlist, file_types, display_output):
    with open(wordlist, 'r') as f:
        words = f.read().splitlines()

    found_files = []

    for word in words:
        for file_type in file_types:
            fuzzed_url = f"{url}/{word}.{file_type}"
            
            try:
                response = requests.get(fuzzed_url)
                if response.status_code == 200:
                    found_files.append(fuzzed_url)
                    if display_output:
                        print(f"File found at URL: {fuzzed_url}")
            except requests.exceptions.RequestException as e:
                pass  # Ignore errors and continue to the next URL

    return found_files

def download_files(found_files):
    for url in found_files:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split("/")[-1]
                with open(file_name, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded file: {file_name}")
        except requests.exceptions.RequestException as e:
            pass  # Ignore errors and continue to the next URL

def main():
    parser = argparse.ArgumentParser(description="Fuzz and download files from URLs")

    parser.add_argument('-u', '--url', required=True, help='Target Url to fuzz')
    parser.add_argument('-w', '--wordlist', required=True, help='Wordlist Path')
    parser.add_argument('-f', '--file-types', default='pdf', help='Comma-separated list of file types')
    parser.add_argument('-o', '--display-output', action='store_true', help='Displays output for found files')
    parser.add_argument('-n', '--no-download', action='store_true', help='Stops automatic file downloads')

    args = parser.parse_args()
    file_types = args.file_types.split(',')

    print(ascii_art)  # Print the ASCII art

    found_files = fuzz_files(args.url, args.wordlist, file_types, args.display_output)
    
    if not args.no_download:
        download_files(found_files)

if __name__ == "__main__":
    main()
