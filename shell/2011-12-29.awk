awk {print $1} access.log
awk {print $(NF-2)} access.log
awk {print NR ")" $1 "->" $(NF-2)} access.log
awk {if($9=="200"){print $0}} access.log
awk '{print $4 " " $5}' access.log | awk '{print $1}' | awk 'BEGIN{FS=":"}{print $1}' | sed 's/\[//'
