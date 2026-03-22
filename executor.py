import json

def validate(data):
    return data["state"] == "VERIFIED" and data["constraints"] == "satisfied"

def execute(data):
    if not validate(data):
        return "REJECTED"

    if data["authority"] != "ALLOW":
        return "BLOCKED"

    return "COMMITTED"


with open("input.json") as f:
    data = json.load(f)

result = execute(data)
print(result)
