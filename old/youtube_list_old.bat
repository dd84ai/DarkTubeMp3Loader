C:\bin\youtube-dl.exe -i -f bestaudio --yes-playlist %1 --exec "C:\bin\ffmpeg\ffmpeg-4.3.2-2021-02-02-full_build\bin\ffmpeg.exe -i {}  -codec:a libmp3lame -qscale:a 0 {}.mp3 && del {} "