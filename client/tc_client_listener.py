# Please do not remove authors' information
# author: Javier Esquivel <javierernesto.esquivelx@gmail.com>

import socket
import client_consts as CONST
from datetime import datetime


class HostException(Exception):
    def __init__(self):
        self.err = "Unable to get the IP Address"
        super().__init__(self.err)


class ClientListener(object):
    def __init__(self):
        self.__run_listener()

    @staticmethod
    def __run_listener():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(45)
        host = socket.gethostbyname(socket.gethostname())

        if type(host) != str:
            raise HostException()

        s.bind((host, CONST.DEFAULT_PORT))
        s.listen(5)

        while True:
            print("Last Heartbeat: %s" % str(datetime.now()))
            try:
                clientsocket, addr = s.accept()

                msg = s.recv(CONST.DEFAULT_RECV_VALUE)

                # Here starts the job selected - to be implemented

                clientsocket.close()
            except socket.timeout:
                pass
