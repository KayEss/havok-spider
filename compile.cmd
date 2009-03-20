..\bjam toolset=msvc preserve-test-targets=on %*
@echo off
IF NOT ERRORLEVEL 1 (
    for /r ..\build.tmp %%f in (*.pdb) do xcopy /D /Y %%f ..\dist\bin
)
