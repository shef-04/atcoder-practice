
"""ex04: 関数"""


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    """xを[lo, hi]に収めて返す。"""
    raise NotImplementedError


def apply_all(funcs: list, value):
    """funcsの各関数をvalueに順に適用して最終結果を返す。"""
    raise NotImplementedError


def make_adder(n: int):
    """nを足す関数を返す（クロージャ）。"""
    raise NotImplementedError
