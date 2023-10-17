Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "Wstart.bat" & Chr(34), 1 
' 1=Visuable Command Window 0=Hidden || Change if needed.
Set WinScriptHost = Nothing