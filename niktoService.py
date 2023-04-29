import cherrypy
import serviceWorkTest
import requests
import json
import nikto_automation

global result
result=[]



#p = serviceWorkTest.processor()
nikto=nikto_automation.niktoAutomation()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def nikto(self):
        global result
        output_data={}
        data = cherrypy.request.json
        goturl=data.values()[0]
        nikto.seturl(goturl)
        result=nikto.run()
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