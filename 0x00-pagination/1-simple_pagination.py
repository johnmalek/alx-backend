#!/usr/bin/env python3
"""
A python function
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Write a function named index_range that takes two
    integer arguments page and page_size.

    The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start = 0
    end = 0
    for _ in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        takes two integer arguments page with default
        value 1 and page_size with default value 10.
        Returns:
            list of lists containing required data
        """
        assert type(page) is int and page > 0
        assert(page_size) is int and page_size > 0
        dataset = self.dataset()
        try:
            idx = index_range(page, page_size)
            return dataset[idx[0]:idx[1]]
        except IndexError:
            return []
