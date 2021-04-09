echo 'Creating validation files'

LRU=0
PLRU=1
OPT=2
NON=0
INC=1

#sim_cache<BLOCKSIZE><L1_SIZE> <L1_ASSOC> <L2_SIZE> <L2_ASSOC><REPLACEMENT_POLICY> <INCLUSION_PROPERTY><trace_file>

echo 'Working on the 0th one'
./sim_cache 16 1024 2 0 0 $LRU $NON gcc_trace.txt > 0.txt
sleep 5
#./sim_cache 16 1024 2 0 0 0 0 gcc_trace.txt
echo 'Working on the 1st one'
./sim_cache 16 1024 1 0 0 $LRU $NON perl_trace.txt > 1.txt
sleep 5
echo 'Working on the 2nd one'
./sim_cache 16 1024 2 0 0 $PLRU $NON gcc_trace.txt > 2.txt
sleep 5
echo 'Working on the 3rd one'
./sim_cache 16 1024 2 0 0 $OPT $NON vortex_trace.txt > 3.txt
sleep 5
echo 'Working on the 4th one'
./sim_cache 16 1024 2 8192 4 $LRU $NON gcc_trace.txt > 4.txt
sleep 5
echo 'Working on the 5th one'
./sim_cache 16 1024 1 8192 4 $LRU $NON go_trace.txt > 5.txt
sleep 5
echo 'Working on the 6th one'
./sim_cache 16 1024 2 8192 4 $LRU $INC gcc_trace.txt > 6.txt
sleep 5
echo 'Working on the 7th one'
./sim_cache 16 1024 1 8192 4 $LRU $INC compress_trace.txt > 7.txt