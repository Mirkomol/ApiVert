import requests

endpoint = "http://127.0.0.1:8000/"



get_response = requests.post(endpoint, params={"title":"Hello World"})

print(get_response.text)
print(get_response.status_code)
print(get_response.headers)

print(get_response.json())

# print(get_response.json())
# print(get_response.status_code)
#
