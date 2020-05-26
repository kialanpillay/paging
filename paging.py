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
    page_list = list(pages) #split string into list
    mem = [] #list of frames
    queue = [] #queue to track page reference order
    i = 0 #frame use counter
    npfault = 0

    for page in page_list:
        if i<size: #if frames not full
            if page not in mem: #if page not in memory
                mem.append(page)
                queue.append(page)
                i+=1
                npfault+=1

        else:
            if page not in mem:
                q = queue.pop(0) #pop the first element of the queue (FIFO)
                queue.append(page) #add new page to queue
                j = mem.index(q) #get the index page to evict
                mem[j] = page #replace page
                npfault+=1

    return npfault

def LRU(size, pages):
    page_list = list(pages) #split string into list
    mem = [] #list of frames
    usage = [] #list to track page reference order
    i = 0
    npfault = 0

    for page in page_list:
        if i<size:
            if page in usage: #if page has been used, add it to front of list
                usage.remove(page)
            usage.insert(0,page)
            if page not in mem: #if page not in memory, add it
                mem.append(page)
                i+=1
                npfault+=1

        else:
            if page in usage: #if page has been used, add it to front of list
                usage.remove(page)
            usage.insert(0,page)
            if page not in mem: #if page not in memory
                q = usage.pop(-1) #remove last element of the list (least used page)
                j = mem.index(q) #get the index page to evict
                mem[j] = page
                npfault+=1

    return npfault

def OPT(size, pages):
    page_list = list(pages)
    mem = [] #list of frames
    i = 0 #frame use counter
    n = 0 #page reference index counter
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
                #create a usage list, with the index of the page in the future references, else 100000000
                usage = [page_list[n::].index(m) if m in page_list[n:] else 100000000 for m in mem]
                u = usage.index(max(usage)) #get the index of the maximum element in the usage list (page not reference in future or furthest ref)
                mem[u] = page
                npfault+=1
            n+=1

    return npfault

def main():
    seed(2020)
    pages = ""
    N = eval(raw_input('Enter N - the number of pages to generate.\n'))
    if(N < 1): #Validation Check
        print 'Error. N < 1'
        exit()
    for _ in range(N): #Generate Page References
	       pages += str(randint(0, 9))
    size = int(sys.argv[1])
    if(size > 7 or size < 1): #Validation
        print 'Error. number of pages parameter not in range [1,7]'
        exit()
    print 'FIFO', FIFO(size,pages), 'page faults.'
    print 'LRU', LRU(size,pages), 'page faults.'
    print 'OPT', OPT(size,pages), 'page faults.'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python paging.py [number of page frames]'
    else:
        main()
