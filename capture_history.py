#!/usr/bin/python

################
# Capture History
# Captures browsing history
# - Fork to have consistent background logging
################

import dpkt, pcap, logging
from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO

#HTTP Request class
class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

def capture():
    pc = pcap.pcap()
    pc.setfilter('tcp')

    for timestamp, packet in pc:
        #unpacks ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)#)
        ip = eth.data
        tcp = ip.data

        try:
            req = dpkt.http.Request(tcp.data)
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            continue

        do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
        more_fragments = bool(ip.off & dpkt.ip.IP_MF)
        fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

        # Print out the info
        request = HTTPRequest(req)
        logging.basicConfig(filename='history.log', level=logging.INFO)
        logging.info(request.path)

if __name__ == "__main__":
    capture()
