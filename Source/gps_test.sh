#!/bin/bash
#x=$(gpspipe -w -n 100 |grep lon|tail -n1|cut -d":" -f9|cut -d"," -f1)
#y=$(gpspipe -w -n 100 |grep lon|tail -n1|cut -d":" -f10|cut -d"," -f1)
#echo "$x,$y" 

#!/bin/bash
exec 2>/dev/null
# get positions
gpstmp=/tmp/gps.data
gpspipe -w -n 40 >$gpstmp"1"&
ppid=$!
sleep 10
kill -9 $ppid
cat $gpstmp"1"|grep -om1 "[-]\?[[:digit:]]\{1,3\}\.[[:digit:]]\{9\}" >$gpstmp
size=$(stat -c%s $gpstmp)
if [ $size -gt 10 ]; then
   cat $gpstmp|sed -n -e 1p > gps_lat.txt
   cat $gpstmp|sed -n -e 2p > gps_lon.txt
fi
rm $gpstmp $gpstmp"1"  
