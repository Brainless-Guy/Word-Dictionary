@echo off 


set root=%~dp0


pip3 install -r %root%requirements.txt


python3 %root%Word.py
 
pause