import httpx
import csv
import os

url = 'https://jsonplaceholder.typicode.com/users'
response = httpx.get(url=url)
data = response.json()
print(data)
# os.mkdir('users')
os.chdir('users')
columns = ('id', 'username', 'email', 'phone', 'website', 'company name')
for user in data:
    with open(f"{user['username']}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerow((user['id'], user['username'], user['email'], user['phone'], user['website'], user['company']['name']))
