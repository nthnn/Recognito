<p align="center">
	<img src="assets/recognito.png" width="120" />
</p>

# Recognito: Image Object Recognition

Recognito is a Python program that utilizes the power of PyQT5 and TensorFlow to provide a user-friendly interface for identifying objects in local image files. With Recognito, you can effortlessly browse for your favorite JPG, JPEG, or PNG images and discover what objects are present within them.

## Features

-   **Intuitive User Interface:** Recognito offers a sleek and user-friendly interface, allowing even beginners to navigate and utilize its functionalities with ease.
    
-   **Local Image Selection:** You can conveniently browse your computer to select the image file you want to analyze. Recognito supports popular formats like JPG, JPEG, and PNG.
    
-   **Object Recognition:** Powered by TensorFlow, Recognito employs state-of-the-art deep learning models to accurately identify and classify objects within the selected image. Gain valuable insights into the contents of your images effortlessly.
    
-   **Detailed Results:** The program provides detailed results, displaying the identified objects along with their corresponding confidence scores. Stay informed about the accuracy of the recognition process.

## Installation

1. Clone the Recognito repository.
```batch
git clone 
```
2. Install Python 3 from [python.org](https://www.python.org/downloads/).
3. Run the [module_installer.bat](scripts/module_installer.bat).
4. You can now either run the [main](__main__.pyw) script of the Recognito or build with [pyinstaller](C:\Users\natha\Desktop\Recognito) by running [build_installer.bat](scripts/build_installer.bat).
5. Finally, you can now clean files after building with [clean_build.bat](scripts/clean_build.bat).

## Usage

1.  Upon launching Recognito, you will be greeted with a user-friendly interface.
2.  Click on the "Browse" button to select the image file you want to analyze.
3.  Once the image is loaded, click on the "Identify" button to initiate the recognition process.
4.  After a brief moment, Recognito will display the identified objects.
5.  You can repeat the process by clicking on the "Browse" button again and selecting a new image file.

## License

Copyright 2023 - Nathanne Isip

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

```THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.```