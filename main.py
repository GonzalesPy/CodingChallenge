import requests
import json
import time
import random

chall_url = "https://cc.the-morpheus.de/challenges/11/"
solution_url = "https://cc.the-morpheus.de/solutions/11/"


resp = requests.get(chall_url)
data = {"token": resp.text}

brackets = []
text = resp.text
result = 0

for i in range(len(text)):
    if text[i] == "(" or text[i] == ")":
        brackets.append(text[i])

def check(result):
    try:
        if len(brackets) % 2 == 0:
            if brackets[0] != ")":
                if brackets[len(brackets) - 1] != "(":
                    for x in range(len(brackets)):
                        if brackets[x] == "(":
                            result +=1
                        else:
                            result #= 1
                        if result == 0:
                            data["token"] = True
                        else:
                            data["token"] = False
                else:
                    data["token"] = False
            else:
                data["token"] = False
        else:
            data["token"] = False
    except IndexError:
        data["token"] = False

check(result)
result = requests.post(solution_url, json.dumps(data))
