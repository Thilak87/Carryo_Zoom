@echo off
title Carryo Zoom - Public Internet Tunnel
cd /d "%~dp0"
echo ========================================================
echo   Launching Public Internet Tunnel for Carryo Zoom
echo ========================================================
echo.
echo Connecting your local server (port 7000) to the secure internet...
echo Look for the link ending in .trycloudflare.com below!
echo Anyone on 4G, 5G, or any Wi-Fi in the world can open that link.
echo.
echo Press Ctrl+C anytime to stop sharing.
echo ========================================================
echo.
cloudflared.exe tunnel --url http://localhost:7000
pause
