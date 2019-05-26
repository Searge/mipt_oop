from typing import Tuple, List, Union

lst: List[Tuple[Union[int, float], Union[int, float]]] = []


def read_lst(lst_):
    """
    Print list line by line
    :type lst_: List[Tuple[Union[int, float], Union[int, float]]]
    :rtype: None
    """
    for i in range(len(lst_)):
        print(lst_[i])


if __name__ == '__main__':
    lst = [(475, 199), (293, 192), (475.9, 199.9), (293, 192)]
    read_lst(lst)
