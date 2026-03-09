@echo off
chcp 65001 >nul
echo ============================================
echo    🎯 南院大王知识库 - 本地服务器
echo ============================================
echo.
echo 正在启动本地服务器...
echo.

python start_server.py

if errorlevel 1 (
    echo.
    echo ❌ 启动失败，请确保已安装Python
    echo    访问 https://www.python.org 下载安装
    echo.
    pause
)
