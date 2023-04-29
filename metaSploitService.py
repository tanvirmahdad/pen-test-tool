import cherrypy
import serviceWorkTest
import requests
import json
import automation

global result
result=[]



#p = serviceWorkTest.processor()
metaSploit=automation.metaAutomation()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def msf(self):
        global result
        output_data={}
        data = cherrypy.request.json
        goturl=data.values()[0]
        metaSploit.surl(goturl)
        result=metaSploit.runServer()
        #print(type(value))
        #df = pd.DataFrame(data)
        #output = p.sqrt(value)
        #print("The result is: "+str(result))
        refined_result='\n'.join(result)
        #output_data_json=json.dumps(output_data)
        #return output_data_json
        return refined_result
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())