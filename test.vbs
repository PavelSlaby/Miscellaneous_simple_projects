a = msgbox("!Hola",0 , "This be the Header")

'creates and shell object

Set oShell = WScript.CreateObject("WScript.Shell")

'uses shell to open a file and waits so that it opens properly


oShell.run """C:\Users\Pavel\Desktop\test.pdf"""
WScript.Sleep 4000

oShell.SendKeys "^a"
WScript.Sleep 1000
oShell.SendKeys "^c"
WScript.Sleep 1000


oShell.run """C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2205.11.0_x64__8wekyb3d8bbwe\Notepad\Notepad"""

WScript.Sleep 2000

oShell.SendKeys "^v"
WScript.Sleep 2000
oShell.SendKeys "^s"
WScript.Sleep 2000
oShell.SendKeys "test.txt"
WScript.Sleep 2000
oShell.SendKeys "{ENTER}"








