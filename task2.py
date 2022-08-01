from moviepy.editor import VideoFileClip
import requests, uuid, os

urls = [
    'https://v16-webapp.tiktok.com/e3bde4927fec37a84b675ba46daef896/62e83455/video/tos/useast2a/tos-useast2a-pve-0068/cd3eef470cd24319a493f317e0a76b30/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2180&bt=1090&btag=80000&cs=0&ds=3&ft=ar5S8qT2mo0PDCYyVuaQ9mw1~ObpkV1PC-&mime_type=video_mp4&qs=0&rc=OzxoOzU7ZWc3N2c0PGY3NkBpM3B2cTs6Zmo3ZTMzNzczM0BjYS9iYjEvNjUxMjBjLy5hYSMxLXFncjQwLi9gLS1kMTZzcw%3D%3D&l=202208011414320102170291360133500B',
    'https://v16-webapp.tiktok.com/e1ba5cf7ee5c9dd7a6e6870881be7114/62e8471b/video/tos/useast2a/tos-useast2a-ve-0068c003/e85e5b31555f4f398323d8818f2e5180/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2230&bt=1115&btag=80000&cs=0&ds=3&ft=gKSYZ8hNo0PD1b~cQsg9w.X2O5LiaQ2D~q4&mime_type=video_mp4&qs=0&rc=Zzg7ZThkaTs3NTtpNmZpNkBpanh0Z2Q6ZnA1ZDMzNzczM0A1YzA2MWM1NmExYTA1Li01YSNqL15scjQwZ2dgLS1kMTZzcw%3D%3D&l=20220801153514010192055055133DF254',
    'https://v16-webapp.tiktok.com/d3f0ac4f938a14cd6424e439e86ee8a5/62e8475a/video/tos/useast2a/tos-useast2a-ve-0068c004/41b3d8beb670480484a92f1c06197d3f/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1848&bt=924&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZIx~1we2N-d3yl7Gb&mime_type=video_mp4&qs=0&rc=OmY1Z2Y0NmhoOTlmM2RlM0BpMzZmZ2Y6ZjgzZTMzNzczM0AvX2FhYWNgXjExYDNeXi8xYSNvNW1ycjRfXmBgLS1kMTZzcw%3D%3D&l=20220801153614010192052138273D4656',
    'https://v16-webapp.tiktok.com/3a19311284d01b6a3d665052c7a62a06/62e84dec/video/tos/useast2a/tos-useast2a-ve-0068c003/416af951ce4d448fab9f8cf491a18a58/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=6284&bt=3142&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZB2~1we2NN5Wyl7Gb&mime_type=video_mp4&qs=0&rc=aTw3Mzo1MzRoOGk4Nmk1N0BpanZrZ2U6Zm5kPDMzNzczM0AyYWNeMTAzXzYxMjJeNl4tYSNiLWk1cjQwLnFgLS1kMTZzcw%3D%3D&l=2022080116034201019020922007407518'
]


def get_gif(url: str):
    """ Function takes url of a video makes an http request to it.
        If needed it creates  directory ~/Documents/gifs or windows equivalent.
        The video is downloaded into this directory, converted to gif and deleted after conversion.
    """
    r = requests.get(url)
    
    file_name = str(uuid.uuid4())
    file_type = r.headers.get('content-type').split('/')[1]

    dir_name = os.path.join(os.path.expanduser('~'), 'Documents', 'gifs')
    os.makedirs(dir_name, exist_ok=True)

    full_video_name = os.path.join(dir_name, file_name+'.'+file_type)
    with open(full_video_name, 'wb') as video_file:
        video_file.write(r.content)
    
    full_gif_name = os.path.join(dir_name, file_name+'.gif')
    with VideoFileClip(full_video_name) as video:
        video.write_gif(full_gif_name)
    
    os.remove(full_video_name)

    return full_gif_name

for url in urls:
    print("gif is at path: " + get_gif(url))

