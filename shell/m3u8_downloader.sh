ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i "$1" -vcodec copy -acodec copy -absf aac_adtstoasc $2.mp4
