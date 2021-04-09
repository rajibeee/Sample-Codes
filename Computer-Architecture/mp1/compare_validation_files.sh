
for k in {0..7}
do
	diff -i -w $k.txt validation$k.txt
	echo "- - - - - - - - - - Done with $k -- - - - - - - - - - - "
	sleep 5
done