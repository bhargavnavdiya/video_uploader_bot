import threading
import io
import pytube
import urllib.request
class Downloader(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.stream = None
        self.buffer = io.BytesIO()
        
    def run(self):
        try:
            video = pytube.YouTube(self.url, on_progress_callback=self.on_progress)
            stream_url = video.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().url
            print(type(stream_url))
            with urllib.request.urlopen(stream_url) as stream:
                while True:
                    chunk = stream.read(1024)
                    if not chunk:
                        break
                    self.buffer.write(chunk)
        except pytube.exceptions.PytubeError as e:
            print(f"An error occurred while downloading the video {e}")
            
            
    def get_title(self):
        return pytube.YouTube(self.url, on_progress_callback=self.on_progress).title
    
    def get_bytes(self, num_bytes):
        if self.buffer.tell() >= num_bytes:
            return self.buffer.read(num_bytes)
        else:
            return None
        
    def on_progress(self, stream, chunk, bytes_remaining):
        print(f"{bytes_remaining} bytes remaining...")
        
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# downloader = Downloader(url)
# downloader.start()

# while downloader.is_alive():
#     bytes_ = downloader.get_bytes(1024)
#     if bytes_ is not None:
#         print("Yes you are recieveing the bytes\n")
#         pass