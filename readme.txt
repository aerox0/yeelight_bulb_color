# How to use and build project

1. Create python environment (python -m venv venv)
2. Install all requirements (pip install -r requirements.txt)
3. Install pyinstaller lib (pip install pyinstaller)
4. Build to .exe (pyinstaller -F -c --path venv\Lib\site-packages -n yeelight.exe main.py)