from src.constant.TattooStyles import TattooStyles


# 处理Prompt - None, 无
def handle_prompt_none(prompt):
    # None, 无
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Black Work, 黑线
def handle_prompt_black_work(prompt):
    # Black Work, 黑线
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"shadow, black, line thickness, black and gray tones, dark, geometric, abstract, solid, tattoo, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Dot Work, 点刺
def handle_prompt_dot_work(prompt):
    # Dot Work, 点刺
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"dot, dotwork, detail, tattoo, black and white, abstract, gradient, grayscale, shadow, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Geometric, 几何
def handle_prompt_geometric(prompt):
    # Geometric, 几何
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"geometric shapes, straight lines, symmetry, polygons, triangles, circles, squares, tattoo, abstract, "
            f"color blocks, patterns, hd, 8k, white background, beautiful pictures")


# 处理Prompt - Watercolor, 水彩
def handle_prompt_watercolor(prompt):
    # Watercolor, 水彩
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"watercolor, soft, flowing, transparent, color gradients, blending, detail, unique, art, tattoo, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Realism, 写实
def handle_prompt_realism(prompt):
    # Realism, 写实
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"realistic, detailed, shadow, light and shadow, portraits, animals, flowers, nature, tattoo, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Neo Traditional, 新传统
def handle_prompt_neo_traditional(prompt):
    # Neo Traditional, 新传统
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"traditional, vibrant, full, shadow, tattoo, rich colors, line thickness, patterns, animals, plants, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - New School, 新学派
def handle_prompt_new_school(prompt):
    # New School, 新学派
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"exaggerated, cartoonish, vibrant, bright, fun, colorful, tattoo, patterns, creative, animals, plants, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Japanese, 日式
def handle_prompt_japanese(prompt):
    # Japanese, 日式
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"traditional Japanese, ukiyo-e, fish, dragon, flowers, clouds, waves, wind, tattoo, shadow, texture, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Tribal, 部落
def handle_prompt_tribal(prompt):
    # Tribal, 部落
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"primitive, traditional, geometric, black, rugged, tattoo, ancient, symbols, totems, strength, courage, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Lettering, 字母
def handle_prompt_lettering(prompt):
    # Lettering, 字母
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"text, lettering, calligraphy, handwritten, decorative, tattoo, font styles, personality, quotes, references, "
            f"hd, 8k, white background, beautiful pictures")


# 处理Prompt - Trash Polka, 垃圾波尔卡
def handle_prompt_trash_polka(prompt):
    # Trash Polka, 垃圾波尔卡
    return (f"{prompt}, "
            f"(tattoo_design:1.2), "
            f"chaotic, graffiti, imagery, broken, abstract, fragmented, meaning, "
            f"hd, 8k, white background, beautiful pictures")


prompt_style_switch = {
    TattooStyles.NONE: handle_prompt_none,  # 0
    TattooStyles.BLACK_WORK: handle_prompt_black_work,  # 1
    TattooStyles.DOT_WORK: handle_prompt_dot_work,  # 2
    TattooStyles.GEOMETRIC: handle_prompt_geometric,  # 3
    TattooStyles.WATERCOLOR: handle_prompt_watercolor,  # 4
    TattooStyles.REALISM: handle_prompt_realism,  # 5
    TattooStyles.NEO_TRADITIONAL: handle_prompt_neo_traditional,  # 6
    TattooStyles.NEW_SCHOOL: handle_prompt_new_school,  # 7
    TattooStyles.JAPANESE: handle_prompt_japanese,  # 8
    TattooStyles.TRIBAL: handle_prompt_tribal,  # 9
    TattooStyles.LETTERING: handle_prompt_lettering,  # 10
    TattooStyles.TRASH_POLKA: handle_prompt_trash_polka,  # 11
}


# 处理Prompt
def handle_prompt(style: TattooStyles, prompt: str):
    # switch style
    new_prompt = prompt_style_switch[style](prompt)
    return new_prompt
    pass
