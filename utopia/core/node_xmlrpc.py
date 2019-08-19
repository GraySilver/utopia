import xmlrpc.client
import http.client

class TimeOutTransport(xmlrpc.client.SafeTransport):

    def make_connection(self, host):
        # return an existing connection if possible.  This allows
        # HTTP/1.1 keep-alive.
        if self._connection and host == self._connection[0]:
            return self._connection[1]
        # create a HTTP connection object from a host descriptor
        chost, self._extra_headers, x509 = self.get_host_info(host)
        self._connection = host, http.client.HTTPConnection(chost, timeout=12)
        return self._connection[1]

class XmlRpc:
    @staticmethod
    def connection(host, port, username, password):
        server = "{host}:{port}/RPC2".format(host=host, port=port)
        if username == "" and password == "":
            address = "http://{server}/RPC2".format(server=server)
        else:
            address = "http://{username}:{password}@{server}/RPC2".format(
                username=username, password=password, server=server
            )

        print(server)
        a = xmlrpc.client.ServerProxy(address,transport=TimeOutTransport())
        return a
