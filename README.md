# Client-Server-UDP-TCP-Socket-Programming-in-C-python
The three types of socket programming interfaces—stream sockets, datagram sockets, and raw sockets—are implemented in C and Python using UDP, TCP server, and TCP clients to establish a connection with the server.

**UDP is a connection-less unreliable protocol of the transport layer** and TCP is a connection-oriented protocol reliable, whereas UDP is a connectionless protocol of the transport layer. Stream sockets, Datagram sockets and raw sockets are the three socket programming interface types. A key difference between TCP and UDP is speed, as TCP is comparatively slower than UDP. Overall, UDP is a much faster, simpler, and efficient protocol, however, retransmission of lost data packets is only possible with TCP. Why UDP is used then? User datagram protocol (UDP) is used for time-critical data transmissions such as DNS lookups, online gaming, and video streaming. This communication protocol boosts transfer speeds by removing the need for a formal two-way connection before the data transmission begins.

## What is TCP server and TCP client?

>Typically, there are two types of applications that use TCP sockets - servers and clients. A TCP server listens on a well-known port (or IP address and port pair) and accepts connections from TCP clients. A TCP client initiates a connection request to a TCP server in order to setup a connection with the server.
