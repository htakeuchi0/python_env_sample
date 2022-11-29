@echo off

if "%1"=="" (
  call :init
  call :test
  exit /b
)

if "%1"=="init" (
  call :init
  exit /b
)

if "%1"=="test" (
  call :test
  exit /b
)

if "%1"=="run" (
  call :run
  exit /b
)

if "%1"=="clean" (
  call :clean
  exit /b
)

exit /b

:init
  call .\\scripts\\makeenv.bat>NUL
  call .venv\\Scripts\\pip install --upgrade pip
  call .venv\\Scripts\\pip install -r requirements.txt
  exit /b

:test
  call .\\scripts\\makeenv.bat>NUL 2>&1
  call .venv\\Scripts\\pip install --upgrade pip>NUL 2>&1
  call .venv\\Scripts\\pip install -r requirements.txt>NUL 2>&1
  call .venv\\Scripts\\python -m unittest tests.test_sample
  exit /b

:run
  call .\\scripts\\makeenv.bat>NUL 2>&1
  call .venv\\Scripts\\pip install --upgrade pip>NUL 2>&1
  call .venv\\Scripts\\pip install -r requirements.txt>NUL 2>&1
  call .venv\\Scripts\\python sandbox\\sample.py
  exit /b

:clean
  rmdir /q /s .venv>NUL 2>&1
  del /q activate.bat>NUL 2>&1
  del /q activate_ps.bat>NUL 2>&1
  exit /b

