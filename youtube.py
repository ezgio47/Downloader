import yt_dlp

# URL des YouTube-Videos (Beispiel)
url = "https://youtu.be/1-7bIxu_z0s?si=-g5LrUtWL6mMGxsT"

# Optionen zum Herunterladen festlegen
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
    'socket_timeout': 60,  # Timeout auf 60 Sekunden setzen, da sonst Fehlermeldung!
}

# Herunterladen des Videos
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])












