import unittest
import requests
import jsonpath
from common.log_utils import logger
from common.config_utils import config
from common import public_api_infos
from requests.exceptions import RequestException

class TestGetAccessTokenApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_01_get_access_token(self):
        ''' 【api_case_01】测试获取access_token能否正常调用 '''
        logger.info('*********************************************')
        logger.info('*          用例[api_case_01]开始执行          *')
        try:
            url_params = {
                "grant_type": "client_credential",
                "appid": "wxb4835daaf8499dbe",
                "secret": "4f78328f444f39760e2919ce248f317e"
            }
            # response = self.session.get(url='https://%s/cgi-bin/token'%self.hosts,
            #                             params=url_params)
            response = public_api_infos.get_access_token_api(self.session,url_params)
            json_body = response.json()
            actual_result = jsonpath.jsonpath(json_body,'$.expires_in')[0]
            self.assertEqual(actual_result,7200)
        except Exception as e:
            logger.info('*          用例[api_case_01]断言失败          *')
        except RequestException as e:
            logger.error('%s'%e.__str__())
        finally:
            logger.info('*          用例[api_case_01]执行结束          *')
            logger.info('*********************************************')

    def test_02_appid_false(self):
        self._testMethodName = 'api_case_02'
        self._testMethodDoc = '测试获取access_token接口在appid错误时，能否正常处理错误'
        url_params = {
            "grant_type": "client_credential",
            "appid": "wxb4835daaf8499d",
            "secret": "4f78328f444f39760e2919ce248f317e"
        }
        # response = self.session.get(url='https://%s/cgi-bin/token'%self.hosts,
        #                             params=url_params)
        response = public_api_infos.get_access_token_api(self.session,url_params)
        json_body = response.json()
        actual_result = jsonpath.jsonpath(json_body,'$.errcode')[0]
        self.assertEqual(actual_result,40013)

if __name__ =='__main__':
    unittest.main(verbosity=2)