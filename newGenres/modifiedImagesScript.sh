for file in newFolder/*.txt
do
	filename="$file"
	imageFolder=$(echo $filename | cut -f 1 -d '.')
	
	while read -r line
	do
		name="$line"
		python modifiedSaveImages.py $name $imageFolder
		count=`expr $count + 1` 
	done < "$filename"
done


# filename="$1"
# imageFolder="$2"
# count=1
# while read -r line
# do
#     name="$line"
#     python saveImages.py $name $count $imageFolder
#     count=`expr $count + 1` 
# done < "$filename"