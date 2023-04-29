import subprocess
import os

#result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))
#cdTest=subprocess.run(['cd', '/usr/local/share'], stdout=subprocess.PIPE)
#resultTest=subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(resultTest.stdout.decode('utf-8'))


class wapitiAutomation:
    def seturl(self,receivedUrl):
        self.wapitiUrl=receivedUrl
        self.urlConstructor="wapiti "+"-u "+"http://"+self.wapitiUrl+"/ "+"-f txt -o /users/tanvirmahdad/wapiti.txt"+" --flush-session"

    def wapiti(self,command):
        process = subprocess.Popen(command, shell=True)
        proc_stdout = str(process.communicate()[0]).strip()
        print(proc_stdout.decode('utf-8'))
        #proc_stdout.communicate('\tstdin: to stdin\n')

    def run(self):
        #print(self.urlConstructor)
        strToPass=str(self.urlConstructor)
        #strToPass='ls -l'

        #print(type(strToPass))
        self.wapiti(strToPass)
        with open('/users/tanvirmahdad/wapiti.txt', 'r') as myfile:
            data = myfile.read().splitlines()

        print(data)
        os.remove('/users/tanvirmahdad/wapiti.txt')
        return data
