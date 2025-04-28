

import os
from PIL import Image

# Đường dẫn thư mục chứa ảnh gốc và thư mục lưu ảnh đã thu nhỏ
input_folder = 'Laser_Sprites'
output_folder = 'Output_Laser_Sprites'

# Kích thước thu nhỏ mong muốn
target_size = (64,64)  # (width, height)

# Tạo thư mục đầu ra nếu chưa tồn tại
os.makedirs(output_folder, exist_ok=True)

# Duyệt qua các ảnh trong thư mục
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        img = Image.open(input_path)

        # Resize ảnh về kích thước cố định
        resized_img = img.resize(target_size, Image.Resampling.LANCZOS)

        # Lưu ảnh mới vào thư mục đích
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)
        print(f"✅ Đã thu nhỏ: {filename}")

print("🎉 Hoàn tất thu nhỏ tất cả ảnh!")

