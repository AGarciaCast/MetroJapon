@echo off

cd C:\Users\User\Documents\GitHub\MetroJapon

:inicio
python japonVisual.py

set /p "seguir=Ejecutar otra vez? (s/n)"
if "%seguir%" == "s" ( goto inicio )