linux:
```bash
sudo apt install tesseract-ocr
```

MacOS:
```bash
brew install tesseract
```

MacOS:
```bash
brew install tesseract
```

Windows:
```bash
https://github.com/UB-Mannheim/tesseract/wiki
```

# how to compile
Create the virtual environment:
```bash
python -m venv venv
```

Install requirements:
```bash
pip install -r requirements.txt
```

Compile the app:
```bash
pyinstaller --onefile -n image_reader main.py
```

Get the app in ./dist image_reader

REMEMBER THAT YOU NEED TO HAVE A IMAGE IN YOUR TRANSFER AREA AND THE RESULT IS THE TEXT OF THE IMAGE IN YOUR TRANSFER AREA!
