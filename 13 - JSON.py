import json

data = '''{
    "name" : "chuck",
    "phone" : {"type" : "intl",
        "number":"+11231234"},
    "email":{"hide":"yes"}
}'''

info = json.loads(data);
print("name = ",info["name"],info["email"]["hide"])

#another example

input = '''[
    {
    "id":"1",
    "name":"andre"
    },
    {
    "id":"2",
    "name":"chuck"
    }
]'''

info = json.loads(input)
print("user count = ",len(info))

for item in info:
    print("Id = ",item["id"])
    print("Nama = ",item["name"])

print(info[0]["name"])