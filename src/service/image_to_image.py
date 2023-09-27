import logging
import os
from datetime import datetime
from compel import Compel

import torch
import torchvision
from diffusers import UniPCMultistepScheduler
from diffusers import ControlNetModel
from diffusers import StableDiffusionControlNetImg2ImgPipeline

from src.client.BaiduTranslator import translate
from src.utils.contorlnet import get_canny_image

print(os.get_exec_path())

# 加载ControlNet模型
controlnet = ControlNetModel.from_pretrained(
    """src//service//models//sd-controlnet-canny""",
    torch_dtype=torch.float16,
)

# 加载模型
pipe = StableDiffusionControlNetImg2ImgPipeline.from_pretrained(
    """src//service//models//v1-5-pruned-emaonly.safetensors""",
    controlnet=controlnet,
    torch_dtype=torch.float16,
)

# 设置采样方法
pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)

# 使用Compel来处理文本，将文本转换为模型可以理解的张量
compel = Compel(tokenizer=pipe.tokenizer, text_encoder=pipe.text_encoder)

pipe = pipe.to("cuda")

prefix_prompt = [
    'masterpiece, top quality, best quality',
    'Black and white tattoo design',
    'Monochromatic tattoo concept',
]
prefix_prompt_str = ", ".join(prefix_prompt)


def draw_with_image(image=None):
    # 获取Canny图像
    canny_image = get_canny_image(image)

    # 将文本转换为张量
    prompt_embeds = compel(prefix_prompt_str)

    # 生成图像
    start_time = datetime.now()
    generator = torch.manual_seed(0)
    images = pipe(
        prompt_embeds=prompt_embeds,
        # height=768,
        # width=512,
        generator=generator,
        # guidance_scale=7,
        num_inference_steps=20,
        num_images_per_prompt=4,
        image=image,
        control_image=canny_image,
    ).images
    end_time = datetime.now()
    print(f"[draw_with_prompt] Done drawing. Elapsed time: {end_time - start_time}")

    # 保存图像
    image_paths = []
    random_str = datetime.now().timestamp()
    print(f"[draw_with_prompt] image prefix: {random_str}")
    for i in range(len(images)):
        image = images[i]
        # 结果名称 = image_时间戳_[序列].png
        image_path = f"src/service/result/image_{random_str}_{i}.png"
        image.save(image_path)
        print(f"[draw_with_prompt] Saved image to {image_path}")
        image_paths.append(image_path)

    return image_paths


if __name__ == '__main__':
    draw_with_image()
