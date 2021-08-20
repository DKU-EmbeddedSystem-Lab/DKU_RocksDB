# Python parser for Latency evaluation

import sys
import re
import numpy as np

file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

_parser = 'Percentiles:'
p = re.compile(r'[0-9][0-9].')
line = None
while line != '':
   line = fr.readline()

   mylist = line.split(' ')
                    
   if mylist[0] == _parser:
        mylist = mylist[1:]
        # P99.94: > 99.94 re.[0-9]
        #fw.write(mylist[5])
        #1. P00.00: > 00.00 then write
        #2. ',' write
        #3. 00.00 write
        #4. '\n' write
        #5. iter til end
        for i in np.arange(0,len(mylist),2):
            fw.write(''.join(re.sub('[P:]','',mylist[i])))
            #fw.write(''.join(p.findall(mylist[i])))
            fw.write(',')
            fw.write(mylist[i+1])
            fw.write('\n')

fr.close()
fw.close()
