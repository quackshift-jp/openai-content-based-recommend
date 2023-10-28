# OpenAI APIを使った、コンテンツベースレコメンドのデモアプリ

## 使用デモ
使用動画を貼り付けたい.

## 使用技術
Python 3.9.12
Pythonライブラリ（バージョンはrequirements.txtに記載）
フレームワークはStreamlit[https://streamlit.io/]を採用

## ディレクトリ構成
root
┗ src
  ┗ app
    ┗ main.py
  ┗ features(各機能、もし機能が更に分岐しそうならリファクタリングを実施する)
    ┗ ファイル1.py
    ┗ ファイル2.py
┗ files
  ┗ image(画像)
    ┗ 画像1.jpg
  ┗ movie(動画)
    ┗ 動画1.mp4

## 開発用ドキュメント
### Step1: git cloneにて、リポジトリをローカル環境に複製する & 作業ブランチを切る
```
$ git clone https://github.com/quackshift-jp/openai-content-based-recommend.git
$ cd path/to/openai-content-based-recommend && git switch main
$ git pull
$ git checkout -b feature/hogehoge_YYYYMMDD
```

### Step2: Python仮想環境のアクティベート
```
$ python3 -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
```

### Step3: streamlitを起動する
```
$ streamlit run main.py
```


### コンテンツ情報
以下の情報から、入力情報に合わせた服装を提案
```
{
  "contents": {
    "シーズン" : ["春", "夏", "秋", "冬"],
    "色" : ["ダークレッド", "緑系", "ブルー系", "ブラック", "白", "グレー"],
    "服装ジャンル" : ["シティ系", "ストリート", "アメカジ", "カジュアル", "きれいめ"],
    "使用シーン" : ["仕事", "デート", "ディナー", "ランチ", "古着巡り"],
    "身長" : ["低身長(160cm以下)", "全ての身長"],
    "髪色" : ["黒髪", "金髪", "茶髪"],
    "髪型" : ["ショート", "ウルフカット", "マッシュ", "センターパート"],
  },
  "image": "https://drive.google.com/file/d/1sAnaosQDzk_ftFZ9plOgALPalEbQ9MGI/view?usp=drive_link"
}
```