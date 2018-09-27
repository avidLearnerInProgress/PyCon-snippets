import threading, random
import multiprocessing

'''def print_s(s):
	print(s)

t = threading.Thread(target = print_s, args = ("hello_world",))
t.start()
print("Started")
t.join()


u = threading.Thread(target = print_s, args = ("hello_world",))
u.daemon = True
u.start()
print("Started")
u.join()
'''

results = []

def compute():
	results.append(sum([random.randint(1, 100) for i in range(1000000)]))

workers = [threading.Thread(target = compute) for x in range(8)]
for worker in workers:
	worker.start()
for worker in workers:
	worker.join()
print("results: %s" %results)

with multiprocessing.Manager() as manager:
	results = manager.list()
	workers = [multiprocessing.Process(target = compute, args = (results,)) for x in range(8)]
	for worker in workers:
		worker.start()
	for worker in workers:
		worker.join()
	print("Results %s" %results)