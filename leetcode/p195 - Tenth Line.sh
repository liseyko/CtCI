# Solution 2
awk 'FNR == 10 {print }'  file.txt
# OR
awk 'NR == 10' file.txt

# Solution 3
sed -n 10p file.txt

# Most efficient: Solution 4
tail -n+10 file.txt | head -1
head -10 file.txt | tail -1