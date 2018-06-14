# Image2HTML
### Convert your image to HTML code pixel by pixel.


It's a simple script which can convert images (most common formats) into size optimized HTML code. The main objective of this script is to generate **EMAIL CLIENT** friendly HTML that will be displayed by pretty much every client. Therfore I decided to disregard modern HTML practices and focus on size and usability. Resulting HTML code is not intended for web design as it contains outdated/deprecated HTML tags.

#### Setup:

```
git clone https://github.com/WalterMccan/Image2HTML.git
cd Image2HTML
pip install -r requirements.txt
```

#### Usage:
```~# image2HTML.py -i <inputfile> -o <outputfile>```

#### Example:

```~# image2HTML.py -i meme.png -o index.html```

*There are limitations in terms of image dimensions as most email clients have limits as to how many columns they can display. Big Images are truncated or displayed incorrectly (might also load slower). Recommended image size is 100px x 100px.*


**Compatible with Python>=3.6** but can be easly ported to any other version. (Use of f-strings makes it incompatible with previous versions. ```f-strings``` can be replaced with ```.format()```)



##### Twitter: [@WalterMccan](https://twitter.com/WalterMccan)
