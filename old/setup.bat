set np="C:\bin\ffmpeg\ffmpeg-4.3.2-2021-02-02-full_build\bin\"
echo %path%|find /i "%np:"=%">nul  || set path=%path%;%np%

