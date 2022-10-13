#!/bin/bash

path="googleplaystore.csv" 
echo $path

# print the first line
echo "print the first line"
head -n 1 $path  > result1.csv

# print the specified 10 lines
echo "print the specified 10 lines"
sed -n '2,11p' $path > result2.csv

# print the total rows
rows=$(wc -l < $path)
echo "The dataset has $rows rows"

#search for all the apps which rating is 5.0
echo "show rating 5.0 apps"
awk -F',' '{if($3 == 5.0) print $0}'  $path > result3.csv

#sort
echo "sort for the top20 high rating apps"
cut -f 1,3  -d"," $path | sort -k2 -n -r -t, | head -n 20 > result4.csv

# filter 
echo "Enter the keyword: "
read keyword
if ! grep $keyword $path  >/dev/null
then
   echo "keyword not exist"
else
   echo "keyword exist"
   grep -i $keyword $path > result5.csv
fi









