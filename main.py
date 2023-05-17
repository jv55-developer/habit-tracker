import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "fmw897#@#@%nv__=8278y",
    "username": "jv55",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

res = requests.post(url=pixela_endpoint, json=user_params)
print(res.text)
