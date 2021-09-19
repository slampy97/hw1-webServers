import requests

Base = "http://127.0.0.1:5000/"

moc_data = [{"name":"potato", "discount":0.7, "id":1},
            {"name":"tomato", "discount":0.1, "id":2},
            {"name":"ququmba", "discount":0.2, "id":3}]

for i in range(len(moc_data)):
    response = requests.put(Base + "mall/" + str(i), moc_data[i])
    print(response.json())
input()
response = requests.delete(Base + "mall/0")
print(response)
input()
response = requests.get(Base + "mall/1")
print(response.json())