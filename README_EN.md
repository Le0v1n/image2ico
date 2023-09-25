# 🥰 Generate ICO File Tool

This is a simple tool for converting image files into `.ico` files, with a GUI interface.

## 1. :rocket: Features

- Choose an input image file.
- Convert the image file to a `.ico` file.
- Customize the saving location and name of the `.ico` file.
- View the converted `.ico` file in the destination folder.

## 2. 👀 How to Use

1. Download and run the executable file: [Download Here](https://github.com/Le0v1n/image2ico/releases/tag/ver1.0)

2. Select the image file you want to convert.

3. Click the "Convert to Icon (.ico)" button.

4. Customize the saving location and name of the `.ico` file.

5. If needed, click the "Open File Location" button to view the converted `.ico` file.

## 3. 🐱‍🐉 System Requirements

- Windows operating system
- Python 3.x

## 4. 🐱‍👤 Dependencies

This executable includes all the necessary dependencies, so there's no need to install Python or other libraries separately.

## 5. ✨ Example

![](./image.png)

## 6. 🎁 Self-Building

```bash
pyinstaller --onefile --noconsole --icon generate_icon.ico --name generate-ico-file-ver-1.0 --add-binary "C:\Users\znv\.conda\envs\gui\lib\site-packages\PIL;Pillow" generate_ico.py
```

## 7. :warning: Note

360 Security Guard may flag this program, but you can trust it. If you have concerns, you can inspect the code or build the `.exe` program yourself.

## 8. :e-mail: Contact me

Feel free to contact me if you encounter any bugs or have questions.

+ [Contact me](mailto:zjkljd@163.com)