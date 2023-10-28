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
$ 