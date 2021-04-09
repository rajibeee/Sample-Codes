echo "Creating validation files"

./sim 2 8 traces/val_trace_gcc.txt > out1.txt

./sim 8 8 traces/val_trace_gcc.txt > out2.txt

./sim 64 1 traces/val_trace_perl.txt > out3.txt

./sim 128 8 traces/val_trace_perl.txt > out4.txt

sleep 2
echo "Comparing validation files"

diff -iw out1.txt validation_runs/pipe_2_8_gcc.txt
echo "Done with 1"
diff -iw out2.txt validation_runs/pipe_8_8_gcc.txt
echo "Done with 2"
#diff -iw out3.txt validation_runs/pipe_64_1_perl.txt
echo "Done with 3"
#diff -iw out4.txt validation_runs/pipe_128_8_perl.txt
echo "Done with 4"
echo "Deleting output files"
#rm out*.txt