# OS Assignment 1 - Memory Management
# Kialan Pillay
# PLLKIA010
# Python Version 2
# Usage: python paging.py [number of page frames (1-7)]
# Input Prompt for Length of Page Reference String (N)

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
            if page not in mem:
                mem.append(page)
                queue.append(page)
                i+=1
                npfault+=1

        else:
            if page not in mem:
                q = queue.pop(0)
                queue.append(page)
                j = mem.index(q)
                mem.pop(j)
                mem.insert(j,page)
                npfault+=1

    return npfault

def LRU(size, pages):
    page_list = list(pages)
    mem = []
    usage = []
    i = 0
    npfault = 0

    for page in page_list:
        if i<size:
            if page in usage:
                usage.remove(page)
            usage.insert(0,page)
            if page not in mem:
                mem.append(page)
                i+=1
                npfault+=1

        else:
            if page in usage:
                usage.remove(page)
            usage.insert(0,page)
            if page not in mem:
                q = usage.pop(-1)
                j = mem.index(q)
                mem.pop(j)
                mem.insert(j,page)
                npfault+=1

    return npfault

def OPT(size, pages):
    page_list = list(pages)
    mem = []
    i = 0
    n = 0
    npfault = 0

    for page in page_list:
        if i<size:
            if page not in mem:
                mem.append(page)
                i+=1
                npfault+=1
            n+=1

        else:
            if page not in mem:
                usage = []
                for m in mem:
                    if m in page_list[n::]:
                        usage.append(page_list[n::].index(m))
                    else:
                        usage.append(10000)

                u = usage.index(max(usage))
                mem.pop(u)
                mem.insert(u,page)
                npfault+=1
            n+=1

    return npfault

def main():
    seed(2020)
    pages = ""
    N = eval(raw_input('Enter N - the number of pages to generate.\n'))
    for _ in range(N):
	       pages += str(randint(0, 9))
    size = int(sys.argv[1])
    if(size > 7 or size < 1):
        print('Error. number of pages parameter not in range [1,7]')
        exit()
    print 'FIFO', FIFO(size,pages), 'page faults.'
    print 'LRU', LRU(size,pages), 'page faults.'
    print 'OPT', OPT(size,pages), 'page faults.'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ('Usage: python paging.py [number of page frames]')
    else:
        main()
