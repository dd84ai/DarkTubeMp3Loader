echo off
set np="C:\bin"
echo %path%|find /i "%np:"=%">nul  || set path=%path%;%np%
echo on

C:\bin\youtube-dl.exe -i -R 10 --extract-audio --audio-format mp3 --no-playlist %1