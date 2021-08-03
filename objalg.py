from typing import TypeVar, Generic
from abc import ABCMeta, abstractmethod

T = TypeVar('T')

class AddExpr(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def lit(self, x: int) -> T:
        pass

    @abstractmethod
    def add(self, x: T, y: T) -> T:
        pass


def expr1(t: AddExpr[T]) -> T:
    return t.add(t.add(t.lit(1), t.lit(2)), t.lit(5))


def expr2(t: AddExpr[T]) -> T:
    e1 = expr1(t)
    return t.add(e1, t.lit(6))


def fib(t: AddExpr[T], n: int) -> T:
    if n < 2:
        return t.lit(n)

    return t.add(fib(t, n - 1), fib(t, n - 2))


class AddExprEval(AddExpr[int]):
    def lit(self, x: int) -> int:
        return x

    def add(self, x: int, y: int) -> int:
        return x + y


class AddExprShow(AddExpr[str]):
    def lit(self, x: int) -> str:
        return f'{x}'

    def add(self, x: str, y: str) -> str:
        return f'({x} + {y})'


print(f'{expr2(AddExprEval())} : {expr2(AddExprShow())}')
# fib example
for i in range(7):
    expr_val = fib(AddExprEval(), i)
    expr_show = fib(AddExprShow(), i) 
    print(f'{expr_val} : {expr_show}')
