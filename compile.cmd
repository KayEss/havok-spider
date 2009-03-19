..\bjam toolset=msvc preserve-test-targets=on %*
for /r ..\build.tmp %%f in (*.pdb) do xcopy /D /Y %%f ..\dist\bin
