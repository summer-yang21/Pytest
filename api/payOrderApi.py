from tools.logger import GetLog
import config as config
import allure
from tools.readIni import read_ini
log = GetLog().get_logger()


class PayOrder:
    def __init__(self):
        '''
        这个支付接口是需要重定向，302的url是从提交订单的接口里面获取jump_url
        '''
        # 消费数据
        self.url = read_ini('url', 'JUMP_URL')
        log.info(f'支付接口的url是{self.url}')

    def pay_order(self, session):
        # 对302接口进行处理，不让其重定向 allow_redirects=False
        resp = session.get(self.url, allow_redirects=False)
        log.info(f'支付的302跳转接口的响应是{resp}')
        log.info(f'支付的302跳转接口的响应头的location是{resp.headers["location"]}')
        resp_pay = session.get(resp.headers['location'])
        return resp_pay