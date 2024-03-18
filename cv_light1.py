from PIL import Image

# 加载图像
yellow_black_image = Image.open("yellow_black_image.jpeg")
green_black_image = Image.open("green_black_image.jpeg")

# 获取图像尺寸
width1, height1 = yellow_black_image.size
width2, height2 = green_black_image.size

# 确保两张图像的高度相同
max_height = max(height1, height2)
yellow_black_image = yellow_black_image.resize((int(width1 * max_height / height1), max_height))
green_black_image = green_black_image.resize((int(width2 * max_height / height2), max_height))

# 创建一个新的图像，尺寸为两张图像的宽度之和和高度的最大值
combined_image = Image.new("RGB", (yellow_black_image.width + green_black_image.width, max_height))

# 将两张图像粘贴到新图像中
combined_image.paste(yellow_black_image, (0, 0))
combined_image.paste(green_black_image, (yellow_black_image.width, 0))

# 显示图像
combined_image.show()
