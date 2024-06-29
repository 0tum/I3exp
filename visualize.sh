#!/bin/bash

# 音楽ファイルの再生
sox -q "$1" -d &

# Pythonスクリプトの実行
python3 visualizer.py "$1"
