
# Python Practice Pack 01 (VSCode向け)

VSCodeでテストを回しながらPythonの基礎〜実務でよく使う部分を練習します。
難易度はやさしめ→ふつう。**解答は入れていません**（テスト駆動で解いてください）。

## セットアップ

```bash
# 任意のフォルダへ展開後、ターミナルで
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

# 動作確認（全テストは失敗するのが正常）
pytest -q
```

## 進め方（TDDで小さく回す）
1. 1問だけ選ぶ（例: `src/ex01_strings.py`）。
2. 未実装の関数を**1つ**だけ実装 → `pytest tests/test_ex01_strings.py::test_関数名 -q`。
3. 緑になったら**次の1関数**へ。赤のときはエラーメッセージを読み、実装/テストを調整。

## 目次
- `ex01_strings.py`：文字列（フォーマット、スライス、正規化）
- `ex02_lists.py`：リスト（内包表記、ソート、検索）
- `ex03_dicts.py`：辞書（頻度カウント、マージ、ネストアクセス）
- `ex04_functions.py`：関数（引数、デフォルト、*args/**kwargs、ラムダ）
- `ex05_classes.py`：クラス（データクラス、メソッド、プロパティ）
- `ex06_files_json.py`：ファイル入出力とJSON（with、例外、パス操作）

追加の応用：`tests/test_style.py`で**型ヒント**と**PEP8**の軽いチェックをします。

がんばって！
