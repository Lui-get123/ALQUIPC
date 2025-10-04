@echo off
echo ================================================
echo    ALQUIPC - Compilador a Archivo .EXE
echo ================================================
echo.

echo Instalando auto-py-to-exe...
pip install auto-py-to-exe

echo.
echo Iniciando compilador grafico...
echo Seleccione el archivo: alquipc_facturacion.py
echo Marque: One File
echo Marque: Window Based (hide the console)
echo Presione: CONVERT .PY TO .EXE
echo.

auto-py-to-exe

echo.
echo ¡Proceso completado!
echo El archivo .exe estara en la carpeta output/
echo.
pause
