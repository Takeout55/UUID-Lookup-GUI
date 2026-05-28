import requests

question = input("Username or UUID?")
if question == "Username":
    Username = input("Username?")
    url = "https://api.mojang.com/users/profiles/minecraft/" + Username

if question == "UUID":
    UUID = input("UUID?")
    url = "https://api.minecraftservices.com/minecraft/profile/lookup/" + UUID

resp = requests.get(url=url)
data = resp.json()
print(data)