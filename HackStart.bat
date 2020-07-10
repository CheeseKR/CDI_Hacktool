@echo off
"%CD%\python383\Scripts\pip3.exe" install selenium
copy "%CD%\chromedriver.exe" "C:\Windows\System32\chromedriver.exe"
@echo on
"%CD%\python383\python.exe" "%CD%\hackscript.py"
pause