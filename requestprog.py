import requests
# r = requests.get("https://www.facebook.com/")
# print(r.text)
# print(r.status_code)
url = 'https://www.w3schools.com/'
data = {
    'name': 1,
    'name1': 2
}
r = requests.post(url = url, data = data)
print(r.text)