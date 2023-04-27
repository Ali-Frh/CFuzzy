import sys
import pyprox_tcp

pyprox_tcp.listen_PORT      = int(sys.argv[1])
pyprox_tcp.Cloudflare_IP    = str(sys.argv[2])
pyprox_tcp.Cloudflare_port  = int(sys.argv[3])
pyprox_tcp.L_fragment       = int(sys.argv[4])
pyprox_tcp.fragment_sleep   = float(sys.argv[5])
pyprox_tcp.my_socket_timeout= int(sys.argv[6])
pyprox_tcp.first_time_sleep = float(sys.argv[7])
pyprox_tcp.accept_time_sleep= float(sys.argv[8])
pyprox_tcp.RFrag            = bool(sys.argv[9])

pyprox_tcp.ThreadedServer('',int(sys.argv[1])).listen()
