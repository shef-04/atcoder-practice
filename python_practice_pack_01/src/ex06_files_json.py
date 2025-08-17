
"""ex06: ファイル入出力とJSON"""
from pathlib import Path
import json


def read_lines(path: Path) -> list[str]:
    """UTF-8でファイルを読み、改行除去した行リストを返す。"""
    raise NotImplementedError


def save_config(path: Path, data: dict) -> None:
    """JSONをUTF-8で整形（indent=2, ensure_ascii=False）して保存する。"""
    raise NotImplementedError


def load_config(path: Path) -> dict:
    """JSONを読み込んでdictを返す。存在しない場合は{}を返す。"""
    raise NotImplementedError
