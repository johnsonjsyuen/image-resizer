# Image Resizer

This takes a photo and resizes it to specified maximum dimensions, then reduces quality until a specified maximum file size. 

Originally developed for submitting a picture to the Korean K-ETA service.

The Korean K-ETA photo specifications are smaller than 100kb and smaller than 700 by 700 pixels.

## Run on Windows
```
python.exe main.py
```

## Package
```
pyinstaller --onefile main.py
```