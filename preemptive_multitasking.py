import threading

log = []

def run(tname):
	for i in range(100):
		for j in range(100):
			pass

		log.append("Thread %s"%tname)

threads = []

for i in range(5):
	t = threading.Thread(target = run, args = (i,))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print("\n".join(log))