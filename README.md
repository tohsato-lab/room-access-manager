# room-access-manager
**コミットは必ずDevelop以下のブランチで！！！**

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
$ git branch -b dev/<自分の名前> # 自分専用のブランチを作る。<>は入れなくていい。
```

## Upload
```bash
$ git add .
$ git commit -m '[add]hogehoge' # メッセージは何を更新したかを明確に。
$ git push origin <ブランチ名> # ローカルからリモートに上げる。<>は入れなくていい。
```

## Pull Request
自分のブランチからdevelopへ統合する場合は、githubのページからプルリクを発行。