import nmap
N = nmap.PortScanner()
 
 #Necessario:
 #Linux: sudo apt-get install python-nmap 
 #Windows: pip install python-nmap
 
 
alvo = raw_input("IP ou URL exemplo:[www.google.com]: ")
porta1 = raw_input("[1] Para escanear as principais portas, ou [2] para especificar a porta desejada, escolha uma option: ")
if not (porta1 == 1):
      porta = '20,80,22,23,25,53,67,68,110,123,135,156,143,161,179,443,445,1723,1863,3128,3389'
else:
      porta = raw_input("Porta desejada: ")
      
      
N.scan(alvo, porta)


for host in N.all_hosts():
    print("######################################################")
    print("######################################################")
    print("Criado por: Daniel Fontenelle")
    print("Facebook: https://www.facebook.com/danielll.fontenelle")
    print("Creation date: 05/09/2017")
    print("Version: 1.0")
    print("Email: danielzinhooficial@gmail.com")
    print("Github: https://github.com/danielfontenelle")
    print('[+]Host : %s (%s)' % (host, N[host].hostname()))
    print('[+]State : %s' % N[host].state())
    for proto in N[host].all_protocols():
        print("######################################################")
        print('[+]Protocolo : %s' % proto)
        lport = N[host][proto].keys()
        lport = list(lport)
        lport.sort()
        for port in lport:
            print ('[+]porta : %s\testado : %s' % (port, N[host][proto][port]['state']))
'''
N.command_line()
N.scaninfo()
N.all_hosts()
N[host].hostname()
N[host].state()
N[host].all_protocols()
N[host][proto].keys()
N[host].has_tcp(port)
N[host].has_tcp(port)
N[host][proto][port]
N[host][proto][port]['state']
'''
