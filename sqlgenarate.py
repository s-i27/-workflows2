# code review
import os

# DDL
# path = os.getcwd()
path = os.path.abspath('Sample.pu')
print(path)

DDL_template = '''\
' -- ----------------------------------------------------- \n'\
' -- Table `#db_name#`.`#table_name#` \n'\
' -- ----------------------------------------------------- \n'\
' CREATE TABLE IF NOT EXISTS `#db_name#`.`#table_name#` (\n'\
'   `#column#` INT(11) NOT NULL AUTO_INCREMENT COMMENT '**',\n'\
'   `#column#` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '**',\n'\
'   `**` INT(11) NOT NULL DEFAULT '0' COMMENT '**',\n'\
'   `**` int(11) NOT NULL DEFAULT '1' COMMENT '**',\n'\
'   `**` varchar(255) NULL COMMENT '**',\n'\
'   `**` text NOT NULL COMMENT '**',\n'\
'   `**` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '**',\n'\
'   `**` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '**',\n'\
'   PRIMARY KEY (`id`))\n'\
' ENGINE = InnoDB\n'\
' DEFAULT CHARSET = utf8\n'\
' COMMENT = '**';\n'\
'''

DDL_template_column_definitions = '''\
'   `#column#` #type# #null# #default# COMMENT '#content#',\n'\
'''

f = open(path)
DDL = [''] * 10
for i, line in enumerate(f):
    print("/" + line.strip() + "/")
    # DDL create
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
af.close