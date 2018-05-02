import requests
files = {
    'files': open('data/2/st_aq_05-01_submission.csv','rb')
}
data = {
    "user_id": "nodgd",
    "team_token": "4dbe68b547d0295813644d576a5248ee9b52377514436fe25271c5904668674e",
    "description": "5.2: use yesterday's data",
    "filename": "st_aq_05-01_submission.csv",
}
url = 'https://biendata.com/competition/kdd_2018_submit/'
response = requests.post(url, files=files, data=data)
print(response.text)