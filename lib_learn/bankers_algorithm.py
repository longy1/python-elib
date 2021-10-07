#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Banker\'s Algorithm '

__author__ = 'Ethan Long'

class Bank(object):
    """docstring for Bank"""
    def __init__(self, avalible_dict={}, re_type=0):
        super(Bank, self).__init__()
        assert re_type == len(avalible_dict)

        self.avalible_dict = avalible_dict
        self.re_type = re_type

    def __str__(self):
        print('*' * 80)
        print(f'Class Bank, id {id(self)}.')
        print(f'Avalible List: {self.avalible_dict}')
        print('*' * 80)
        return ''

    __rper__ = __str__

    def _is_safe_for_need(self, need_dict, max_alloc_dict, allocation_dict, work):
        if not need_dict.keys() | max_alloc_dict.keys() | allocation_dict.keys():
            print('Invalid needs_list or max_alloc list.')
            return False

        for key in need_dict.keys():
            if need_dict[key] + allocation_dict[key] > max_alloc_dict[key]:
                print('Max allocation overflow.')
                return False

            if need_dict[key] > work[key]:
                return False
            
        return True

    def is_safe_for_needs(self, t_list):
        if not t_list:
            print('Emtyp thread list.')
            return

        work = dict(self.avalible_dict)
        finished = [False] * len(t_list)
        while False in finished:

            for i in range(len(t_list)):

                if not finished[i]:
                    thread = t_list[i]
                    
                    if self._is_safe_for_need(thread.need_dict, thread.max_alloc_dict, thread.allocation_dict, work):
                        finished[i] = True
                        for key in t_list[i].allocation_dict.keys():
                            work[key] += t_list[i].allocation_dict[key]
                    elif i == len(t_list) - 1:
                        print('No, not safe')
                        return False

        print('Yes, safe.')
        return True

    def is_safe_to_alloc(self, thread, need_dict):
        pass


class Thread(object):
    """docstring for Thread"""
    def __init__(self, need_dict, max_alloc_dict, allocation_dict):
        super(Thread, self).__init__()
        self.need_dict = need_dict
        self.max_alloc_dict = max_alloc_dict
        self.allocation_dict = allocation_dict

    def __str__(self):
        print('*' * 80)
        print(f'Class Thread, id {id(self)}.')
        print(f'Need dict: {self.need_dict}')
        print(f'Max allocation dict: {self.max_alloc_dict}')
        print(f'Allocation dict: {self.allocation_dict}')
        print('*' * 80)
        return ''

    __rper__ = __str__
        

bank = Bank({'r1': 0, 'r2': 1, 'r3': 1}, 3)
t1 = Thread({'r1': 2, 'r2': 2, 'r3': 2}, {'r1': 3, 'r2': 2, 'r3': 2}, {'r1': 1, 'r2': 0, 'r3': 0})
t2 = Thread({'r1': 0, 'r2': 0, 'r3': 1}, {'r1': 6, 'r2': 1, 'r3': 3}, {'r1': 6, 'r2': 1, 'r3': 2})
t3 = Thread({'r1': 1, 'r2': 0, 'r3': 3}, {'r1': 3, 'r2': 1, 'r3': 4}, {'r1': 2, 'r2': 1, 'r3': 1})
t4 = Thread({'r1': 4, 'r2': 2, 'r3': 0}, {'r1': 4, 'r2': 2, 'r3': 2}, {'r1': 0, 'r2': 0, 'r3': 2})
bank.is_safe_for_needs([t1, t2, t3, t4])

bank = Bank({'r1': 0, 'r2': 1, 'r3': 1}, 3)
t5 = Thread({'r1': 1, 'r2': 2, 'r3': 1}, {'r1': 3, 'r2': 2, 'r3': 2}, {'r1': 2, 'r2': 0, 'r3': 1})
t6 = Thread({'r1': 1, 'r2': 0, 'r3': 2}, {'r1': 6, 'r2': 1, 'r3': 3}, {'r1': 5, 'r2': 1, 'r3': 1})
t7 = Thread({'r1': 1, 'r2': 0, 'r3': 3}, {'r1': 3, 'r2': 1, 'r3': 4}, {'r1': 2, 'r2': 1, 'r3': 1})
t8 = Thread({'r1': 4, 'r2': 2, 'r3': 0}, {'r1': 4, 'r2': 2, 'r3': 2}, {'r1': 0, 'r2': 0, 'r3': 2})
bank.is_safe_for_needs([t5, t6, t7, t8])

# b = Bank(re_type=0)
