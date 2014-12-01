
import web
import model


# -*- coding: UTF-8 -*-
urls = ('/', 'index',
        '/login', 'login')
db = web.database(dbn='sqlite', db='crm.db')
render = web.template.render('../templates/')

class index():
    def GET(self):
        return render.index()
#         return render.index(db.select('user'))
class login():
#     form = web.form.Form(web.form.Form("username"),web.form.Form("password"))
    def POST(self):
        postdata=web.input()  
        username=web.net.websafe(postdata.username)  
        password=web.net.websafe(postdata.password) 
        rs = db.select('user')
        for r in rs:
            if  r.username == username and r.password == password :
                return render.clients(model.get_clients())
            return render.error() 
        
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run();
