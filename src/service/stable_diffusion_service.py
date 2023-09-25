import logging
import os
from datetime import datetime

import torch
import torchvision
from diffusers import StableDiffusionPipeline
from src.client.BaiduTranslator import translate

print(os.get_exec_path())
pipe = StableDiffusionPipeline.from_single_file(
    """src//service//models//v2-1_768-ema-pruned.ckpt""",
    transformers=[
      torchvision.transforms.Resize(512),
    ],
    cache_dir='./models/')
pipe = pipe.to("cuda")


# pipe.enable_attention_slicing()


prefix_prompt = [
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


def draw_with_prompt(prompt: str = ""):
    prompt = prompt.strip()
    if prompt is None or prompt == "":
        print(f"[draw_with_prompt] No prompt provided, return demo image")
        return f"src/service/result/image.jpg"
    print(f"[draw_with_prompt] input prompt: '{prompt}'.")
    prompt = translate(prompt)
    print(f"[draw_with_prompt] translated prompt: '{prompt}'.")
    # prompt = f"{prefix_prompt_str}, ({prompt}:1.6)"
    prompt = f"{prompt}, {prefix_prompt_str}"
    print(f"[draw_with_prompt] Final prompt: '{prompt}'.")
    start_time = datetime.now()
    images = pipe(
        prompt=prompt,
        height=512,
        width=512,
        # num_inference_steps=100,
    ).images
    image = images[0]
    end_time = datetime.now()
    print(f"[draw_with_prompt] Done drawing. Elapsed time: {end_time - start_time}")
    image_path = f"src/service/result/image_{datetime.now().timestamp()}.png"
    # save image, add timestamp
    image.save(image_path)
    print(f"[draw_with_prompt] Saved image to {image_path}")
    return image_path


if __name__ == '__main__':
    draw_with_prompt()
