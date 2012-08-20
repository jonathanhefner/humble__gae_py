#!/usr/bin/env python

import webapp2

pie_url = "http://chart.googleapis.com/chart?cht=p&chs=122x122&chco=%(colors)s&chf=bg,s,00000000&chdlp=r&chd=t:%(data)s"

class ChartHandler(webapp2.RequestHandler):
    def get(self, chart_id):
        if chart_id == 'skills' or chart_id == 'skills-greyscale':
          colors = '338833|992222|333388' if chart_id == 'skills' else '333333|666666|999999'
          data = '0.09,0.40,0.51'
          self.redirect(pie_url % {'colors': colors, 'data': data})
        else:
          self.abort(404)


app = webapp2.WSGIApplication([
    (r'/charts/(.+)', ChartHandler)
], debug=True)
