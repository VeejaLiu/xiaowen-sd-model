from src.constant.TattooStyles import TattooStyles

# 纹身固定提示词
tattoo_prompt = ("(tattoo_design:1.2), "
                 "tattoo proposal, "
                 "tattoo artwork, "
                 "Clean and crisp tattoo outline, "
                 "Tattoo stencil, "
                 "tattoo concept")

# 画质固定提示词
quality_prompt = ("hd,"
                  "8k",
                  "white background",
                  "beautiful pictures",
                  "masterpiece")


# 处理Prompt - Dot Work, 点刺
# 这种风格的纹身通常是由特别多的点来设计和构成，通过点的密集程度来表现深浅和过度，基本上所有的题材都能用这种方式来表达。
def handle_prompt_dot_work(prompt):
    # Dot Work, 点刺
    return (f"{prompt}, "
            # f"{tattoo_prompt}"
            f"<lora:dotwork_sd15:1>, "
            f"dotwork, solo, simple background, white background, "
            # f"{quality_prompt}"
            )


# 处理Prompt - Black Work, 纯黑
# 这种风格只有一种颜色：纯粹的黑。通常是大面积的黑色或者纯黑色线条的图案。
def handle_prompt_black_work(prompt):
    # Black Work, 纯黑
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"shadow, black, line thickness, black and gray tones, dark, geometric, abstract, solid, tattoo, "
            f"{quality_prompt}")


# 处理Prompt - Minimalist, 小清新
# 这种风格的纹身通常以简洁的线条和轮廓为主，类似于手绘的草图或速写。它强调线条的流畅和简洁，通常没有过多的细节或阴影。
def handle_prompt_minimalist(prompt):
    # Minimalist, 小清新
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"simple, clean, minimalist, line, line art, tattoo, sketch, "
            f"{quality_prompt}")


# 处理Prompt - Geometric, 几何
# 几何纹身就是利用线条和图形构成。极简主义却又充满个性，利用直线曲线和棱角的巧妙结合，可以带给人一种独特的优雅感觉。
def handle_prompt_geometric(prompt):
    # Geometric, 几何
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"geometric shapes, straight lines, symmetry, polygons, triangles, circles, squares, tattoo, abstract, "
            f"color blocks, patterns, {quality_prompt}")


# 处理Prompt - Old School, 传统美式
# 传统美式纹身是最古老的纹身风格之一，它的特点是色彩鲜艳，线条粗犷，图案简单，通常是一些动物、花朵、心形、刀剑、锚等等。
# 这种风格是“最像纹身的纹身”，是相对比较流行的一种风格。这种风格有很实在的轮廓线，很少的颜色变化和过度以及很少的细节。这种纹身都很简单，但是普遍会被认为：相对其他风格的纹身，这种纹身会更经久不衰。
def handle_prompt_old_school(prompt):
    # Neo Traditional, 新传统
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"traditional, old school, classic, Timeless Charm, Bold Lines, Simplified Strength, Recognizable Imagery, Solid Outlines, Vivid Resilience, Classic Endurance"
            f"{quality_prompt}")


# 处理Prompt - New School, 新学派
# 相对于老传统，新传统颜色稍微多一点，颜色变化也稍微多一点，不过也具有老传统的“卡通”风格。这算是一种试验风格的纹身，既遵循了老传统的一些东西，又多了一些不同的改变。
def handle_prompt_new_school(prompt):
    # New School, 新学派
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"exaggerated, cartoonish, vibrant, bright, fun, colorful, tattoo, patterns, "
            f"creative, traditional, vibrant, full, shadow, tattoo, rich colors, line thickness, patterns, "
            f"{quality_prompt}")


# 处理Prompt - Japanese, 日式
# 日式纹身的历史可以追溯到公元前5000年，因此这种风格的特点是非常鲜明的。这种风格的细节特别多，有特别考究的一套图案绘制方式，每个日式纹身都是一个复杂的艺术品。日式纹身通常会覆盖全身、整个背部或者四肢。
def handle_prompt_japanese(prompt):
    # Japanese, 日式
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"Traditional Essence: Rooted in traditional Japanese art, showcasing unique symbols and patterns inspired by the country's cultural and philosophical heritage."
            f"Intricate Details: Emphasis on meticulous details, with each line and color carefully designed to demonstrate a high level of skill."
            f"Fluid Naturalism: Prioritizing the harmonious integration of the tattoo with the body, seeking natural and fluid lines that make the tattoo appear as if it's growing on the skin."
            f"Rich Palette: Utilizes a diverse color palette, including classic red, black, blue, and metallic tones, injecting vibrant artistic atmospheres into the tattoos."
            f"Traditional Themes: Often draws inspiration from Japanese mythology, natural elements, and the samurai of the Warring States period, reflecting deep traditional cultural significance."
            f"Symbolic Meaning: Each design carries symbolic significance, representing qualities such as courage, endurance, and resilience, transforming tattoos into expressions of life philosophy."
            f"Unique Techniques: Incorporates unique traditional techniques like irezumi (tattooing), using traditional tools, highlighting the individuality and skills of the artist."
            f"Overall Balance: Emphasizes overall balance, seeking harmony not only within individual designs but also in the cohesive coordination and aesthetic appeal of multiple tattoos."
            f"Enriched Cultural Elements: Infuses a variety of cultural elements from Japanese literature, painting, and drama, turning tattoos into extensions and expressions of culture."
            f"Longevity and Durability: Prioritizes the durability of tattoos, employing high-quality pigments and techniques to ensure longevity and vibrant clarity over time."
            f"{quality_prompt}")


# 处理Prompt - Anime, 动漫
# 动漫纹身是一种受到日本动漫文化启发的纹身艺术。它通常包括以动漫角色、动漫场景或动漫元素为主题的纹身设计。
def handle_prompt_anime(prompt):
    # Anime, 动漫
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"anime, cartoon, manga, tattoo, "
            f"{quality_prompt}")


# 处理Prompt - Realism, 写实
# 写实纹身是一种以真实主义风格表现图像的纹身艺术。它追求逼真的细节和精确的描绘，以再现现实世界中的人物、动物、植物或物体等。
def handle_prompt_realism(prompt):
    # Realism, 写实
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"realistic, detailed, shadow, light and shadow, portraits, nature, tattoo, "
            f"{quality_prompt}")


# 处理Prompt - Surrealism, 超现实
# 风格名字就能很好地表达内容了：非现实的纹身。可能会使用带条纹的颜色、不寻常的形状来表现这个图形，使之具有很独特的艺术感。
def handle_prompt_surrealism(prompt):
    # Surrealism, 超现实
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"surrealism, dreamlike, dream, "
            f"{quality_prompt}")


# 处理Prompt - Tribal, 部落
def handle_prompt_tribal(prompt):
    # Tribal, 部落
    return (f"{prompt}, "
            f"{tattoo_prompt}"
            f"primitive, traditional, geometric, black, rugged, tattoo, ancient, symbols, totems, strength, courage, "
            f"{quality_prompt}")


prompt_style_switch = {
    # TattooStyles.NONE: handle_prompt_none,  # 0
    TattooStyles.DOT_WORK: handle_prompt_dot_work,  # 1, 点刺
    TattooStyles.BLACK_WORK: handle_prompt_black_work,  # 2, 纯黑
    TattooStyles.MINIMALIST: handle_prompt_minimalist,  # 3, 小清新
    TattooStyles.GEOMETRIC: handle_prompt_geometric,  # 4, 几何
    TattooStyles.OLD_SCHOOL: handle_prompt_old_school,  # 5, 传统美式
    TattooStyles.NEW_SCHOOL: handle_prompt_new_school,  # 6, 新学派
    TattooStyles.JAPANESE: handle_prompt_japanese,  # 7, 日式
    TattooStyles.ANIME: handle_prompt_anime,  # 8, 动漫
    TattooStyles.REALISM: handle_prompt_realism,  # 9, 写实
    TattooStyles.SURREALISM: handle_prompt_surrealism,  # 10, 超现实
    TattooStyles.TRIBAL: handle_prompt_tribal,  # 11, 部落
}


# 处理Prompt
def handle_prompt(style: TattooStyles, prompt: str):
    # switch style
    new_prompt = prompt_style_switch[style](prompt)
    return new_prompt
    pass
