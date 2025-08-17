
"""ex05: クラス"""
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int

    # 税込み価格（10%）を返す read-only プロパティ "price_with_tax" を実装せよ。


class Cart:
    """簡易カート: add/remove/total"""
    def __init__(self):
        # 実装：アイテム名→数量 の辞書などでOK
        raise NotImplementedError

    def add(self, item: Item, qty: int = 1) -> None:
        raise NotImplementedError

    def remove(self, item: Item, qty: int = 1) -> None:
        """数量が0以下になったら項目を削除"""
        raise NotImplementedError

    def total(self) -> int:
        """税込合計（切り捨てでint）"""
        raise NotImplementedError
