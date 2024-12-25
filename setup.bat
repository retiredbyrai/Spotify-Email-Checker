@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Creating start.bat to run the application...
echo @echo off > start.bat
echo python account_validator.py >> start.bat

echo Installation complete! You can now run the application using start.bat.
pause
