
"""ex03: 辞書"""


def word_count(words: list[str]) -> dict[str, int]:
    """単語頻度を返す（大文字小文字は区別しない）。"""
    raise NotImplementedError


def merge_scores(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    """同じキーは加算、それ以外は結合した新しいdictを返す。元は変更しない。"""
    raise NotImplementedError


def deep_get(data: dict, path: list[str], default=None):
    """ネストdictからpathで値を取り出す。なければdefault。"""
    raise NotImplementedError
