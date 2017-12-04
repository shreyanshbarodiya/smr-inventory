filename="$1"
imageFolder="$2"
count=1
while read -r line
do
    name="$line"
    python saveImages.py $name $count $imageFolder
    count=`expr $count + 1` 
done < "$filename"