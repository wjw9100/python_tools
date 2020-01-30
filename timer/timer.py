import time

def timeit_warpper(func):
	#@wraps(func)
	def wrapper(*args,**kwargs):
		start=time.perf_counter()
		func_return_val=func(*args,**kwargs)
		end=time.perf_counter()
		print('{0:<10}.{1:<8}:{2:<8}'.format(func.__module__, func.__name__, end - start))
		return func_return_val
	return wrapper

@timeit_warpper
def func():
	print("11111111111")
	time.sleep(3)
	print("22222222222")

if __name__=="__main__":
	func()
