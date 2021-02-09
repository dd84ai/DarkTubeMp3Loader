@echo off
Setlocal enabledelayedexpansion

Set "Pattern=Fallout Equestria - Project Horizons - "
Set "Replace=FoE_PH_"

For %%# in ("F:\youtube\*.mp3") Do (
    Set "File=%%~nx#"
    Ren "%%#" "!File:%Pattern%=%Replace%!"
)