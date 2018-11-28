grep -oP '\w+' words.txt | sort | uniq -c | sort -nr | sed 's/\ *\(.*\)\ \(.*\)/\2\ \1/'
grep -oP '\w+' words.txt | sort | uniq -c | sort -nr | awk '{ print $2, $1 }'