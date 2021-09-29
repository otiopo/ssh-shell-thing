import requests, colorama, sys

colorama.init()

while True:
    colorama.reinit()

    sys.stdout.write(colorama.Fore.LIGHTGREEN_EX)
    sys.stdout.flush()

    sys.stdout.write(requests.get("https://website url here/user").text + "@ssh")
    sys.stdout.flush()

    sys.stdout.write(colorama.Style.RESET_ALL)
    sys.stdout.flush()

    sys.stdout.write(":")
    sys.stdout.flush()

    sys.stdout.write(colorama.Fore.BLUE)
    sys.stdout.flush()

    sys.stdout.write(requests.get("https://website url here/cwd").text)
    sys.stdout.flush()

    sys.stdout.write(colorama.Style.RESET_ALL)

    command = input("$ ")

    response = requests.post("https://website url here/sendCommand?command=" + command)

    if response.status_code != 200:
        print(colorama.Fore.RED + "Error")
    else:
        print(colorama.Fore.WHITE + "\n" + response.text)
