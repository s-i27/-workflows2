# code review
import os

' -- -----------------------------------------------------
' -- Table `**`.`**`
' -- -----------------------------------------------------
' CREATE TABLE IF NOT EXISTS `**`.`**` (
'   `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '**',
'   `**` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '**',
'   `**` INT(11) NOT NULL DEFAULT '0' COMMENT '**',
'   `**` int(11) NOT NULL DEFAULT '1' COMMENT '**',
'   `**` varchar(255) NULL COMMENT '**',
'   `**` text NOT NULL COMMENT '**',
'   `**` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '**',
'   `**` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '**',
'   PRIMARY KEY (`id`))
' ENGINE = InnoDB
' DEFAULT CHARSET = utf8
' COMMENT = '**';

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
af.close
