#!/bin/bash

function foreachd(){
	for file in $1/*
	do
		if [ -f $file ]; then
			echo $file >> ~/$2.txt
		else
			foreachd $file $2
		fi
	done
}

if [ $# = 2 ]; then
	foreachd $1 1
	foreachd $2 2
fi
#以上功能也可用find来实现
#find $1 -depth -type f -exec ls {} \; > 1.txt
#find $2 -depth -type f -exec ls {} \; > 2.txt

filesInDir1=()
filesInDir2=()

count1=0
while read line
do
	filesInDir1[$count1]=$line
	count1=$[$count1+1]
done<1.txt

count2=0
while read line
do
	filesInDir2[$count2]=$line
	count2=$[$count2+1]
done<2.txt

printf "======================================\nBelow is the files with same name:\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
p1=0
while [ $p1 -lt ${#filesInDir1[*]} ]
do
	same=0
	p2=0
	file1abs=${filesInDir1[$p1]}
	file1name=${file1abs##*/}
	while [ $p2 -lt ${#filesInDir2[*]} ]
	do 
		file2abs=${filesInDir2[$p2]}
		file2name=${file2abs##*/}
		if [ $file1name = $file2name ]; then
			same=$[$same+1]
			echo $file1abs VS. $file2abs
			diff $file1abs $file2abs
			echo "------------------------------------"
			unset filesInDir2[$p2]
		fi	
		p2=$[$p2+1]
	done
	if [ $same -gt 0 ]; then
		unset filesInDir1[$p1]
	fi
	p1=$[$p1+1]
done

printf "====================================\nBelow is the files with different names:\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
echo ${filesInDir1[*]}

echo "---------------------------------------"
echo ${filesInDir2[*]}

rm 1.txt
rm 2.txt
