import subprocess
import os

#result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))
#cdTest=subprocess.run(['cd', '/usr/local/share'], stdout=subprocess.PIPE)
#resultTest=subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(resultTest.stdout.decode('utf-8'))


class niktoAutomation:
    def seturl(self,receivedUrl):
        self.niktoUrl=receivedUrl
        self.urlConstructor="nikto "+"-h "+self.niktoUrl+"/ "+" -output /home/ubuntu/nikto.txt"

    def nikto(self,command):
        process = subprocess.Popen(command, shell=True)
        proc_stdout = str(process.communicate()[0]).strip()
        print(proc_stdout.decode('utf-8'))
        #proc_stdout.communicate('\tstdin: to stdin\n')

    def run(self):
        #print(self.urlConstructor)
        strToPass=str(self.urlConstructor)
        #strToPass='ls -l'

        #print(type(strToPass))
        self.nikto(strToPass)
        with open('/home/ubuntu/nikto.txt', 'r') as myfile:
            data = myfile.read().splitlines()

        os.remove('/home/ubuntu/nikto.txt')
        return data
