import requestss

response = requests.get("http://httpbin.org/ip")

print(f"Your IP address is {response.json()['origin']}.")
