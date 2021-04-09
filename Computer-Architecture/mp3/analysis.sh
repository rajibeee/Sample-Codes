echo "gcc_trace"
echo "-------------------------- N=1 -------------------"
echo $'\n'
./sim 8   1 traces/val_trace_gcc.txt
./sim 16  1 traces/val_trace_gcc.txt
./sim 32  1 traces/val_trace_gcc.txt
./sim 64  1 traces/val_trace_gcc.txt
./sim 128 1 traces/val_trace_gcc.txt
./sim 256 1 traces/val_trace_gcc.txt
echo $'\n'
echo "- --------------------------------- N=2 -----------------------------"
echo $'\n'
./sim 8   2 traces/val_trace_gcc.txt
./sim 16  2 traces/val_trace_gcc.txt
./sim 32  2 traces/val_trace_gcc.txt
./sim 64  2 traces/val_trace_gcc.txt
./sim 128 2 traces/val_trace_gcc.txt
./sim 256 2 traces/val_trace_gcc.txt
echo $'\n'
echo "- ---------------------------------N=4- ---------------------------------"
echo $'\n'
./sim 8   4 traces/val_trace_gcc.txt
./sim 16  4 traces/val_trace_gcc.txt
./sim 32  4 traces/val_trace_gcc.txt
./sim 64  4 traces/val_trace_gcc.txt
./sim 128 4 traces/val_trace_gcc.txt
./sim 256 4 traces/val_trace_gcc.txt
echo $'\n'
echo "- ---------------------------------N=8- ---------------------------------"
echo $'\n'
./sim 8   8 traces/val_trace_gcc.txt
./sim 16  8 traces/val_trace_gcc.txt
./sim 32  8 traces/val_trace_gcc.txt
./sim 64  8 traces/val_trace_gcc.txt
./sim 128 8 traces/val_trace_gcc.txt
./sim 256 8 traces/val_trace_gcc.txt
echo $'\n'
echo $'\n'
echo "- ---------------------------------Perl_trace"
echo $'\n'
echo "- ---------------------------------N=1- ---------------------------------"
echo $'\n'
./sim 8   1 traces/val_trace_perl.txt
./sim 16  1 traces/val_trace_perl.txt
./sim 32  1 traces/val_trace_perl.txt
./sim 64  1 traces/val_trace_perl.txt
./sim 128 1 traces/val_trace_perl.txt
./sim 256 1 traces/val_trace_perl.txt
echo $'\n'
echo "- ---------------------------------N=2- ---------------------------------"
echo $'\n'
./sim 8   2 traces/val_trace_perl.txt
./sim 16  2 traces/val_trace_perl.txt
./sim 32  2 traces/val_trace_perl.txt
./sim 64  2 traces/val_trace_perl.txt
./sim 128 2 traces/val_trace_perl.txt
./sim 256 2 traces/val_trace_perl.txt
echo $'\n'
echo "- ---------------------------------N=4- ---------------------------------"
echo $'\n'
./sim 8   4 traces/val_trace_perl.txt
./sim 16  4 traces/val_trace_perl.txt
./sim 32  4 traces/val_trace_perl.txt
./sim 64  4 traces/val_trace_perl.txt
./sim 128 4 traces/val_trace_perl.txt
./sim 256 4 traces/val_trace_perl.txt
echo $'\n'
echo "- ---------------------------------N=8- ---------------------------------"
echo $'\n'
./sim 8   8 traces/val_trace_perl.txt
./sim 16  8 traces/val_trace_perl.txt
./sim 32  8 traces/val_trace_perl.txt
./sim 64  8 traces/val_trace_perl.txt
./sim 128 8 traces/val_trace_perl.txt
./sim 256 8 traces/val_trace_perl.txt