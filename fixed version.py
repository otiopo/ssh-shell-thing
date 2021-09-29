import requests, colorama, sys

colorama.init()

while True:
    colorama.reinit()

    command = input(colorama.Fore.LIGHTGREEN_EX + requests.get("https://website url here/user").text + "@ssh" + colorama.Style.RESET_ALL + ":" + colorama.Fore.BLUE + requests.get("https://website url here/cwd").text + colorama.Style.RESET_ALL + "$ ")

    response = requests.post("https://website url here/sendCommand?command=" + command)

    if response.status_code != 200:
        print(colorama.Fore.RED + "Error")
    else:
        print(colorama.Fore.WHITE + "\n" + response.text)
