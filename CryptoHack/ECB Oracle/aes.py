import requests
import string
import pprint

encode = {}

for i in range(2,34):
    plaintext=f"{'a'*i}".encode("utf-8").hex()
    response = requests.get(f'https://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/')
    if response.status_code == 200:
        data = response.json()
        ciphertext = data["ciphertext"]
        encode[i]=ciphertext[:64]
        #print(i, ": ", ciphertext)
print("Data collection done!")
pprint.pprint(encode)

charset=string.digits+string.ascii_letters+string.punctuation
flag="crypto{"

while flag[-1]!='}':
    for c in charset:
        temp_flag=flag+c
        position=32-len(temp_flag)
        plaintext=f"{'a'*position}{temp_flag}".encode("utf-8").hex()
        response = requests.get(f'https://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/')

        # Checking the status of the request (200 means success)
        if response.status_code == 200:
            data = response.json()
            ciphertext = data["ciphertext"]
            if ciphertext[:64]==encode[position]:
                break
    flag=temp_flag
print(flag)
