import sys
import socket
import time

def sequential(port):
	s = socket.socket()
	s.bind(('0.0.0.0', port))
	s.listen(500)
	while True:
		cli, addr = s.accept()
		handle_request(cli, time.sleep)

def handle_request(s, sleep):
	try:
		s.recv(1024)
		sleep(0.1)
		s.send('''HTTP/1.0 200 Ok

		Hello world''')
		s.shutdown(socket.SHUT_WR)
		print '.',
	except Exception, ex:
		print 'e', ex
	finally:
		sys.stdout.flush()
		s.close()

if __name__ == '__main__':
	sequential(int(sys.argv[1]))