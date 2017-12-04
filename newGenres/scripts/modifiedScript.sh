for file in newFolder/*.txt
do
	filename="$file"
	while read -r line
	do
	    name="$line"
	    python hi2modified.py $name $filename
	done < "$filename"	
done

# filename="$1"
# csvfilename="$2"
# while read -r line
# do
#     name="$line"
#     python hi2.py $name $csvfilename
# done < "$filename"