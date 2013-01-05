echo set tics textcolor rgb \"orange\" >> dplot.gnu
echo set border lc rgb \"orange\" >> dplot.gnu
echo set grid lc rgb \"orange\" >> dplot.gnu
echo set title \"Trace of Car\" >> dplot.gnu
echo set xlabel \"X\" >> dplot.gnu
echo set ylabel \"Y\" >> dplot.gnu
echo set xtics 0,20,1000 >> dplot.gnu
echo set ytics 0,20,1000 >> dplot.gnu
echo set autoscale >> dplot.gnu

echo count=\$0 >> dplot.gnu
echo index=1 >> dplot.gnu
touch looper.gnu
printf "plot " > "looper.gnu"

count=0
pt=1
lc=1
position=$[$#-1]
for filename in $@
do
	echo ${filename}f\(n\)=sprintf\(\"${filename}%d.txt\", n\) >> dplot.gnu
	printf "${filename}f(index) using 3:4 with lp pt $pt lw 2 lc $lc notitle, \"${filename}begin.txt\" using 3:4 with points pt 7 ps 2 notitle, \"${filename}end.txt\" using 3:4 with points pt 10 ps 2 notitle" >> "looper.gnu"
	if [ $count != $position ]; then
		printf ", " >> "looper.gnu"
	fi
	count=$[$count+1]
	pt=$[$pt+2]
	lc=$[$lc+1]
done

echo load \'looper.gnu\' >> dplot.gnu
echo pause 5 >> dplot.gnu
printf "\n" >> looper.gnu
echo index=index+1 >> looper.gnu
echo pause 0.05 >> looper.gnu
echo if\(index\<count\) reread >> looper.gnu
