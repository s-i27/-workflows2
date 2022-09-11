# code review
import os

# DDL
# path = os.getcwd()
path = os.path.abspath('Sample.pu')
print(path)

DDL = 'CREate #table_name1# \n'\
      'CREate #table_name2# \n'

DDL = DDL.replace('#table_name1#','test')

f = open(path)

for line in f:
  print("/" + line.strip() + "/")
  print(line.strip().find('entity'))

f.close

# With open(path) as f:
#   s = f.read()
#   print(type(s))
#   Print(s)

# output
af = open('DDL.txt','w')
af.write(DDL)
af.close