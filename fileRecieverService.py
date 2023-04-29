import cherrypy
import serviceWorkTest
import requests
import json
#import automation
import os

global result
result=[]



#p = serviceWorkTest.processor()


class MyWebService(object):

   @cherrypy.expose

   def upload(self,ufile):
       # Either save the file to the directory where server.py is
       # or save the file to a given path:
       # upload_path = '/path/to/project/data/'
       print("Hey I amm here")
       upload_path = os.path.dirname('/users/tanvirmahdad/research/mom/')
       #ufile = '@/users/tanvirmahdad/Desktop/metasploit_workflow.png'
       print(ufile)
       print(cherrypy.request.headers)
       print(cherrypy.request.params)
       print(cherrypy.request.body.read())
       #print(ufile.filename)
       #print(ufile.content_type)

       # Save the file to a predefined filename
       # or use the filename sent by the client:
       # upload_filename = ufile.filename
       upload_filename = 'filename.png'
       #ufile='@/users/tanvirmahdad/Desktop/metasploit_workflow.png'
       upload_file = os.path.normpath(
           os.path.join(upload_path, upload_filename))
       print(upload_file)
       size = 0
       with open(upload_file, 'wb') as out:
           while True:
               data = ufile.file.read(8192)
               if not data:
                   break
               out.write(data)
               size += len(data)
       out = '''
length: {}
filename: {}
mime-type: {}
''' .format(size, ufile.filename, ufile.content_type, data)

       return out





if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.config.update({'log.error_file': 'Web.log', 'log.access_file': 'Access.log'})
    cherrypy.quickstart(MyWebService())