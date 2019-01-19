import cherrypy


class Poll:

    @cherrypy.expose
    def index(self):

        return "Hello, world. You're at the polls index."

cherrypy.quickstart(Poll())