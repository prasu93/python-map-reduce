
import sys 


# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split("\t")
  if (len(datalist) == 2) : 
    store, amount = datalist

    # print intermediate key-value pairs to standard output
    print(amount + "\t" + store + "\n")
