echo 'Creating validation files'

echo 'Working on the 0th one'
./sim bimodal 6 gcc_trace.txt > b1.txt
sleep 5
echo 'Working on the 1st one'
./sim bimodal 12 gcc_trace.txt > b2.txt
sleep 5
echo 'Working on the 2nd one'
./sim bimodal 4 jpeg_trace.txt > b3.txt
sleep 5
echo 'Working on the 3rd one'
./sim gshare 9 3 gcc_trace.txt > g1.txt
sleep 5
echo 'Working on the 4th one'
./sim gshare 14 8 gcc_trace.txt >g2.txt
sleep 5
echo 'Working on the 5th one'
./sim gshare 11 5 jpeg_trace.txt > g3.txt
sleep 5
echo 'Working on the 6th one'

./sim hybrid 8 14 10 5 gcc_trace.txt >h1.txt
sleep 5
echo 'Working on the 7th one'
./sim smith 3 gcc_trace.txt > s1.txt
sleep 5
echo 'Working on the 8th one'

./sim smith 1 jpeg_trace.txt > s2.txt
sleep 5
echo 'Working on the 9th one'
./sim smith 4 perl_trace.txt > s3.txt
