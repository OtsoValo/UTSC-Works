class EmptyQueueError(Exception):
    ''' This error will raise when dequeue an empty queue. '''
    pass


class Queue:
    ''' This is a class of a queue. '''

    def __init__(self):
        self._contents = []

    def enqueue(self, item):
        self._contents.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self._contents.pop(0)
        else:
            raise EmptyQueueError

    def is_empty(self):
        return len(self._contents) == 0


def radix_sort(num_list):
    # create a dict to store all bins
    all_bin = {}
    # create 10 bins and store them in all_bin
    for i in range(10):
        new_bin = Queue()
        all_bin[i] = new_bin
    # initialize longest digit
    digit = 0
    # loop through each num if num's digit is greater than digit,
    # let digit be that number's digit
    for num in num_list:
        if len(str(num)) > digit:
            digit = len(str(num))
    curr_dig = 1
    while curr_dig <= digit:
        for num in num_list:
            if len(str(num)) < curr_dig:
                all_bin[0].enqueue(num)
            else:
                all_bin[int(str(num)[-curr_dig])].enqueue(num)
        num_list = []
        for bin_num in all_bin:
            while not all_bin[bin_num].is_empty():
                num_list.append(all_bin[bin_num].dequeue())
        curr_dig += 1
    return num_list


if __name__ == '__main__':
    print(radix_sort([1,2,3,4,5,11,22,33,44,11,323,4,312,13,243]))
