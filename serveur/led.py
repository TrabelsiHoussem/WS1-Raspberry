import time
import web
import RPi.GPIO as g

g.setmode(g.BOARD)

led=40

g.setup(led,g.OUT)

def ledon ():
    g.output(led, g.HIGH)
def ledoff():
    g.output(led, g.LOW)




urls = ('/', 'index')
dossier_web = web.template.render('templates/')

app = web.application(urls, globals())


# definit l action a effectuer quand la page index est appele
class index:
    # utilise quand la page est demande
    def GET(self):
        return dossier_web.index()

    # traite une requete ajax
    def POST(self):
        userdata = web.input()
        if hasattr(userdata, 'etat'):
            if userdata.etat == 'on':
                ledon()

            if userdata.etat == 'off':
                ledoff()

if __name__ == '__main__':
    app.run()
