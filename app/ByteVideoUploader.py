from pytube import YouTube
import urllib.request

def download_video(video_url: str) -> bytes:
    try:
        yt = YouTube(video_url, use_oauth= True, allow_oauth_cache= True)
        stream =yt.streams.filter(progressive= True, file_extension = 'mp4').order_by('resolution').desc().first()
        video_bytes = b''
        with urllib.request.urlopen(stream.url, timeout=600) as response:
            video_bytes = response.read()
        return video_bytes
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        return None

