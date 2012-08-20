#!/usr/bin/env python

import os
import webapp2, jinja2

templates_path = os.path.join(os.path.dirname(__file__), 'templates')
jja = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(templates_path))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jja.get_template('index.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
