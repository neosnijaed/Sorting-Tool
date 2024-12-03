from enum import Enum


class DataType(Enum):
    LONG = 'long'
    LINE = 'line'
    WORD = 'word'
    SORT = True


class SortingType(Enum):
    COUNT = 'byCount'
    NATURAL = 'natural'
