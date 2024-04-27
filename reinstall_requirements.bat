REM This script installs requirements specified in requirements.txt to the virtual environment.
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt