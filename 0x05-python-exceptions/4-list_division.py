#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    n_list = list()
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            count += 1
        except (TypeError, ValueError):
            print("wrong type")
            count =+ 1
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            count += 1
            result = 0
        except IndexError:
            print("out of range")
            count += 1
            result = 0
        finally:
            n_list.append(result)
    return n_list
