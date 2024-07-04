#!/usr/bin/env python3
'''Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[any]) -> Union[Any, None]:
    ''' Retrieves the first element of a sequence if it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
