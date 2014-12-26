
import web
import model


# -*- coding: UTF-8 -*-
urls = ('/', 'index',
        '/login', 'login',
        '/bootstrap', 'bootstrap')
render = web.template.render('templates/')

class index():
    def GET(self):
        return render.index()
#         return render.index(db.select('user'))
class login():
#     form = web.form.Form(web.form.Form("username"),web.form.Form("password"))
    def POST(self):
        postdata = web.input()  
        username = web.net.websafe(postdata.username)  
        password = web.net.websafe(postdata.password) 
        if model.login(username, password) :
            return render.clients(model.get_clients())
        return render.error() 
class bootstrap():
    def GET(self):
        return render.bootstrap()       
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run();
