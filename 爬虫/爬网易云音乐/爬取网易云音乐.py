import requests
import re
import os

filename = 'music\\'
if not os.path.exists(filename):
    os.mkdir(filename)
url = 'https://music.163.com/discover/toplist?id=1897927515'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/98.0.4758.82 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# print(response.text)
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)
# print(html_data)
for num_id, title in html_data:
    music_url = f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
    music_content = requests.get(url=music_url, headers=headers).content
    with open(filename + title + '.mp3', mode='wb') as f:
        f.write(music_content)
    print(num_id, title)
