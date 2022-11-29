@echo off

set env_path=.\\
set env_name=.venv

set py_cmd=python
set venv_py_cmd=%env_path%\\Scripts\\python.exe
set venv_pip_cmd=%env_path%\\Scripts\\pip.exe

echo # Make new python environment: %env_name%
echo.

if not exist %env_path%%env_name% (
  %py_cmd% -m venv %env_path%%env_name%
)

if not exist activate.bat (
  echo @echo off>activate.bat
  echo %%~dp0%env_path%%env_name%\\Scripts\\activate.bat>>activate.bat
)

if not exist activate_ps.bat (
  echo @echo off>activate_ps.bat
  echo powershell -NoExit -File %%~dp0%env_path%%env_name%\\Scripts\\Activate.ps1>>activate_ps.bat
)

echo done.
echo.
echo #
echo # To activate the %env_name% environment:
echo # ^> activate.bat    ^(Command Prompt^)
echo # or ^> activate_ps.bat ^(Windows PowerShell^)
echo #
echo # To install packages:
echo # ^> activate.bat    ^(Command Prompt^)
echo # or ^> activate_ps.bat ^(Windows PowerShell^)
echo # ^(%env_name%^) ^> pip install -r requirements.txt
echo #
