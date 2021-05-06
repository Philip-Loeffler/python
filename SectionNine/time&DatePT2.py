import time
from time import perf_counter as my_timer
# monotonic - time cant go backwards
# processed_time - calculates the cpu time, not the elapased time. used for profiling code
import random
print(time.gmtime(0))
print(time.localtime())
print(time.time())


print(time.localtime(time.time()))


time_here = time.localtime()
print(time_here)
print("year", time_here[0], time_here.tm_year)
print("month", time_here[1], time_here.tm_mon)
print("day", time_here[2], time_here.tm_day)

# generates a random number between 1 and six
wait_time = random.randint(1, 6)
# sleeps for the generated number amount of time
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")

end_time = my_timer()
# strtime is used to format the time string
print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))

print("your reactio ntime was {} seconds".format(end_time - start_time))
