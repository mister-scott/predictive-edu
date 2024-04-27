REM This script deletes and reinstalls the virtual environment and dependencies specified in requirements.txt
rmdir /S /Q venv
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt