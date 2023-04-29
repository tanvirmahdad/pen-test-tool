from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
import sys
import re
import socket
import time
import stdout

global global_positive_out
global_positive_out = list()
global global_console_status
global_console_status = True
global dataStore
global flag
flag=0
global ip
ip=[]


def read_console(console_data):
    global global_console_status
    global flag
    global ip
    #global_console_status = console_data['busy']
   # print(console_data)
    sigdata = console_data['data'].rstrip().split('\n')
    matchString="[*] + ["+ ip +"] ("+ ip +")"
    for line in sigdata:
        if matchString in line:
            flag=1
        if (flag==1):
            global_positive_out.append(line)
        if '[*] exec: whoami' in line:
            global_console_status=False
    print console_data['data']


class metaAutomation:
    def surl(self,surl):
        self.url=surl




    def extractIP(raw_data):
        global ip
        test=raw_data
        ip=re.findall(r'[0-9]+(?:\.[0-9]+){3}', test)
        print(ip)

    def runServer(self):

        global ip
        ip = socket.gethostbyname(self.url)

        client = MsfRpcClient('cloudSecurity')
        console = MsfRpcConsole(client, cb=read_console)
        print("The Console Running Status is:"+ str(console.running))
        #storeConsole=MsfRpcConsole(client, cb=store_console)

        console.console.read()

        #File for Extracting IP

        #siteData=open("ipFile.txt","a+")

        #This are the list of console execute file that we have will do test in

        console.execute('load wmap')
        #test=storeConsole.execute('load wmap')
        #console.execute('wmap_sites -l')
        #console.execute('cd /users/tanvirmahdad')
        siteAdditionURl='wmap_sites -a ' +'http://'+self.url
        print(siteAdditionURl)
        console.execute(siteAdditionURl)

        #console.execute('wmap_sites -l')

        stringConstructor="wmap_targets -t http://"+str(ip)
        print(stringConstructor)
        console.execute(stringConstructor)
        #console.execute('wmap_targets -l')

        #bufferText=str(console.execute('wmap_sites -l'))

        #siteIp=extractIP(siteData)
        #print(siteIp)
        #extractIP(siteData)


        # Web server Testing

        console.execute('wmap_run -m auxiliary/scanner/http/http_version')
        console.execute('wmap_run -m auxiliary/scanner/http/open_proxy')
        console.execute('wmap_run -m auxiliary/scanner/http/drupal_views_user_enum')
        console.execute('wmap_run -m auxiliary/scanner/http/frontpage_login')
        console.execute('wmap_run -m auxiliary/scanner/http/host_header_injection')
        console.execute('wmap_run -m auxiliary/scanner/http/options')
        console.execute('wmap_run -m auxiliary/scanner/http/robots_txt')
        console.execute('wmap_run -m auxiliary/scanner/http/scraper')
        console.execute('wmap_run -m auxiliary/scanner/http/svn_scanner')
        console.execute('wmap_run -m auxiliary/scanner/http/trace')
        console.execute('wmap_run -m auxiliary/scanner/http/vhost_scanner')
        console.execute('wmap_run -m auxiliary/scanner/http/webdav_internal_ip')
        console.execute('wmap_run -m auxiliary/scanner/http/webdav_scanner')
        console.execute('wmap_run -m auxiliary/admin/http/tomcat_administration')
        console.execute('wmap_run -m auxiliary/scanner/http/webdav_website_content')
        console.execute('wmap_run -m auxiliary/admin/http/tomcat_utf8_traversal')



        #File/Directory Testing

        console.execute('wmap_run -m auxiliary/scanner/http/verb_auth_bypass')
        console.execute('wmap_run -m auxiliary/scanner/http/copy_of_file')
        console.execute('wmap_run -m auxiliary/scanner/http/dir_listing')
        console.execute('wmap_run -m auxiliary/scanner/http/dir_scanner')
        console.execute('wmap_run -m auxiliary/scanner/http/file_same_name_dir')
        console.execute('wmap_run -m auxiliary/scanner/http/files_dir')
        console.execute('wmap_run -m auxiliary/scanner/http/http_put')
        console.execute('wmap_run -m auxiliary/scanner/http/ms09_020_webdav_unicode_bypass')
        console.execute('wmap_run -m auxiliary/scanner/http/prev_dir_same_name_file')
        console.execute('wmap_run -m auxiliary/scanner/http/replace_ext')
        console.execute('wmap_run -m auxiliary/scanner/http/soap_xml')
        console.execute('wmap_run -m auxiliary/scanner/http/trace_axd')
        console.execute('wmap_run -m auxiliary/scanner/http/backup_file')


        #Unique query testing

        console.execute('wmap_run -m auxiliary/scanner/http/blind_sql_query')
        console.execute('wmap_run -m auxiliary/scanner/http/error_sql_injection')
        console.execute('wmap_run -m auxiliary/scanner/http/http_traversal')
        console.execute('wmap_run -m auxiliary/scanner/http/rails_mass_assignment')
        console.execute('wmap_run -m exploit/multi/http/lcms_php_exec')


        console.execute('wmap_vulns -l')
        #console.execute('spool off')
       # console.execute('spool off')

        #with stdout.Capturing() as output:
        #print 'global_console_status: ' + str(global_console_status)

        console.execute('whoami')
        while global_console_status:
            time.sleep(5)

        #with open('/usr/local/share/metasploit-framework/metaResult/vuln.txt', 'r') as myfile:
            #vulns = myfile.read()
        #print("This Block should not be generated")

        global_positive_out.pop()
        print(global_positive_out)
        print("The IP is:"+ str(ip))

        try:
            console.console.destroy()
            print("Console Destroyed")

        except:
            sys.exit()
            print("Except")

        #time.sleep(60)
        #print("The output is:" + global_positive_out)


        #print(global_positive_out)
        #print(test)

        #use spool command to print the result

        vul_list=''.join(global_positive_out)
        vul_list=vul_list.splitlines()

        return vul_list


