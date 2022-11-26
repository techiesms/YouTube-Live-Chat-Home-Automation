import pytchat
import requests
chat = pytchat.create(video_id="pMAgTNSl0sc")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.author.name}]- {c.message}")

        if c.message == "LIGHT1 ON" or c.message == "light1 on":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V0=1')
          print(x.text)

        if  c.message == "LIGHT1 OFF" or c.message == "light1 off":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V0=0')
          print(x.text)

        if c.message == "LIGHT2 ON" or c.message == "light2 on":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V1=1')
          print(x.text)

        if  c.message == "LIGHT2 OFF" or c.message == "light2 off":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V1=0')
          print(x.text)

        if c.message == "LIGHT3 ON" or c.message == "light3 on":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V2=1')
          print(x.text)

        if  c.message == "LIGHT3 OFF" or c.message == "light3 off":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V2=0')
          print(x.text)

        if c.message == "LIGHT4 ON" or c.message == "light4 on":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V3=1')
          print(x.text)

        if  c.message == "LIGHT4 OFF" or c.message == "light4 off":
          print("LED on Kare")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V3=0')
          print(x.text)

	    
