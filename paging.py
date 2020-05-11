# OS Assignment 1 - Memory Management
# Kialan Pillay
# PLLKIA010

def FIFO(int size, int pages):
    return 0

def LRU(int size, int pages):
    return 0


def OPT(int size, int pages):
    return 0

def main():
    pages = '123456789'
    size = int(sys.argv[1])
    print 'FIFO', FIFO(size,pages), 'page faults.'
    print 'LRU', LRU(size,pages), 'page faults.'
    print 'OPT', OPT(size,pages), 'page faults.'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python paging.py [number of pages]'
    else:
        main()
