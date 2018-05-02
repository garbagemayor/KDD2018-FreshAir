import requests
files = {
    'files': open('data/2/st_aq_05-01_submission.csv','rb')
}
data = {
    "user_id": "nodgd",
    "team_token": "53dfdfsdfdsfioiuoiuoiu7231asdfa7sdfdfsdf23cdf716e5072",
    "description": "5.2: use yesterday's data",
    "filename": "st_aq_05-01_submission.csv",
}
url = 'https://biendata.com/competition/kdd_2018_submit/'
response = requests.post(url, files=files, data=data)
print(response.text)