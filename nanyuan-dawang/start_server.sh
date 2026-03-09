#!/bin/bash

echo "============================================"
echo "   🎯 南院大王知识库 - 本地服务器"
echo "============================================"
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ 未找到Python，请先安装Python 3"
        echo "   macOS: brew install python3"
        echo "   Linux: sudo apt-get install python3"
        exit 1
    else
        PYTHON=python
    fi
else
    PYTHON=python3
fi

echo "正在启动本地服务器..."
echo ""

$PYTHON start_server.py
