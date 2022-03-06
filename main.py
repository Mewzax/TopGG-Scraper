import httpx; from colorama import Fore, init; init()

def storeInvites(server, filename):
    invite = str(server).replace("discord.com/invite/", "discord.gg/")

    with open(filename, "a") as f:
        f.write(invite + "\n")

def topggScraper(skip):
    servers = httpx.post(
        f"https://top.gg/api/client/entities/search?platform=discord&entityType=server&amount=100&skip={skip}&nsfwLevel=1&sort=top",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "Origin": "https://top.gg",
            "Referer": "https://top.gg/en/servers",
        },
    )

    guilds = servers.json()["results"]
    for i in guilds:
        id = i["id"]
        server = httpx.get(f"https://top.gg/servers/{id}/join", follow_redirects=True)
        if "https://top.gg/servers/" in str(server.url):
            pass
        else:
            print(Fore.LIGHTGREEN_EX + '[x] ' + str(server.url) + Fore.RESET)
            storeInvites(server.url, "invites.txt")

if __name__ == "__main__":
    print(Fore.LIGHTRED_EX + '''
░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░░░░░░░░██████╗░░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗░░░░░░██╔════╝░██╔════╝░
╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝█████╗██║░░██╗░██║░░██╗░
░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗╚════╝██║░░╚██╗██║░░╚██╗
██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║░░░░░░╚██████╔╝╚██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░░░░░╚═════╝░░╚═════╝░
''' + Fore.RESET)
    scrapes = input(Fore.LIGHTBLUE_EX + 'How many servers to scrape? (enter 1 for 100): ' + Fore.RESET + '\n')
    skip = 0

    for i in range(int(scrapes)):
        skip += 100
        topggScraper(skip)