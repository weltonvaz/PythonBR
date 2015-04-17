import time
import sys

def progress_bar(value, max, barsize):
    chars = int(value * barsize / float(max))
    percent = int((value / float(max)) * 100)
    sys.stdout.write("#" * chars)
    sys.stdout.write(" " * (barsize - chars + 2))
    if value >= max:
        sys.stdout.write("done. \n\n")
    else:
        sys.stdout.write("[%3i%%]\r" % (percent))
    sys.stdout.flush()


print "processing..."
for i in xrange(11):
    progress_bar(i, 10, 40)
    time.sleep(1)
print "ok"
raw_input()
