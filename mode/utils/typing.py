import abc
import collections
import typing
import _collections_abc
from typing import (
    Any,
    Dict,
    Generic,
    KT,
    MutableMapping,
    MutableSequence,
    T,
    T_co,
    VT,
)

__all__ = [
    'AsyncContextManager',
    'ChainMap',
    'Counter',
    'Deque',
    'NoReturn',
]

if typing.TYPE_CHECKING:
    from typing import AsyncContextManager
else:
    try:
        from typing import AsyncContextManager  # noqa: F811
    except ImportError:
        @typing.no_type_check
        class AsyncContextManager(Generic[T_co]):  # noqa: F811
            __slots__ = ()

            async def __aenter__(self):
                return self

            @abc.abstractmethod
            async def __aexit__(self, exc_type, exc_value, traceback):
                return None

            @classmethod
            def __subclasshook__(cls, C):
                if cls is AsyncContextManager:
                    return _collections_abc._check_methods(
                        C, '__aenter__', '__aexit__')
                return NotImplemented


if typing.TYPE_CHECKING:
    from typing import ChainMap
else:
    try:
        from typing import ChainMap  # noqa: F811
    except ImportError:
        @typing.no_type_check
        class ChainMap(collections.ChainMap,  # noqa: F811
                       MutableMapping[KT, VT],
                       extra=collections.ChainMap):
            __slots__ = ()

            def __new__(cls, *args, **kwds):
                if typing._geqv(cls, ChainMap):
                    return collections.ChainMap(*args, **kwds)
                return typing._generic_new(
                    collections.ChainMap, cls, *args, **kwds)


if typing.TYPE_CHECKING:
    from typing import Counter
else:
    try:
        from typing import Counter  # noqa: F811
    except ImportError:
        @typing.no_type_check
        class Counter(collections.Counter,
                      Dict[T, int],
                      extra=collections.Counter):
            __slots__ = ()

            def __new__(cls, *args, **kwds):
                if typing._geqv(cls, Counter):
                    return collections.Counter(*args, **kwds)
                return typing._generic_new(
                    collections.Counter, cls, *args, **kwds)


if typing.TYPE_CHECKING:
    from typing import Deque
else:
    try:
        from typing import Deque  # noqa: F811
    except ImportError:
        @typing.no_type_check
        class Deque(collections.deque,  # noqa: F811
                    MutableSequence[T],
                    extra=collections.deque):
            __slots__ = ()

            def __new__(cls, *args, **kwds):
                if typing._geqv(cls, Deque):
                    return collections.deque(*args, **kwds)
                return typing._generic_new(
                    collections.deque, cls, *args, **kwds)


if typing.TYPE_CHECKING:
    from typing import NoReturn
else:
    try:
        from typing import NoReturn  # noqa: F811
    except ImportError:
        @typing.no_type_check
        class _NoReturn(typing._FinalTypingBase, _root=True):
            __slots__ = ('__type__',)

            def __init__(self, tp: Any = None, **kwds: Any) -> None:
                self.__type__ = tp

            def __hash__(self) -> int:
                return hash((type(self).__name__, self.__type__))

        def __eq__(self, other) -> Any:
            if not isinstance(other, _NoReturn):
                return NotImplemented
            if self.__type__ is not None:
                return self.__type__ == other.__type__
            return self is other
        NoReturn = _NoReturn(_root=True)
