import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def select_input_image():
    input_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.bmp")])
    input_image_entry.delete(0, tk.END)
    input_image_entry.insert(0, input_image_path)

def convert_to_icon():
    input_image_path = input_image_entry.get()
    
    if not input_image_path:
        result_label.config(text="Author: Le0v1n [ver 1.0]\nContact me: zjkljd@163.com")
        return
    
    try:
        image = Image.open(input_image_path)
        
        # 获取默认的保存位置和文件名
        file_name = os.path.splitext(os.path.basename(input_image_path))[0]
        default_output_path = os.path.join(os.path.expanduser("~"), "Desktop", f"{file_name}.ico")
        
        # 提示用户选择保存位置和文件名
        output_icon_path = filedialog.asksaveasfilename(defaultextension=".ico", initialfile=f"{file_name}.ico", filetypes=[("Icon Files", "*.ico")])
        
        if output_icon_path:
            image.save(output_icon_path, format="ICO")
            result_label.config(text=f"已将图像保存为 {output_icon_path}")
            
            # 显示“打开文件所在位置”按钮
            open_folder_button.pack()
            open_folder_button.config(state=tk.NORMAL, command=lambda: open_output_folder(output_icon_path))
    except Exception as e:
        result_label.config(text=f"转换失败: {str(e)}")

def open_output_folder(output_icon_path):
    output_folder = os.path.dirname(output_icon_path)
    os.startfile(output_folder)  # 使用os.startfile打开文件夹

# 创建主窗口
window = tk.Tk()
window.title("image2ico - a tool to convert image into icon")

# 创建输入图片选择按钮
input_image_label = tk.Label(window, text="Author: Le0v1n [ver 1.0]\nContact me: zjkljd@163.com")
input_image_label.pack()
input_image_entry = tk.Entry(window, width=50)
input_image_entry.pack()
select_input_button = tk.Button(window, text="请选择要转换的图片(.jpg | .png | .bmp)", command=select_input_image)
select_input_button.pack()

# 创建转换按钮
convert_button = tk.Button(window, text="转换为图标(.ico)", command=convert_to_icon)
convert_button.pack()

# 创建“打开文件所在位置”按钮（初始状态隐藏）
open_folder_button = tk.Button(window, text="打开转换后文件所在位置", state=tk.DISABLED)
open_folder_button.pack()

# 显示转换结果
result_label = tk.Label(window, text="")
result_label.pack()

# 启动主循环
window.mainloop()
