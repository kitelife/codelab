#将每个源文件处理成一系列的内容递增的文件
function preProcess() {
name=1
while read line
do
	head -n $name $1 > "$1$name.txt"
	name=$[$name+1] ;
done<$1
head -n 1 $1 > "$1begin.txt"
tail -n 1 $1 > "$1end.txt"
}

printf "call \"dplot.gnu\" " > cmd.gnu

for filename in $@
do
	preProcess $filename
done

printf "$name " >> cmd.gnu
./gendplot.sh $@
gnuplot cmd.gnu

for filename in $@
do
	rm ${filename}[0-9]*.txt
	rm ${filename}begin.txt ${filename}end.txt
done
rm cmd.gnu
rm dplot.gnu
rm looper.gnu
