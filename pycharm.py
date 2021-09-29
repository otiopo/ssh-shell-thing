import requests, colorama, sys

colorama.init()

while True:
    colorama.reinit()

    command = input(colorama.Fore.LIGHTGREEN_EX + requests.get("https://sshshell.otiopo.repl.co/user").text + "@ssh" + colorama.Style.RESET_ALL + ":" + colorama.Fore.BLUE + requests.get("https://sshshell.otiopo.repl.co/cwd").text + colorama.Style.RESET_ALL + "$ ")

    response = requests.post("https://sshshell.otiopo.repl.co/sendCommand?command=" + command)

    if response.status_code != 200:
        print(colorama.Fore.RED + "Error")
    else:
        print(colorama.Fore.WHITE + "\n" + response.text)
