import base64
import io
from datetime import datetime

import requests
import json
import PIL.Image as Image

url = "http://localhost:7860/sdapi/v1/txt2img"

payload = {
    "prompt": "1girl",
    "negative_prompt": "",
    "steps": 20,
    "batch_size": 1
}
headers = {"content-type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)

# JSON解析
json_data = json.loads(response.text)
# print(json_data)

# 获取图片数据
images_data = json_data['images']
# print(images_data)

# 保存图片
for i in range(len(images_data)):
    image_data = base64.b64decode(images_data[i])
    image_data_io = io.BytesIO(image_data)
    image = Image.open(image_data_io)
    # 文件命名时间格式
    file_name = datetime.now().strftime("%Y%m%d%H%M%S")
    # 保存图片
    image.save(f"image_{file_name}_{i}.png")