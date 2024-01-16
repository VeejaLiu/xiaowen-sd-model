from PIL import Image
import os


def binarize_image(input_folder, output_folder, threshold=128):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有图片文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 打开图片
            img = Image.open(input_path)

            # 将图片二值化
            img = img.convert('L')  # 转换为灰度图
            img = img.point(lambda p: p > threshold and 255)  # 设置低于阈值的像素为白色

            # 保存处理后的图片
            img.save(output_path)

            print(f"Processed: {filename}")


if __name__ == "__main__":
    # 输入文件夹路径
    input_folder_path = ""
    # 输出文件夹路径
    output_folder_path = ""

    # 阈值设置
    threshold_value = 150

    # 执行二值化操作
    binarize_image(input_folder_path, output_folder_path, threshold_value)
