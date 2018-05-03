import requests

files = {
    'files': open('../data/2/submission.csv','rb')
}
data = {
    "user_id": "nodgd",
    "team_token": "4dbe68b547d0295813644d576a5248ee9b52377514436fe25271c5904668674e",
    "description": "5.4: use yesterday's model",
    "filename": "submission.csv",
}
url = 'https://biendata.com/competition/kdd_2018_submit/'
response = requests.post(url, files=files, data=data)
print(response.text)
print("提交完成")