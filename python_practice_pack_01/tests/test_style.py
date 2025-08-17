
# ざっくりチェック：全ファイルに型ヒントが含まれているか（一部でもOK）
from pathlib import Path
import pkgutil


def test_src_files_have_type_hints():
    import src
    pkg_path = Path(src.__file__).parent
    py_files = [p for p in pkg_path.glob("*.py") if p.name != "__init__.py"]
    assert py_files, "No source files found"
    # ヒントの痕跡として「: 」や「->」を軽く確認（厳密ではない）
    ok = any((": " in p.read_text(encoding="utf-8")) or ("->" in p.read_text(encoding="utf-8")) for p in py_files)
    assert ok, "Add some type hints to your functions/classes"
