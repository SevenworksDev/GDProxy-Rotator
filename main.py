import gdproxy, time

def test():
    return gdproxy.get("/getAccountURL.php", data={"accountID": 16, "type": 2, "secret": "Wmfd2893gb7"})

while True:
    time.sleep(3)
    response = test()
    print("Response:", response)
