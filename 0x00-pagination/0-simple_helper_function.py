#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    page_index = ((page - 1) * page_size, page * page_size)
    return page_index
