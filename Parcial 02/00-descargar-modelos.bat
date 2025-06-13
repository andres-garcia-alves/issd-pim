@echo off

rem Crear la carpeta models si no existe
if not exist ".\models\" mkdir ".\models\"

echo.
echo Descargando modelos...

echo.
echo - Familia EDSR:

echo   Descargando EDSR_x2.pb...
curl -sS -L -o "./models/EDSR_x2.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/EDSR/EDSR_x2.pb"

echo   Descargando EDSR_x3.pb...
curl -sS -L -o "./models/EDSR_x3.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/EDSR/EDSR_x3.pb"

echo   Descargando EDSR_x4.pb...
curl -sS -L -o "./models/EDSR_x4.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/EDSR/EDSR_x4.pb"

echo.
echo - Familia ESPCN:

echo   Descargando ESPCN_x2.pb...
curl -sS -L -o "./models/ESPCN_x2.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/ESPCN/ESPCN_x2.pb"

echo   Descargando ESPCN_x3.pb...
curl -sS -L -o "./models/ESPCN_x3.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/ESPCN/ESPCN_x3.pb"

echo   Descargando ESPCN_x4.pb...
curl -sS -L -o "./models/ESPCN_x4.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/ESPCN/ESPCN_x4.pb"

echo.
echo - Familia FSRCNN:

echo   Descargando FSRCNN-small_x2.pb...
curl -sS -L -o "./models/FSRCNN-small_x2.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/FSRCNN/FSRCNN-small_x2.pb"

echo   Descargando FSRCNN-small_x3.pb...
curl -sS -L -o "./models/FSRCNN-small_x3.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/FSRCNN/FSRCNN-small_x3.pb"

echo   Descargando FSRCNN-small_x4.pb...
curl -sS -L -o "./models/FSRCNN-small_x4.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/FSRCNN/FSRCNN-small_x4.pb"

echo   Descargando FSRCNN_x2.pb...
curl -sS -L -o "./models/FSRCNN_x2.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/FSRCNN/FSRCNN_x2.pb"

echo   Descargando FSRCNN_x3.pb...
curl -sS -L -o "./models/FSRCNN_x3.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/FSRCNN/FSRCNN_x3.pb"

echo   Descargando FSRCNN_x4.pb...
curl -sS -L -o "./models/FSRCNN_x4.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/FSRCNN/FSRCNN_x4.pb"

echo.
echo - Familia LapSRN:

echo   Descargando LapSRN_x2.pb...
curl -sS -L -o "./models/LapSRN_x2.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/LapSRN/LapSRN_x2.pb"

echo   Descargando LapSRN_x4.pb...
curl -sS -L -o "./models/LapSRN_x4.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/LapSRN/LapSRN_x4.pb"

echo   Descargando LapSRN_x8.pb...
curl -sS -L -o "./models/LapSRN_x8.pb" "https://github.com/MGunturG/implementation-dnn-sr/raw/refs/heads/main/models/LapSRN/LapSRN_x8.pb"

echo.
echo Descarga finalizada.
pause
