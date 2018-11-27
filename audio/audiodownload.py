# 导入系统库
import urllib.request
import json
# 声明json目录和文件保存目录
str_file = './audio.json'
file_path = './langxianping/'
# 将json转为object
with open(str_file, 'r') as f:
    json_str = f.read()
    audio_data = json.loads(json_str)
# 将mp3文件保存到本地
for item in audio_data["items"]:
	url = item["audio"]
	file_name = file_path + item["name"] + '.mp3'
	print(file_name, url)
	urllib.request.urlretrieve(url, file_name)
