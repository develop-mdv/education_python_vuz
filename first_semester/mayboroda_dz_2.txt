from random import randint


class OneWayBox(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class OneWayList(object):

    def __init__(self):
        self.head = OneWayBox()

    def add_begin(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            self.head = OneWayBox(value, self.head)

    def add_end(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = OneWayBox(value)

    def random_fill(self):
        if self.head.value is None:
            for i in range(randint(1, 10)):
                self.add_end(randint(1, 10))
        else:
            return False

    def print_all(self):
        cur = self.head
        while cur.next is not None:
            print(cur.value, end=' ')
            cur = cur.next
        print(cur.value)

    def delete_all(self):
        self.head = OneWayBox()

    @property
    def count(self):
        k = 1
        cur = self.head
        while cur.next is not None:
            k += 1
            cur = cur.next
        return k

    @property
    def is_empty(self):
        if self.head.value is None:
            return True
        return False

    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None

    def delete_value(self, value, every=False):
        if self.count == 1 and self.head.value == value:
            self.head = OneWayBox()
        cur = self.head
        if self.head.value == value:
            self.delete_first()
        elif every:
            while cur.next is not None:
                if cur.next.value == value:
                    if cur.next is None:
                        cur.next = None
                    else:
                        cur.next = cur.next.next
                cur = cur.next
            if cur.next.value == value:
                self.delete_last()
        else:
            while cur.next.next is not None:
                if cur.next.value == value:
                    cur.next = cur.next.next
                    return
                cur = cur.next
            if cur.next.value == value:
                self.delete_last()

    def index_val(self, value):
        k = 0
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return k
            k += 1
            cur = cur.next
        return -1

    @property
    def max(self):
        k = self.head.value
        cur = self.head
        while cur is not None:
            if cur.value > k:
                k = cur.value
            cur = cur.next
        return k

    @property
    def min(self):
        k = self.head.value
        cur = self.head
        while cur is not None:
            if cur.value < k:
                k = cur.value
            cur = cur.next
        return k

    def replace(self, old_value, new_value):
        cur = self.head
        while cur.next is not None:
            if cur.value == old_value:
                cur.value = new_value
            cur = cur.next

    @property
    def uniq_count(self):
        k = 0
        cur = self.head
        while cur.next is not None:
            j = cur.next
            flag = True
            while j.next is not None:
                if cur.value == j.value:
                    flag = False
                j = j.next
            if flag:
                k += 1
            cur = cur.next
        i = self.head
        flag = True
        while i.next is not None:
            if i.value == cur.value:
                flag = False
            i = i.next
        if flag:
            k += 1
        return k

    def make_uniq(self):
        cur = self.head
        while cur.next is not None:
            j = cur.next
            while j is not None:
                if cur.value == j.value:
                    self.delete_value(cur.value)
                j = j.next
            cur = cur.next

    def reverse(self):
        cur = self.head
        prev = None
        while cur.next is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
        self.add_begin(cur.value)

    def sort(self, on_value=True):
        j = self.head
        if on_value:
            while j.next is not None:
                cur = self.head
                while cur.next is not None:
                    if cur.value < cur.next.value:
                        cur.value, cur.next.value = cur.next.value, cur.value
                    cur = cur.next
                j = j.next
        else:
            while j.next is not None:
                cur = self.head
                while cur.next is not None:
                    if cur.value < cur.next.value:
                        pup = cur
                        cur = cur.next
                        pup.next = cur.next
                        cur.next = pup
                    cur = cur.next
                j = j.next


class TwoWayBox(object):
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class TwoWayList(object):

    def __init__(self):
        self.head = TwoWayBox()

    def add_begin(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            self.head = TwoWayBox(value, self.head)
            self.head.next.prev = self.head

    def add_end(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = TwoWayBox(value, None, cur)

    def random_fill(self):
        if self.head.value is None:
            for i in range(randint(1, 10)):
                self.add_end(randint(1, 10))
        else:
            return False

    def print_all(self):
        cur = self.head
        while cur.next is not None:
            print(cur.value, end=' ')
            cur = cur.next
        print(cur.value)

    def delete_all(self):
        self.head = TwoWayBox()

    @property
    def count(self):
        k = 1
        cur = self.head
        while cur.next is not None:
            k += 1
            cur = cur.next
        return k

    @property
    def is_empty(self):
        if self.head.value is None:
            return True
        return False

    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_last(self):
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None

    def delete_value(self, value, every=False):
        if self.count == 1 and self.head.value == value:
            self.head = OneWayBox()
        cur = self.head
        if self.head.value == value:
            self.delete_first()
        elif every:
            while cur.next is not None:
                if cur.next.value == value:
                    if cur.next is None:
                        cur.next = None
                    else:
                        cur.next = cur.next.next
                    cur.next.prev = cur
                cur = cur.next
            if cur.next.value == value:
                self.delete_last()
        else:
            while cur.next.next is not None:
                if cur.next.value == value:
                    cur.next = cur.next.next
                    cur.next.prev = cur
                    return
                cur = cur.next
            if cur.next.value == value:
                self.delete_last()

    def index_val(self, value):
        k = 0
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return k
            k += 1
            cur = cur.next
        return -1

    @property
    def max(self):
        k = self.head.value
        cur = self.head
        while cur is not None:
            if cur.value > k:
                k = cur.value
            cur = cur.next
        return k

    @property
    def min(self):
        k = self.head.value
        cur = self.head
        while cur is not None:
            if cur.value < k:
                k = cur.value
            cur = cur.next
        return k

    def replace(self, old_value, new_value):
        cur = self.head
        while cur.next is not None:
            if cur.value == old_value:
                cur.value = new_value
            cur = cur.next

    @property
    def uniq_count(self):
        k = 0
        cur = self.head
        while cur.next is not None:
            j = cur.next
            flag = True
            while j.next is not None:
                if cur.value == j.value:
                    flag = False
                j = j.next
            if flag:
                k += 1
            cur = cur.next
        i = self.head
        flag = True
        while i.next is not None:
            if i.value == cur.value:
                flag = False
            i = i.next
        if flag:
            k += 1
        return k

    def make_uniq(self):
        cur = self.head
        while cur.next is not None:
            j = cur.next
            while j is not None:
                if cur.value == j.value:
                    self.delete_value(cur.value)
                j = j.next
            cur = cur.next

    def reverse(self):
        cur = self.head
        prev = None
        while cur.next is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
        self.add_begin(cur.value)
        self.head.prev = None
        cur = self.head
        while cur.next is not None:
            cur.next.prev = cur
            cur = cur.next

    def sort(self, on_value=True):
        j = self.head
        if on_value:
            while j.next is not None:
                cur = self.head
                while cur.next is not None:
                    if cur.value < cur.next.value:
                        cur.value, cur.next.value = cur.next.value, cur.value
                    cur = cur.next
                j = j.next
        else:
            while j.next is not None:
                cur = self.head
                while cur.next is not None:
                    if cur.value < cur.next.value:
                        pup = cur
                        cur = cur.next
                        pup.next = cur.next
                        cur.next = pup
                    cur = cur.next
                j = j.next
        self.head.prev = None
        cur = self.head
        while cur.next is not None:
            cur.next.prev = cur
            cur = cur.next


if __name__ == "__main__":
    print('One')
    a = OneWayList()
    a.add_end(1)
    a.add_end(3)
    a.add_end(2)
    a.add_end(4)
    a.add_begin(5)
    print(a.count)
    print(a.is_empty)
    print(a.uniq_count)
    a.print_all()
    a.sort()
    a.print_all()
    a.reverse()
    a.print_all()
    a.delete_first()
    a.print_all()
    a.delete_last()
    a.print_all()
    a.delete_value(2)
    a.print_all()
    print(a.index_val(4))
    print(a.max, a.min)
    a.replace(3, 5)
    a.print_all()
    a.add_begin(5)
    a.add_end(4)
    a.add_end(3)
    a.print_all()
    a.make_uniq()
    a.print_all()

    print('Two')
    b = TwoWayList()
    b.add_end(1)
    b.add_end(3)
    b.add_end(2)
    b.add_end(4)
    b.add_begin(5)
    print(b.count)
    print(b.is_empty)
    print(b.uniq_count)
    b.print_all()
    b.sort()
    b.print_all()
    b.reverse()
    b.print_all()
    b.delete_first()
    b.print_all()
    b.delete_last()
    b.print_all()
    b.delete_value(2)
    b.print_all()
    print(b.index_val(4))
    print(b.max, b.min)
    b.replace(3, 5)
    b.print_all()
    b.add_begin(5)
    b.add_end(4)
    b.add_end(3)
    b.print_all()
    b.make_uniq()
    b.print_all()
