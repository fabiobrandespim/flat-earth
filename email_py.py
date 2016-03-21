#email_py.py   python27

#!/usr/bin/python

import smtplib
import socket
import os
import urllib


class SendEmail:
   def __init__(self, emailorigem, senhaemailorigem, emaildestino, emailsubject, emailmenssagem):
     self.emailorigem = emailorigem
     self.senhaemailorigem = senhaemailorigem
     self.emaildestino = emaildestino
     self.emailsubject = emailsubject
     self.emailmenssagem = emailmenssagem


   def sendnow(self):
    # BUSCA O IP DO ROUTER
    url = "http://www.meuip.com.br"
    response = str(urllib.urlopen(url).read())
    #print response
    achouip = response.find('("div_ip").innerHTML')
    iprouter = response[achouip + 24 : achouip + 37]


    # WINDOWS - BUSCA O IP O HOST E O GATEWAY
    gw = os.popen("arp -a").read().split()

    # LINUX - BUSCA O IP O HOST E O GATEWAY
    #gw = os.popen("ip -4 route show default").read().split()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[1], 0))
    ipaddr = s.getsockname()[0]
    gateway = gw[1]
    host = socket.gethostname()
    #print ("Host:", host, "IP:", ipaddr, "GW:", gateway)


    # ENVIA EMAIL
    FROM     = self.emailorigem
    TO       = self.emaildestino
    SUBJECT  = host + " - " + ipaddr + " - " + self.emailsubject
    msg      = self.emailmenssagem
    message  = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, msg)

    username = self.emailorigem
    password = self.senhaemailorigem

    try:
      server   = smtplib.SMTP('smtp.gmail.com:587')
      server.ehlo()
      server.starttls()
      server.login(username,password)
      server.sendmail(FROM, TO, message)
      server.quit()
      print('successfully sent the mail')
    except:
      print('failed to send mail')





