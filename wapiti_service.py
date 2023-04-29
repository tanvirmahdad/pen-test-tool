import cherrypy
import requests
import json
import wapiti_automation

global result
result=[]



#p = serviceWorkTest.processor()
wapiti=wapiti_automation.wapitiAutomation()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def wapiti(self):
        global result
        output_data={}
        data = cherrypy.request.json
        goturl=data.values()[0]
        wapiti.seturl(goturl)
        result=wapiti.run()
        #print(type(value))
        #df = pd.DataFrame(data)
        #output = p.sqrt(value)
        #print("The result is: "+str(result))
        #refined_result='\n'.join(result)
        #output_data_json=json.dumps(output_data)
        #return output_data_json
        return result
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())