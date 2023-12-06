import time
import os
tabIp=[]
def verHttp(ip):
    resultat=os.system("telnet "+ip+" 80")
    print("port 80: {}".format(resultat))

def scanIpUp(ip):
    resultat=os.system("ping -n 1 "+ip)
    if (resultat==0):
        tabIp.append(ip)
        print("-------------Liste adress IP--------------")
        for ipx in tabIp:
            verHttp(ipx)
            print("Ip : {}".format(ipx))
        return "Ip valide"
    else:
        return "IP invalide"
def generateIp(subIp_Max=255,subIp1_Max=255):
    subIp=1
    ip="217.64."
    while(0<subIp<subIp_Max):
        subIp1=1
        while(0<subIp1<subIp1_Max):
            subIp1+=1
            netIp =ip+"{}.{}".format(subIp,subIp1)
            robotSentinel1(netIp)
        subIp+=1
def robotSentinel1(ip):
    time.sleep(1)
    print("la machine est en cours {}".format(ip, scanIpUp(ip)))
    
generateIp()
            
        
