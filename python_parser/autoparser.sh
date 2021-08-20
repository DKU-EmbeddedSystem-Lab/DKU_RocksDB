#!/bin/bash

#python3 latency_parser.py ../result_txt/compaction_on_latency_result.txt ../parsing_csv/compaction_on_latency_result.csv
for FILE in `ls ../result_txt`
do
	s=${FILE%.*}
	#echo "${s}"
        python3 latency_parser.py ../result_txt/${FILE} ../parsing_csv/${s}.csv
	python3 latency_parser2.py ../result_txt/${FILE} ../parsing_csv/${s}.csv
	#let I=I+1
        #echo "$I) $s"
done
 
