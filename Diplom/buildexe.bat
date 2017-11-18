@echo off
cls
set pyinstPath=C:\Program Files\Python36\Lib\site-packages\PyInstaller
set buildPath=%pyinstPath%\bin
set moveBin=0
set fileParam=0
:ParamChk
if "%1%"=="" goto binBuild
goto p%1
:p-F
:p/F
:p/file
:p--file
if not "%2"=="" (
set pyFile=%2
if not %fileParam%==1 set fileParam=1
)
shift & shift & goto ParamChk
 
:p-O
:p/O
:p/out
:p--out
if not "%2"=="" set buildPath=%2
shift & shift & goto ParamChk
 
:p-M
:p/M
:p/move
:p--move
set moveBin=1
shift & goto ParamChk
 
:p-H
:p/H
:p/help
:p--help
echo.
echo Use: %~n0 [/F [path]filename] [/O dir] [/M]
echo.
echo /F, -F, /file, --file - Path to .py file 
echo /O, -O, /out, --out - Output directory. Default directory - %buildPath%
echo /M, -M, /move, --move - Move created binary to .py file directory
goto :EOF
:binBuild
if %fileParam%==0 echo No file to work with. Use /h for help & goto :EOF
set specParams=-o %buildPath%
"%pyinstPath%\MakeSpec.py" %specParams% "%pyFile%"
for %%i in (%pyFile%) do (set fileName=%%~ni)
%pyinstPath%\Build.py "%buildPath%\%fileName%.spec"
if %moveBin%==1 (
for %%i in (%pyFile%) do (set outDir=%%~pi)
move /y "%buildPath%\dist\%fileName%.exe" %outDir%
)