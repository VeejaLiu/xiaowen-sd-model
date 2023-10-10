import requests
import time
import random
from hashlib import md5

from env_config import BAIDU_TRANSLATE_CONFIG

# Set your own appid/appkey.
appid = BAIDU_TRANSLATE_CONFIG['APP_ID']
appkey = BAIDU_TRANSLATE_CONFIG['APP_KEY']
endpoint = BAIDU_TRANSLATE_CONFIG['ENDPOINT']
path = BAIDU_TRANSLATE_CONFIG['PATH']
url = endpoint + path
headers = {'Content-Type': 'application/x-www-form-urlencoded'}


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def translate(q, from_lang='zh', to_lang='en', max_retry=3, retry_interval=0.5):
    # 去除首尾空格
    q = q.strip()
    if not q or len(q) == 0:
        return ""
    print(f"Translating [{len(q)}]'{q}'")
    for i in range(max_retry):

        try:
            # 构造请求参数
            salt = random.randint(32768, 65536)
            sign = make_md5(appid + q + str(salt) + appkey)
            payload = {'appid': appid, 'q': q, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

            # 发送请求
            r = requests.post(url, params=payload, headers=headers)
            r.raise_for_status()
            result = r.json()

            # 返回翻译结果
            translate_result = result['trans_result'][0]['dst']
            print(f"Translated [{len(translate_result)}]'{translate_result}'")
            return translate_result

        except Exception as e:
            print(f"Translate request failed, retrying {i + 1}/{max_retry}")
            time.sleep(retry_interval)

    # 重试失败抛出异常
    raise Exception("Translate failed after max retries")


if __name__ == '__main__':
    test_cases = [
        # 一般中文
        "这是一只可爱的小猫",
        "今天北京天气很好",
        "我想学习编程",
        # 英文
        "This is a cute cat",
        "Hello world",
        # 特殊符号
        "我的电话号码是 10086@#¥%",
        # HTML标签
        "今天是<b>圣诞节</b>,我们一起<i>欢庆</i>吧",
        # 空字符串
        "",
        # 很长的句子
        "我想要大声告诉这个世界,我深爱着静静的生活,夕阳下的散步才是我今生最大的梦想。",
        "好久不见,朋友!祝你新年快乐,身体健康!",
    ]
    for case in test_cases:
        print(f"Translating '{case}'")
        print(f"Result: '{translate(case)}'")  # 默认中译英
        print()
