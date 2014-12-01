'''
@author: lizhe_a
'''
import web

# -*- coding: UTF-8 -*-

db = web.database(dbn='sqlite', db='crm.db')

def get_clients():
    return db.select('client', order='id DESC')

if __name__ == '__main__':
    pass