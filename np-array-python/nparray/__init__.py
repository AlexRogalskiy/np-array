import numpy as np

from collections import namedtuple
from enum import IntEnum


VERSION = 'U20PJBYW'
SUPPORTED_VERSIONS = {VERSION}
VERSION_SIZE = 8

NUMBER_SIZE = 4
SHORT_SIZE = 2
STRING_TYPE = np.unicode_


class TypeDescriptor(IntEnum):
    INTEGER = 1
    FLOAT = 2
    STRING = 3
    INTEGER16 = 4
    FLOAT16 = 5

    @classmethod
    def from_dtype(cls, dtype):
        if dtype == np.int32:
            return cls.INTEGER
        if dtype == np.int16:
            return cls.INTEGER16
        if dtype == np.float32:
            return cls.FLOAT
        if dtype == np.float16:
            return cls.FLOAT16
        if dtype.type == STRING_TYPE:
            return cls.STRING
        raise ValueError('invalid type: ' + str(dtype))


Metadata = namedtuple('Metadata', [
    'type_descriptor',
    'array_name',
    'rows',
    'columns',
    'data_size'
])
