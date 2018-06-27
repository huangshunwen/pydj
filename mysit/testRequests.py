import requests
#查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url, params={'eid': '4'})
result = r.json()
print(result)
assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "iphonexf发布会"
assert result['data']['address'] == "山东省打打杀杀的宋丹丹说三道四"
assert result['data']['start_time'] == "2018-06-07T07:26:34"