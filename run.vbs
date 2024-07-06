Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c Dictionary.bat"
oShell.Run strArgs, 0, False
