import youtube_dl
import os
import argparse


def download_ytvid_as_mp3(path, video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':path + filename,
        'verbose':False
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))

if __name__ == "__main__":
    list_vid = open('./input.txt', 'r')
    vids = list_vid.read().split('\n')

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='/Download/')
    args = parser.parse_args()

    path = os.getcwd()+args.path
    if os.path.isdir(path) != True:
        os.mkdir(path)

    for vid in vids:
        download_ytvid_as_mp3(path, vid)

    # clear the data in the info file
    with open('./input.txt', 'w') as file:
        pass

    print('Finish Download.')