from src.constant.TattooStyles import TattooStyles

# 通用负面提示词
general_negative_prompt = (
        ""
        f"nsfw, "
        + f"worst quality, low quality, normal quality, lowresolution, low resolution, "
        # + f"poor anatomical structure, poor hand, text, errors, missing fingers, multiple fingers, "
        # + f"few fingers, cropped, worst quality, low quality, normal quality, jpeg artifacts, "
        + f"signature, watermark, username, blurry, exposed, nipple, penis, penis, vagina, anus, "
    # + f"underwear,Breast cleavage, sexy clothing,Not wearing clothes, boobs, Naked chest,"
    # + f"nipple protrusion,expose the body,"
    # + f"paper, painting, pen, pencil"
)

# 画质固定提示词
quality_prompt = (
        "solo, "
        # + "hd, "
        + "no background, "
        + "white background, "
    # + "beautiful pictures, "
    # + "masterpiece"
)


# 处理Prompt - Dot Work, 点刺
def handle_prompt_dot_work(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"dotwork, "  # trigger word
            + f"<lora:dotwork_for_dreamshaper8:1>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 512
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Black Work, 纯黑
def handle_prompt_black_work(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"blackgrey, monochrome, "  # trigger word
            + f"<lora:blackgrey-for-dreamshaper8:0.7>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 512
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Minimalist, 小清新
def handle_prompt_minimalist(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"minimalist, minimal, lineart, "
            # trigger word
            + f"<lora:minimalist-for-dreamshaper8:0.6>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 512
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Geometric, 几何
def handle_prompt_geometric(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"geometric, "  # trigger word
            + f"<lora:geo-5-for-dreamshaper:0.6>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 640
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Old School, 传统美式
def handle_prompt_old_school(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"oldschooltattoo, old school, "  # trigger word
            + f"<lora:oldschool-for-dreamshaper8:0.8>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 640
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - New School, 新学派
def handle_prompt_new_school(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"new school, "  # trigger word
            + f"<lora:ns1-for-dreamshaper:0.8>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 512
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Japanese, 日式
def handle_prompt_japanese(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"japanese, tattoo, japanese pattern, totem, "  # trigger word
            + f"<lora:japanese-tattoo:0.5>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 640
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Realism, 写实
# TODO 暂时不需要LoRA模型，只用Prompt的效果就可以了
def handle_prompt_realism(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"realistic, detailed, design, realism, monochrome, lineart, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 512
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Trash Polka, 垃圾波尔卡
def handle_prompt_trash_polka(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"tp, blood, ink, "
            + f"<lora:tp3-for-dreamshaper:0.7>, "
            + f"{quality_prompt}"
    )
    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 512
    width = 512
    return {
        "positive_prompt": positive_prompt,
        "negative_prompt": negative_prompt,
        "height": height,
        "width": width
    }


# 处理Prompt - Tribal, 图腾
def handle_prompt_tribal(prompt):
    # 正向提示词
    positive_prompt = (
            f"{prompt}, "
            + f"tribal, "
            + f"<lora:tribal-1-for-dreamshaper-000018:0.7>, "
            + f"{quality_prompt}")

    # 负向提示词
    negative_prompt = general_negative_prompt
    height = 512
    width = 512

    return {
        'positive_prompt': positive_prompt,
        'negative_prompt': negative_prompt,
        'height': height,
        'width': width
    }


prompt_style_switch = {
    # TattooStyles.NONE: handle_prompt_none,  # 0
    TattooStyles.DOT_WORK: handle_prompt_dot_work,  # 1, 点刺
    TattooStyles.BLACK_WORK: handle_prompt_black_work,  # 2, 纯黑
    TattooStyles.MINIMALIST: handle_prompt_minimalist,  # 3, 小清新
    TattooStyles.GEOMETRIC: handle_prompt_geometric,  # 4, 几何
    TattooStyles.OLD_SCHOOL: handle_prompt_old_school,  # 5, 传统美式
    TattooStyles.NEW_SCHOOL: handle_prompt_new_school,  # 6, 新学派
    TattooStyles.JAPANESE: handle_prompt_japanese,  # 7, 日式
    TattooStyles.REALISM: handle_prompt_realism,  # 8, 写实
    TattooStyles.TRASH_POLKA: handle_prompt_trash_polka,  # 9, 垃圾波尔卡
    TattooStyles.TRIBAL: handle_prompt_tribal,  # 10, 部落
}


# 处理Prompt
def handle_prompt(style: TattooStyles, prompt: str):
    # switch style
    return prompt_style_switch[style](prompt)
