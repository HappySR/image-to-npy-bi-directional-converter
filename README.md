# Image to `.npy` Bi-directional Converter

This Python script converts images (including **SVG**) to `.npy` files and vice versa.  

## Features
- Convert **JPEG, PNG, SVG** (and more) to **NumPy (`.npy`)** format.
- Convert `.npy` files back into images.
- Supports **SVG conversion** using `cairosvg`.

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/HappySR/image-to-npy-bi-directional-converter.git

pip install -r requirements.txt
```

### **Dependencies:**
- `numpy`
- `Pillow`
- `cairosvg` (only needed for SVG support)

Install dependencies manually if needed:

```bash
pip install numpy pillow cairosvg
```

## 🛠 Usage  

If you keep your script in the **root directory**, you can run it like this:  

### Convert an Image to `.npy`  
```bash
python image_to_npy_bidirectional.py --mode to_npy --input image.jpg --output image.npy
```

### Convert `.npy` Back to an Image  
```bash
python image_to_npy_bidirectional.py --mode to_image --input image.npy --output output.png
```

### Convert **SVG** to `.npy`  
```bash
python image_to_npy_bidirectional.py --mode to_npy --input image.svg --output image.npy
```

## 📂 Using File Paths  

You can also provide **absolute** or **relative paths** for input and output files.  

### 🔹 **Using Relative Paths**  
(Relative to the script's location)  
```bash
python image_to_npy_bidirectional.py --mode to_npy --input images/sample.jpg --output npy_files/sample.npy
```

```bash
python image_to_npy_bidirectional.py --mode to_image --input npy_files/sample.npy --output output_images/sample.png
```

### 🔹 **Using Absolute Paths**  
(Replace `/path/to/` with the actual directory)  
```bash
python image_to_npy_bidirectional.py --mode to_npy --input /home/user/images/sample.jpg --output /home/user/npy_files/sample.npy
```

```bash
python image_to_npy_bidirectional.py --mode to_image --input /home/user/npy_files/sample.npy --output /home/user/output_images/sample.png
```

## 📝 Notes
- **SVG images** are first converted to **PNG** before saving as `.npy`.
- The script **automatically detects formats** and handles conversions accordingly.

## 🤝 Contributing
Feel free to submit **issues** or **pull requests**!

## 📜 License
This project is licensed under the **MIT License**.

## 🛠 Developed By

💡 Subhajit Roy
🚀 Connect with me: [GitHub](https://github.com/HappySR) | [LinkedIn](www.linkedin.com/in/subhajit-roy-dev)