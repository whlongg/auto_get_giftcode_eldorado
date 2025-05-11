
ur_id = "user123@example.com" #Nhập id của bạn ở đây

#pip install requests
import requests
from time import sleep

def gift_code_request(id, code, platform="WEB"):
    url = "https://game.busidol.com/ELDORADO_WEB/coupon/input_coupon_after.php"  # Replace with your actual URL
    payload = {
        "UNIQ_ID": id,
        "COUPON_BUNHO": code,
        "PLATFORM": platform
    }    
    return requests.post(url, data=payload).text

def format_code(code):
    return f"{code[:4]}-{code[4:8]}-{code[8:12]}"

def get_code_from_file(file_path):
    with open(file_path, 'r') as file:
        codes = file.readlines()
    return [code.strip() for code in codes]

def main():
    codes = get_code_from_file('code.txt')
    for code in codes:
        formatted_code = format_code(code)
        response = gift_code_request(ur_id, formatted_code)
        print(f"{formatted_code}: {response}")
        sleep(1)

if __name__ == "__main__":
    main()
