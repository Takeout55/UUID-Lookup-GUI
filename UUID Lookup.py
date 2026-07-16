import requests
import os.path

while True:
    question = input("Username or UUID?")
    if question == "Username":
        Username = input("Username?")
        url = "https://api.mojang.com/users/profiles/minecraft/" + Username
        filename=Username

    if question == "UUID":
        UUID = input("UUID?")
        url = "https://api.minecraftservices.com/minecraft/profile/lookup/" + UUID
        filename=UUID

    resp = requests.get(url=url)
    data = resp.json()
    print(data)

    if os.path.isdir("files"):
        if os.path.isfile("files/" + filename + ".txt"):
            f = open("files/" + filename + ".txt", "w")
            f.write(str(data))
            f.close()
        else:
            f = open("files/" + filename + ".txt", "x")
            f.write(str(data))
            f.close()
    else:
        os.mkdir("files")
        f = open("files/" + filename + ".txt", "x")
        f.write(str(data))
        f.close()

    question1 = input("Restart? Y/N")
    question1.upper()
    if question1 == "Y":
        continue
    elif question1 == "N":
        break