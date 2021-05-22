# Room Access Manager
計算生物学研究室の入退室記録システムです。\
カードリーダで学生証から学籍番号を取得し、月曜日朝10:00に自動生成されたエクセルファイルがSlackのワークスペースに投稿されます。

**なお、学籍番号と氏名※を紐付けるため、研究室Slackに追加されている「RoomAccessManager」と呼ばれるAppに学籍番号を送信する必要があります。**

※ Slackの氏名がそのまま登録されます。

## インストール
1. パッケージのインストール
```shell
bash install.sh
touch token.ini
```
2. token.iniを設定
１行目：bot token
２行目：channel のID（チャンネルURLの後半部分
```
xoxb-....
hogehoge
```
正常にインストールが完了した後、カードリーダを接続する。

## 実行
```shell
bash launch.sh
```
なお、カードリーダが刺さっている状態でも`OSError: [Errno 19] No such device`と表示されることがあるが、
```shell
python3 -m nfc --search-tty
```
を実行すると必要な手順が表示されるので、それに従って不足分の設定を補う。

- - -
**コミットは必ずDevelop以下のブランチで！！！**

## バージョンとか
```
OS : ubuntu 20.04LTS , windows10
python == 3.8.8
slack-sdk == 3.5.0
openpyxl == 3.0.7
```

## slack API のトークン
```
file.upload
  files:write 

conversations.history
  channels:history  groups:history  im:history  mpim:history 

conversations.members
  channels:read  groups:read  im:read  mpim:read 

conversations.open
  channels:manage  groups:write  im:write  mpim:write 

users.info
  users:read

```

## ブランチの構造
    master                   ← 完成品、絶対動くやつ。
    └── develop              ← 開発段階で統合する場所。
        ├── dev/hogehoge     ← それぞれで担当している箇所を開発する場所。
            └── feture/fooo  ←　更にブランチを切りたい場合はこんな感じで。
        └── dev/hogehoge2
        ・
        ・
        ・

## Init
``` bash
$ git clone https://github.com/tohsato-lab/room-access-manager.git # gitリポジトリを落としてくる。
$ cd room-access-manager
$ git checkout -b dev/<自分の名前> # 自分専用のブランチを作る。<>は入れなくていい。
```

## Upload
```bash
$ git add .
$ git commit -m '[add]hogehoge' # メッセージは何を更新したかを明確に。
$ git push origin <ブランチ名> # ローカルからリモートに上げる。<>は入れなくていい。
```

## Pull Request
自分のブランチからdevelopへ統合する場合は、githubのページからプルリクを発行。