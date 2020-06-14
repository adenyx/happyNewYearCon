token = "someToken"

import requests
from datetime import datetime
import time


IsCycleWork = True
currentTime = datetime.now().hour

print(currentTime)

User1ID = "user1ID"
text = "someText"
User1Text = ["someText", "someText2"]
User2Text = "someText"
User3Text = "someText"
User4Text = "someText"
User5Text = "someText"
method = "messages.send"
userIDs = ["somobodyID1", "somobodyID2", "somobodyID3", "somobodyID4", "somobodyID5", "somobodyID6", "somobodyID7", "somobodyID8", "somobodyID9", "somobodyID10", "somobodyID11", "somobodyID12", "somobodyID13"]
apiVersion = "5.52"

while IsCycleWork:
    if datetime.now().hour == 00:
        for AText in User1Text:
            params = "access_token=" + token + "&user_id=" + User1ID + "&message=" + AText + "&v=" + apiVersion
            print(requests.get("https://api.vk.com/method/" + method + "?" + params).text)
            time.sleep(0.5)
        for userID in userIDs:
            if userID == "somebodyID1":
                print("Control mark: Somebody")
                params = "access_token=" + token + "&user_id=" + userID + "&message=" + User2Text + "&v=" + apiVersion
                print(requests.get("https://api.vk.com/method/" + method + "?" + params).text)
                time.sleep(0.5)
                continue
            if userID == "somobodyID2":
                print("Control mark: Somebody")
                params = "access_token=" + token + "&user_id=" + userID + "&message=" + User3Text + "&v=" + apiVersion
                print(requests.get("https://api.vk.com/method/" + method + "?" + params).text)
                time.sleep(0.5)
                continue
            if userID == "somobodyID3":
                print("Control mark: Somebody")
                params = "access_token=" + token + "&user_id=" + userID + "&message=" + User4Text + "&v=" + apiVersion
                print(requests.get("https://api.vk.com/method/" + method + "?" + params).text)
                time.sleep(0.5)
                continue
            if userID == "somobodyID4":
                print("Control mark: Somebody")
                params = "access_token=" + token + "&user_id=" + userID + "&message=" + User5Text + "&v=" + apiVersion
                print(requests.get("https://api.vk.com/method/" + method + "?" + params).text)
                time.sleep(0.5)
                continue
            params = "access_token=" + token + "&user_id=" + userID + "&message=" + text + "&v=" + apiVersion
            print(requests.get("https://api.vk.com/method/"+method+"?"+params).text)
            time.sleep(0.5)
        break
    else:
        time.sleep(1)