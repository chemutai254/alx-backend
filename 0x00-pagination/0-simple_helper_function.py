#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns the start ad end of the index according to the range"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
