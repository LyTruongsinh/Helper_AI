import os
from PIL import Image

# Màu nền cần xóa (R, G, B) - bạn có thể đổi sang màu khác
target_color = (255, 255, 255)  # trắng
tolerance = 30  # Độ lệch màu cho phép

input_folder = 'bullet'
output_folder = 'output_images_color'

os.makedirs(output_folder, exist_ok=True)

def is_similar_color(c1, c2, tolerance):
    return all(abs(a - b) <= tolerance for a, b in zip(c1, c2))

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        new_data = []
        for item in datas:
            r, g, b, a = item
            if is_similar_color((r, g, b), target_color, tolerance):
                new_data.append((r, g, b, 0))  # alpha = 0 => trong suốt
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path)
        print(f"✅ Đã xử lý: {filename}")

print("🎉 Hoàn tất việc xóa màu nền chỉ định!")