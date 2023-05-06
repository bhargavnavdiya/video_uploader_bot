import pytube

link = "https://youtu.be/sVPYIRF9RCQ"
yt = pytube.YouTube(link, use_oauth= True, allow_oauth_cache= True)
stream = yt.streams.filter(progressive= True, res= "720p").first().download("C:\\Users\\bharg\\Downloads\\BUbot")
print("Downloading")