#!/usr/bin/python

################
# Web get 
# A utility that works in similar fashion to the Linux tool 'wget'.
# It makes use of ftp and http to 'get' data.
################

import sys, argparse,os, ftplib, httplib
from urlparse import urlparse
from ftplib import FTP

def main(args):

  url = args.argument
  o = urlparse(url)
  response = os.system("ping -o -q -c 3 -W 3000 "+o.netloc + " 2>&1 >/dev/null")
  if response != 0:
	print("ERROR " + "host is unreachable")
 	sys.exit()
  if(o.scheme == 'ftp'):
	  try:
	    ftp = FTP(o.netloc)
	    ftp.login("anonymous","")
            ftp.set_pasv(True)
	    local_filename = os.getcwd()+"/" + str(o.path).split('/')[-1]
	    ftp_file = open(local_filename, 'wb')
	    ftp.retrbinary('RETR '+ o.path, ftp_file.write)
		
	  except ftplib.all_errors, e:
		if str(o.path).split('/')[-1] in ftp.nlst():
			print "Directory is incorrect"
		else:
			print "File is incorrect"
	  finally:
		  ftp_file.close()

  if(o.scheme == 'http'):
	conn = httplib.HTTPConnection(o.netloc)
	conn.request("GET",o.path)
	res = conn.getresponse()
	if(res.status != 200):
		print ("HTTP request failed, due to : "+str(res.status) + " "+res.reason) 		
	data = res.read()
	local_filename = os.getcwd()+"/" + str(o.path).split('/')[-1]
	http_file = open(local_filename, 'wb')
	http_file.write(data)
	http_file.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = "Re-implementation of wget")
  parser.add_argument(
                      "argument",
                      help = "pass ARG to the program",
                      metavar = "ARG")
  args = parser.parse_args()
  main(args)
