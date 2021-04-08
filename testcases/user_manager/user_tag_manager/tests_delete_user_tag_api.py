import requests
import unittest
import jsonpath
from common import public_api_infos

class TestsDeleteUserTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_tagid_0(self):
        self._testMethodName = 'VXC_YH_003'
        self._testMethodDoc = '验证不能删除标签id为0的标签'
        token_id = public_api_infos.get_access_token(self.session)
        '''
        url_params = {
            "grant_type": "client_credential",
            "appid": "wxb4835daaf8499dbe", 
            "secret": "4f78328f444f39760e2919ce248f317e"
        }
        response = public_api_infos.get_access_token_api(self.session,url_params)
        json_body = response.json()
        token_id = jsonpath.jsonpath(json_body,'$.access_token')[0]
        '''
        url_params = {
            "access_token":token_id
        }
        post_data = {   "tag":{        "id" : 0   } }
        response = public_api_infos.delete_user_tag_api(self.session,url_params,post_data)
        actual_result = jsonpath.jsonpath(response.json(),'$.errcode')[0]
        self.assertEqual(actual_result,45058,'[VXC_YH_003]用例执行失败')

if __name__=='__main__':
    unittest.main(verbosity=2)