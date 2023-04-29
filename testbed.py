import subprocess


#result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))
#cdTest=subprocess.run(['cd', '/usr/local/share'], stdout=subprocess.PIPE)
#resultTest=subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
#print(resultTest.stdout.decode('utf-8'))


def subprocess_cmd(command):
    process = subprocess.Popen(command, shell=True)
    print(type(process))
    proc_stdout = str(process.communicate()[0]).strip()
    print(proc_stdout.decode('utf-8'))
    #proc_stdout.communicate('\tstdin: to stdin\n')

subprocess_cmd('ls -l; cd /usr/local/share/metasploit-framework')
