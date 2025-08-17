
import json
from pathlib import Path
import pytest
from src.ex06_files_json import read_lines, save_config, load_config


def test_read_lines(tmp_path: Path):
    p = tmp_path / "a.txt"
    p.write_text("a\n b \n\n c", encoding="utf-8")
    assert read_lines(p) == ["a", " b ", "", " c"]


def test_save_and_load_config(tmp_path: Path):
    p = tmp_path / "conf.json"
    data = {"name": "Yuta", "lang": "ja"}
    save_config(p, data)
    text = p.read_text(encoding="utf-8")
    # ensure formatted
    assert "\n  \"name\"\:" in text
    out = load_config(p)
    assert out == data
    # missing file
    q = tmp_path / "missing.json"
    assert load_config(q) == {}
