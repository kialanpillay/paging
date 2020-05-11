# OS Assignment 1 - Memory Management
# Kialan Pillay
# PLLKIA010
from random import seed
from random import randint
import sys

def FIFO(size, pages):
    page_list = list(pages)
    mem = []
    queue = []
    i = 0
    npfault = 0

    for page in page_list:
        if i<size:
            mem.append(page)
            queue.append(page)
            i+=1
            npfault+=1
        else:
            if(page not in mem):
                q = queue.pop(0)
                queue.append(page)
                j = mem.index(q)
                mem.pop(j)
                mem.insert(j,page)
                npfault+=1

    return npfault

def LRU(size, pages):
    return size

def OPT(size, pages):
    page_list = list(pages)
    mem = []
    queue = []
    i = 0
    n = 0
    npfault = 0

    for page in page_list:
        if i<size:
            mem.append(page)
            queue.append(page)
            i+=1
            n+=1
            npfault+=1
        else:
            if(page not in mem):
                usage = []
                for m in mem:
                    usage.append(page_list[n::].count(m))
                u = usage.index(min(usage))
                mem.pop(u)
                mem.insert(u,page)
                npfault+=1
            n+=1

    return npfault

def main():
    seed(1)
    pages = ""
    for _ in range(8):
	       pages += str(randint(0, 9))

    pages = "85625354"
    size = int(sys.argv[1])
    print ('FIFO', FIFO(size,pages), 'page faults.')
    print ('LRU', LRU(size,pages), 'page faults.')
    print ('OPT', OPT(size,pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ('Usage: python paging.py [number of pages]')
    else:
        main()
