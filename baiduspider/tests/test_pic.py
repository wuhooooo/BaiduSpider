"""测试BaiduSpider的图片搜索函数

本测试案例用于测试`BaiduSpider.search_pic`及其实现函数。
"""
from unittest import TestCase
import sys
import os
import requests

class PicTestCase(TestCase):
    def __init__(self, methodName):
        """测试图片搜索

        本测试用于测试BaiduSpider.`search_pic`
        """
        super().__init__(methodName)

    def setUp(self):
        # 导入包
        sys.path.append(os.path.abspath('.'))
        from baiduspider.core import BaiduSpider
        from baiduspider.errors import ParseError
        self.spider = BaiduSpider()
        self.assets_base_url = 'https://gitlab.com/samzhangjy/BaiduSpiderTestAssets/-/raw/master/pic'
        self.normal_res = {
            'host': 'www.cwq.com',
            'title': 'python中文社区',
            'url': 'http://img.cwq.com/201611/581c95c35ca62.png'
        }
    
    def __get_asset(self, name):
        return requests.get('{base_url}/test_pic_{name}.html'.format(base_url=self.assets_base_url, name=name)).text

    def test_pic_normal(self):
        """测试普通搜索结果"""
        asset = self.__get_asset('normal')
        result = self.spider.parser.parse_pic(asset)
        self.assertIn(self.normal_res, result['results'])
    
    def test_spider_request(self):
        """测试爬虫获取网页"""
        result = self.spider.search_web('Python')
        self.assertIsNotNone(result['results'])
        