from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    return None