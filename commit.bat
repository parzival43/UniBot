@echo off
cd C:/User*/j*/O*/De*/Y*/Proj*/U*
git add .
set /p input= Commit Message? 
git commit -m "%input%"
git push origin main