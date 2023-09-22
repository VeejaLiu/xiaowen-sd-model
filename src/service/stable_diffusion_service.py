import logging
import os
from datetime import datetime

import torch
import torchvision
from diffusers import StableDiffusionPipeline

print(os.get_exec_path())
pipe = StableDiffusionPipeline.from_single_file(
    """src//service//models//v2-1_768-ema-pruned.ckpt""",
    transformers=[
      torchvision.transforms.Resize(512),
    ],
    cache_dir='./models/')
pipe = pipe.to("cuda")


# pipe.enable_attention_slicing()


def draw_with_prompt(prompt="A painting of a cat"):
    print(f"[draw_with_prompt] prompt: '{prompt}'. Start drawing...")
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
