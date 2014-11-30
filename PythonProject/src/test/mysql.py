'''

@author: lizhe_a
'''
import web


db=web.database(dbn='mysql', db='test', user='root', pw='')
for record in db.select('user'):
    print(record.marvel);

if __name__ == '__main__':
    pass