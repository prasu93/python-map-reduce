
import sys


thisKey = 0.0
thisValue = ""

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    store, amount = datalist

    if amount != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey + '\t' + thisValue+'\n')

      # start over for each new key
      thisKey = amount 
      thisValue = store
  
    

# output the final key-summaryvalue result outside the loop
print(str(thisKey) + '\t' + thisValue +'\n')

