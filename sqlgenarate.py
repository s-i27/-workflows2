# code review
import os

# DDL
# path = os.getcwd()
path = os.path.abspath('Sample.pu')
print(path)

DDL_template = 'CREATE TABLE IF NOT EXISTS #db_name#.#table_name# \n'\
    '(col_name data_type,) \n'

f = open(path)
DDL = [''] * 10
for i, line in enumerate(f):
    print("/" + line.strip() + "/")
    if line.strip().find('entity'):
        replace_key = line[line.find('entity'):3]
        DDL[i] = DDL_template.replace('#table_name#', replace_key)
        print(DDL[i])
f.close
# With open(path) as f:
#   s = f.read()
#   print(type(s))
#   Print(s)

# output
af = open('DDL.txt', 'w')
af.write(DDL)
af.closeｓ