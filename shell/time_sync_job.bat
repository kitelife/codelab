sc config w32time start= auto
sc start w32time
at 03:30 /every:M,T,W,Th,F,S,Su w32tm /config /update /manualpeerlist:"192.168.2.33" /syncfromflags:manual
at 03:31 /every:M,T,W,Th,F,S,Su w32tm /resync /nowait