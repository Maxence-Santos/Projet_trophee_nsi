import serial
import os
ard = serial.Serial('COM3',timeout=1)
print(ard)
while True:
    if ard.readline != None:
        os.startfile("D:/DOCUMENTS/Python_Scripts/Home/build/exe.win-amd64-3.8/voice_commands.exe")
        os.startfile("C:\\Programmes\\Microsoft VS Code\\Code.exe")
        break 
    else:
        print(str(ard.readline().decode('UTF-8')))
