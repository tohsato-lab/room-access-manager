from slack_sdk import WebClient

def send_file(client,sended_file_path,channel,comment=None,title=None,file_type=None):
    #一応動く
    try:
        response = client.files_upload(channels=channel,
                                       file=sended_file_path,
                                       title=title,
                                       initial_comment=comment,
                                       file_type=file_type
                                       )
    except Exception as e:
        print(e)
        return False
    return response['ok']

def send_xlsx(token,channel_id,sended_file_path=None):
    client = WebClient(token=token)
    comment = "入退出記録"
    title = sended_file_path.split("/")[-1]
    if sended_file_path != None:
        result = send_file(client=client,
                          sended_file_path=sended_file_path,
                          channel=channel_id,
                          title=title,
                          comment=comment,
                          file_type="xlsx")
        return result
    else:
        print("please write file_path")
        return False

def main():
    send_xlsx_path="../output/"+"hogehoge.xlsx"
    channel="...."
    token = "xoxb-...."
    send_xlsx(token=token,channel_id=channel,sended_file_path=send_xlsx_path)

if __name__ == '__main__':
    main()
