import requests

def email_alert(first, second, third):
    report = {}
    report["value1"] = first
    report["value2"] = second
    report["value3"] = third
    requests.post("https://maker.ifttt.com/trigger/HWS_notification/with/key/cZeYR3pOgWj7CZMa5gQT5J", data=report)    

print("Choose your first string.")
a = input()
print("Choose your second string.")
b = input()
print("Choose your third string.")
c = input()
email_alert(a, b, c)
