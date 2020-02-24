set original_dir=%CD%
set venv_root_dir="C:\Users\Roman\PycharmProjects\beautymarketAds"
cd %venv_root_dir%
call %venv_root_dir%\venv\Scripts\activate.bat

python google_sheets.py

call %venv_root_dir%\venv\Scripts\deactivate.bat
cd %original_dir%
exit


