import pytchat
import requests
chat = pytchat.create(video_id="XEY8P6kN9AA")
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.datetime} [{c.author.name}]- {c.message}")

        if c.message == "ON" or c.message == "on":
          print("LED on")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V0=1')
          print(x.text)

        if  c.message == "OFF" or c.message == "off":
          print("LED off")
          x = requests.get('https://blr1.blynk.cloud/external/api/update?token=kI8yJW4Sxh9K1kxDcr4ZnamJ4gEKPFDO&V0=0')
          print(x.text)
	    
