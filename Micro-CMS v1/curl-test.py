import requests

for i in range(1, 1000):
    r = requests.get(f'http://35.227.24.107/c24dce6c00/page/edit/{i}')
    if r.status_code == 200:
        print(i)
