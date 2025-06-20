import requests

target = input("Target: ")
wordlist = input("Wordlist: ")

with open(wordlist, "r") as file:
    for line in file:
        try:
            if "#" in line:
                continue
            url = f"{target}/{line.replace("\n", "")}"
            response = requests.get(url)
            if not ("Oops... ! the page you looking for isnt there!" in response.text):
                print(f"{line.replace("\n", "")}:{response.status_code}")
        except KeyboardInterrupt:
            break # solve this serious problem