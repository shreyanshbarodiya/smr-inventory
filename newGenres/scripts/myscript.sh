filename="$1"
csvfilename="$2"
while read -r line
do
    name="$line"
    python hi2.py $name $csvfilename
done < "$filename"