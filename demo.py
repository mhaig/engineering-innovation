#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import socket

port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),port))
s.listen(5)

while True:
    client, address = s.accept()
    print 'You found a vulnerability!'
    client.close()

