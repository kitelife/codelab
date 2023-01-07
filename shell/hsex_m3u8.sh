export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890

url=$(curl $1 | grep index.m3u8 | awk -F'src="' '{print $2}' | awk -F'" ' '{print $1}')
file_name=$(echo $1 | md5sum | awk -F' ' '{print $1}')
youtube-dl ${url} -o "${file_name}.mp4"
