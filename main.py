#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	output = ''
        output += 'Send an email to tc@tcemailconnector.appspotmail.com with a statement in the body to add it to the Pantry'
        output += '<br>'
        output += '<br>'
        output += 'example statement content:'
        output += '<br>'
        output += '<br>'
        output += 'email:user@example.com'
        output += '<br>'
        output += 'fname:Joe'
        output += '<br>'
        output += 'lname:User'
        output += '<br>'
        output += 'verb:completed'
        output += '<br>'
        output += 'objectid:http://dev.cloud.scorm.com/testing/102'
        output += '<br>'
        output += 'objectname:A Test Course'
        output += '<br>'
        output += 'objectdesc:This is the course description'
        self.response.write(output)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
