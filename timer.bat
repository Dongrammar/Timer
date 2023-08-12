@echo off

REM Pick a random number
set /a rnum=%random%/16383

REM The main program.
D:
cd "D:\Programming\timer"

if %rnum%==0 (
  python timer.py
) else if %rnum% equ 1 (
  python timer_2nd.py
)

pause
