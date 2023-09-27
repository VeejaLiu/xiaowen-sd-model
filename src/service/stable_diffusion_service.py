import logging
import os
from datetime import datetime
from compel import Compel

import torch
import torchvision
from diffusers import StableDiffusionPipeline
from diffusers import DPMSolverMultistepScheduler

from src.client.BaiduTranslator import translate

print(os.get_exec_path())

# 加载模型
pipe = StableDiffusionPipeline.from_single_file(
    # """src//service//models//v2-1_768-ema-pruned.ckpt""",
    """src//service//models//v1-5-pruned-emaonly.safetensors""",
    # """src//service//models//ghostmix_v20Bakedvae.safetensors""",
    # transformers=[
    #     torchvision.transforms.Resize(512),
    # ],
    # torch_dtype=torch.float16,
    load_safety_checker=None,
    # use_safetensors=False,
    cache_dir='./models/')

# 设置采样方法
pipe.scheduler = DPMSolverMultistepScheduler.from_config(
    pipe.scheduler.config
)

# 使用Compel来处理文本，将文本转换为模型可以理解的张量
compel = Compel(tokenizer=pipe.tokenizer, text_encoder=pipe.text_encoder)

pipe = pipe.to("cuda")

prefix_prompt = [
    'masterpiece, top quality, best quality',
    'Black and white tattoo design',
    'Monochromatic tattoo concept',
    'Tattoo stencil idea',
    'Ink-only tattoo sketch',
    'Clean and crisp tattoo outline',
    'Minimalistic tattoo artwork',
    'Geometric tattoo pattern',
    'Abstract tattoo proposal',
    'Sharp and defined tattoo image',
    'Bold tattoo design',
    'Intricate linework for tattoo',
    'Symmetrical tattoo draft',
    'Tribal tattoo inspiration',
    'Japanese-style tattoo concept',
    'Celtic knotwork tattoo idea',
    'Tattoo with no gradients',
    'High contrast tattoo sketch',
    'Fine details in tattoo design',
    'Line art for tattoo',
    'Two-dimensional tattoo concept'
]

prefix_prompt_str = ", ".join(prefix_prompt)


# negative_prompt = [
#     'Colorful tattoo design',
# ]

# negative_prompt_str = ", ".join(negative_prompt)


def draw_with_prompt(prompt: str = "", negative_prompt: str = ""):
    # Prompt预处理，
    prompt = prompt.strip()
    if prompt is None or prompt == "":
        print(f"[draw_with_prompt] No prompt provided, return demo image")
        return f"src/service/result/image.jpg"
    print(f"[draw_with_prompt] input prompt: '{prompt}'.")
    prompt = translate(prompt)
    print(f"[draw_with_prompt] translated prompt: '{prompt}'.")
    # prompt = f"{prefix_prompt_str}, ({prompt}:1.6)"
    prompt = f"{prompt}, {prefix_prompt_str}".lower()
    print(f"[draw_with_prompt] Final prompt: '{prompt}'.")
    print(f"[draw_with_prompt] Final prompt length: {len(prompt)}")
    print(f"[draw_with_prompt] Final prompt tokens length: {len(prompt.split(' '))}")
    print(f"[draw_with_prompt] Final negative prompt: '{negative_prompt}'.")
    print(f"[draw_with_prompt] Final negative prompt length: {len(negative_prompt)}")
    print(f"[draw_with_prompt] Final negative prompt tokens length: {len(negative_prompt.split(' '))}")

    # 将文本转换为张量，便于输入长文本
    prompt_embeds = compel(prompt)
    negative_prompt_embeds = compel(negative_prompt)

    start_time = datetime.now()

    # generator 的作用是控制生成过程的随机性
    generator = torch.Generator(device="cuda").manual_seed(8)

    # prompt: 输入的文本提示,控制生成图像的主题和内容。
    # height: 生成图像的高度大小。
    # width: 生成图像的宽度大小。设置height和width可以控制输出图像的尺寸。
    # num_inference_steps: 生成图像的迭代次数,越大图像会越精细清晰,但耗时也更长。通常50步已经足够好。
    # guidance_scale: 控制生成图像时引导损失的影响力量。数值越大,图像会越趋近于prompt指定的样式,但写实程度可能降低。
    # negative_prompt: 介绍负面prompt来减弱某些不希望出现的特征。
    # num_images_per_prompt: 每个prompt生成的图像数量。
    # eta:控制先验噪声和输入文本特征的融合比例。
    # generator:Torch随机数生成器,控制生成过程的随机性。
    # latents:提供噪声输入来引导生成。
    # prompt_embeds:将prompt嵌入为张量,提供给模型。
    # negative_prompt_embeds:将负面prompt嵌入为张量。
    # output_type:输出图像的格式,如PIL或者ndarray。
    # return_dict:是否以字典形式返回额外信息。
    # callback:每次迭代的回调函数,用于实时监控生成过程。
    # callback_steps:设置回调函数调用间隔。
    # cross_attention_kwargs:控制交叉注意力机制的超参数。
    # guidance_rescale:重新缩放损失函数以控制稳定性。
    images = pipe(
        # prompt=prompt,
        # negative_prompt=negative_prompt_str,
        prompt_embeds=prompt_embeds,
        negative_prompt_embeds=negative_prompt_embeds,
        # height=768,
        # width=512,
        # generator=generator,
        guidance_scale=7,
        num_inference_steps=30,
        num_images_per_prompt=4,
    ).images
    end_time = datetime.now()
    print(f"[draw_with_prompt] Done drawing. Elapsed time: {end_time - start_time}")

    # 保存图像
    image_paths = []
    random_str = datetime.now().timestamp()
    print(f"[draw_with_prompt] image prefix: {random_str}")
    for i in range(len(images)):
        image = images[i]
        # 结果名称 = image_时间戳.png
        image_path = f"src/service/result/image_{random_str}_{i}.png"
        image.save(image_path)
        print(f"[draw_with_prompt] Saved image to {image_path}")
        image_paths.append(image_path)

    return image_paths


if __name__ == '__main__':
    draw_with_prompt()
