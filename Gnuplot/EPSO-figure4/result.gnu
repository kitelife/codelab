reset
set terminal postscript eps color
set output "result.eps"
set size 1.0,1.0
set origin 0.0,0.0
set multiplot

set size 0.5,0.5
set origin 0.0,0.5
set title "(a)"
set xlabel "Robot	No."
set ylabel "Remained	Energy"
set xrange [0:6]
set yrange [3000:7000]
plot "1.txt" using 1:2 with lp pt 5 lw 4 title "EPSO", "1.txt" using 1:3 w lp pt 8 lw 4  title "MS-PSO"

unset xlabel
unset ylabel
set title "(b)"
set size 0.5,0.5
set origin 0.0,0.0
set key left top
set ylabel "Variance"
set xrange [0:3]
set yrange [0:1000000]
set ytics 0,100000,1000000
unset xtics
plot "2.1.txt" with boxes fs solid 0.50 title "EPSO", "2.2.txt" with boxes fs solid 0.75 title "MS-PSO"

unset xlabel
unset ylabel
set size 0.5,0.5
set origin 0.5,0.5
set title "(c)"
set xrange [0:3]
set ylabel "Total Energy Consumption"
set yrange [24850:25150]
set ytics 24850,50,25150
unset xtics
plot "3.1.txt" with boxes fs solid 0.50 title "EPSO", "3.2.txt" with boxes fs solid 0.75 title "MS-PSO"

unset xlabel
unset ylabel
set size 0.5,0.5
set origin 0.5,0.0
set title "(d)"
set key right top
set xlabel "Test No."
set ylabel "Mission Completion Times"
set yrange [32:40]
set ytics 32,2,40
set xrange [0:10]
set xtics 0,1,10
plot "4.txt" using 1:2 with linespoints pt 5 lw 4 title "EPSO", "4.txt" using 1:3 w lp pt 8 lw 4 title "MS-PSO"

unset multiplot
