#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return a list with the values of the index"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        end_index = min(end_index, len(dataset))

        # return dataset[start_index:5]
        return dataset[start_index:end_index]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination"""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        assert index <= len(dataset), f"Index {index} out of range"

        start_index = index
        end_index = index + page_size
        end_index = min(end_index, len(dataset))

        dict_returns = {
            "index": start_index,
            "data": dataset[start_index:end_index],
            "page_size": page_size,
            "next_index": end_index,
        }
        return dict_returns


def index_range(page: int, page_size: int) -> tuple:
    """return a  tuple of size two containing a start index
    and an end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
