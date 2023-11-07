import logging
import os
from datetime import datetime
from compel import Compel

import torch
import torchvision
from diffusers import StableDiffusionPipeline
from diffusers import DPMSolverMultistepScheduler
from diffusers import ControlNetModel

from src.client.BaiduTranslator import translate

print(os.get_exec_path())

# 加载模型
pipe = StableDiffusionPipeline.from_single_file(
    """src//service//models//revAnimated_v122EOL.safetensors""",
    # """src//service//models//v1-5-pruned-emaonly.safetensors""",
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
# pipe.load_lora_weights(
#     # """src//service//models//lora//BLTA2.safetensors""",
#     """src//service//models//lora//b1nk3(0.85-1)CIVIT.safetensors""",
# )
# pipe.fuse_lora(lora_scale=0.9)



def draw_with_prompt_with_lora(prompt: str = "", negative_prompt: str = ""):
    # Prompt预处理，
    prompt = prompt.strip()
    if prompt is None or prompt == "":
        print(f"[draw_with_prompt] No prompt provided, return demo image")
        return f"src/service/result/image.jpg"
    print(f"[draw_with_prompt] input prompt: '{prompt}'.")
    prompt = translate(prompt)
    print(f"[draw_with_prompt] translated prompt: '{prompt}'.")
    # prompt = f"{prefix_prompt_str}, ({prompt}:1.6)"
    # prompt = f"{prompt}, {prefix_prompt_str}".lower()
    prompt = f"{prompt}".lower()
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
    generator = torch.Generator(device="cuda").manual_seed(739703152)

    images = pipe(
        # prompt=prompt,
        # negative_prompt=negative_prompt_str,
        prompt_embeds=prompt_embeds,
        negative_prompt_embeds=negative_prompt_embeds,
        # height=768,
        # width=512,
        generator=generator,
        guidance_scale=7,
        num_inference_steps=50,
        num_images_per_prompt=1,
        # cross_attention_kwargs={"scale": 0.3},
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
    draw_with_prompt_with_lora()
