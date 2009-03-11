..\bjam toolset=msvc --preserve-test-targets %*
for /r ..\build.tmp %f in (*.pdb) do xcopy /D /Y %f ..\dist\bin
