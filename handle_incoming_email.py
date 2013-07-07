import logging
import webapp2
import base64
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

import urllib
from google.appengine.api import urlfetch

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):

    	tc_url = 'http://lrs.tld/TCAPI/statements'
    	tc_auth = 'Basic '+ base64.b64encode('user@example.com:password')

        logging.info("Received a message from: " + mail_message.sender)
        logging.info("message subject: " + mail_message.subject)

        plaintext_bodies = mail_message.bodies('text/plain')

        body_json = ""
        for content_type, body in plaintext_bodies:
	        body_json += body.decode()
            #logging.info(body_json)

		logging.info("message body: " + body_json)

        data = [line.strip().split(':') for line in body_json.split('\n')]

        tc_email = ''
        tc_fname = ''
        tc_lname = ''
        tc_verb = ''
        tc_object_id = ''
        tc_object_name = ''
        tc_object_desc = ''

        for itm in data:
            logging.info(itm)
            if itm[0] == 'email':
                tc_email = itm[1]
            elif itm[0] == 'fname':
                tc_fname = itm[1]
            elif itm[0] == 'lname':
                tc_lname = itm[1]
            elif itm[0] == 'verb':
                tc_verb = itm[1]
            elif itm[0] == 'objectid':
                tc_object_id = itm[1]
            elif itm[0] == 'objectname':
                tc_object_name = itm[1]
            elif itm[0] == 'objectdesc':
                tc_object_desc = itm[1]

        statement_data = ''
        statement_data += '{"actor": {"mbox": ["mailto:' + tc_email + '"],'
        statement_data += '"givenName": ["' + tc_fname + '"],'
        statement_data += '"familyName": ["' + tc_lname + '"]},'
        statement_data += '"verb": "' + tc_verb + '",'
        statement_data += '"object": {"id": "' + tc_object_id + '",'
        statement_data += '"objectType":"Activity","definition": {"name": {"en-US": "' + tc_object_name + '"},'
        statement_data += '"description": {"en-US": "' + tc_object_desc + '"}}}}'

        logging.info(statement_data)

        result = urlfetch.fetch(url=tc_url,
            payload=statement_data,
            method=urlfetch.POST,
            headers={'Content-Type': 'application/json','Authorization': tc_auth})

        logging.info('pantry put results: ' + str(result.status_code) + ' - ' + result.content)


app = webapp2.WSGIApplication([LogSenderHandler.mapping()], debug=True)




#tc@tcemailconnector.appspotmail.com
