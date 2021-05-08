# 全体のファイル構造
```
.
├── README.md
├── launch.sh
├── log/
├── output/
├── publish_record/
│   └── publish_record_main.py
├── subscribe_card/
│   └── subscribe_card_main.py
├── template/
└── token.ini
```

## publish_recodeの中身
```
- publish_record_main.py
  こいつのメイン関数を呼び出すといい。
  ここをいじくることでlog/とoutput/の中身を処理の後に消すかどうかを決める。デフォルトでは消さない設定になっている。
  
- get_userdata_from_slack.py
  slackにある特定のチャンネルに所属しているメンバーのIDと名前、最新のDMテキストを持ってくる
  
- create_xlsx.py
  logからデータを持ってきて、template.xlsxに書き込みoutputに吐き出す。
  
- send_to_slack.py
  outputにいるxlsxファイルを指定したチャンネルに吐き出す。
```
## token.iniの中身
１行目：bot token
２行目：channel のID（チャンネルURLの後半部分
```
xoxb-....
hogehoge
```


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
