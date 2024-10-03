@echo off
cd C:/User*/j*/O*/De*/Y*/Proj*/UniBot
git add .
set /p input= Commit Message? 
git commit -m "%input%"
git push origin master