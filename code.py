import yt_dlp

yt_dlp.YoutubeDL({"format": "bestvideo[height<=2160]+bestaudio/best", "merge_output_format": "mp4", "outtmpl": "%(title)s.%(ext)s"}).download(["https://youtu.be/ytiPYwftb_w?si=YRdTx8H5bjwgn1mt"])
