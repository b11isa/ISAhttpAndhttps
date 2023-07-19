
import requests
import webbrowser

url = "https://jsonplaceholder.typicode.com/"
a = requests.get(url)
a.raise_for_status()
print(a)

with open('json.json', 'w') as file:
    file.write(a.text)

URL = 'json.json'
webbrowser.open_new_tab(url)
# txt = "myfile.svg"
# with open(txt, 'wb') as file:
#     file.write(a.content)
#
