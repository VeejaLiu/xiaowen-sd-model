from enum import Enum

from src.lib.logger import logger


class TattooStyles(Enum):
    BLACK_WORK = 1
    DOT_WORK = 2
    GEOMETRIC = 3
    WATERCOLOR = 4
    REALISM = 5
    NEO_TRADITIONAL = 6
    NEW_SCHOOL = 7
    JAPANESE = 8
    TRIBAL = 9
    LETTERING = 10
    TRASH_POLKA = 11


async def draw_with_prompt(prompt: str, style: TattooStyles):
    # If style is not specified, use default style
    if style is None or style not in TattooStyles:
        logger.info(f"[draw_with_prompt] Using default style: {TattooStyles.BLACK_WORK}")
        style = TattooStyles.BLACK_WORK

    logger.info(f"[draw_with_prompt] Drawing with prompt: {prompt}, style: {style}")

    # result_paths = []
    #
    # # 上传图片到minio
    # time_string = datetime.now().isoformat()
    # for i in range(0, len(image_names)):
    #     image = image_names[i]
    #     image_path = f"src/service/result/{image}"
    #     # add timestamp to image name
    #     image_object_name = f"{time_string}_{i + 1}_{image}"
    #     result = put_in_minio(image_object_name, image_path)
    #     logger.info(f"[draw] Saved image to {result}")
    #     result_paths.append('http://' + MINIO_URL + result)
    # logger.info(f"[draw] Done drawing.")
    # return result_paths
