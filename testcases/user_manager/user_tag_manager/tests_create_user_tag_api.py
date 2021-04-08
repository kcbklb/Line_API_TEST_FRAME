import unittest
import requests
import json
import jsonpath
from common.config_utils import config
from common import public_api_infos

class TestsCreateUserTagApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_create_user_tag(self):
        self._testMethodName = 'api_case_03'
        self._testMethodDoc = '测试正常进行创建标签接口调用'
        token_id = public_api_infos.get_access_token(self.session)
        '''
        url_params = {
            "grant_type": "client_credential",
            "appid": "wxb4835daaf8499dbe",
            "secret": "4f78328f444f39760e2919ce248f317e"
        }
        # response = self.session.get(url='https://%s/cgi-bin/token'%self.hosts,
        #                             params=url_params)
        response = public_api_infos.get_access_token_api(self.session,url_params)
        json_body = response.json()
        token_id = jsonpath.jsonpath(json_body,'$.access_token')[0]
        '''
        url_params = {
            "access_token":token_id
        }
        post_data_json = {   "tag" : {     "name" : "english2"   } }
        # post_data_str = json.dumps(post_data_json,ensure_ascii=False)
        # response = self.session.post(url='https://%s/cgi-bin/tags/create'%self.hosts,
        #                              params=url_params,
        #                              data=post_data_str.encode('utf-8'))
        response = public_api_infos.create_user_tag_api(self.session,url_params,post_data_json)

        actual_result = jsonpath.jsonpath(response.json(),'$.tag.name')[0]
        self.assertEqual(actual_result,"english2")

if __name__=='__main__':
    unittest.main(verbosity=2)