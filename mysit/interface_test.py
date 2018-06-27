import requests
import unittest

class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_null(self):
        '''发布会id为空'''
        r = requests.get(self.url, params={'eid': ''})
        result = r.json()
        print(result)
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_success(self):
        '''发布会id为4，查询成功'''
        r = requests.get(self.url, params={'eid': '4'})
        result = r.json()
        print(result)
        assert result['status'] == 200
        assert result['message'] == "success"
        assert result['data']['name'] == "iphonexf发布会"
        assert result['data']['address'] == "山东省打打杀杀的宋丹丹说三道四"
        assert result['data']['start_time'] == "2018-06-07T07:26:34"

if __name__ == '__main__':
    unittest.main()
