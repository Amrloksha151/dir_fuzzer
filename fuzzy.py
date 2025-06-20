import requests

target = input("Target: ")
wordlist = input("Wordlist: ")

with open(wordlist, "r") as file:
    for line in file:
        response = requests.get(target + line)
        if not (response.status_code == 404):
            print(f"{line}:{response.status_code}")