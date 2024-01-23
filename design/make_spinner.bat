@echo off
setlocal enabledelayedexpansion

set "input_dir=spinner"
set "output_dir=spinner_renamed"
set "counter=49"

:: Create the output directory if it doesn't exist
if not exist "%output_dir%" mkdir "%output_dir%"

for /R "%input_dir%" %%I in (*.png) do (
    set /A counter+=1
    copy /Y "%%~fI" "%output_dir%/spinner!counter!.png"
)

endlocal

ffmpeg -y -start_number 51 -i spinner_renamed/spinner%%d.png -vf palettegen=reserve_transparent=1 palette.png
ffmpeg -y -start_number 51 -framerate 30 -i spinner_renamed/spinner%%d.png -i palette.png -lavfi paletteuse=alpha_threshold=128 -gifflags -offsetting spinner.gif