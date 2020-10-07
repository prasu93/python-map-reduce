# Case 1 - Sorter using Files
# Easy to test
# Not needed for Hadoop (Hadoop performs this automatically)

# An inplace sort is good for small data only 
# This step is done automatically in Hadoop

with open("outputCase1_1.txt", "r") as unsorted:
  with open("outputCase1_2.txt", "w") as sorted:

    dataList = unsorted.readlines()
    dataList.sort()

    # output sorted intermediate key-value pairs
    for line in dataList:
      sorted.write(line)  # output
      print (line)        # display to console

