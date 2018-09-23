import socket, threading

log = []

def _connect():
	s = socket.socket()
	log.append('connecting..')
	s.connect('python.org', 80)
	log.append('connected..')

threads = []

for i in range(2):
	t = threading.Thread(target = _connect)
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print("\n".join(log))