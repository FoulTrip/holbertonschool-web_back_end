#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return a list with the values of the index"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        end_index = min(end_index, len(dataset))

        # return dataset[start_index:5]
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Hypermedia pagination"""
        # assert isinstance(page, int) and page > 0
        # assert isinstance(page_size, int) and page_size > 0

        if len(self.get_page(page + 1, page_size)) < page_size:
            next_page = None
        else:
            next_page = page + 1

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        total_pages = int(len(self.dataset()) / page_size)

        dict_return = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
        return dict_return


def index_range(page: int, page_size: int) -> tuple:
    """return a  tuple of size two containing a start index
    and an end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
