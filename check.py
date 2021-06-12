from slack_sdk import WebClient

from push_record.get_userdata_from_slack import get_user_id_list, get_user_info, open_DM_channnel, get_text


def get_token_channel_id():
    ini_path = "./token.ini"
    with open(ini_path, "r") as f:
        data = f.readlines()
    token = data[0].replace('\n', '')
    channel_id = data[1].replace('\n', '')
    return token, channel_id


def create_user_dict(client, channel_id):
    # チャンネルに所属しているメンバーのIDを取得
    # メンバーのIDからDMのIDを検索
    # 一番新しいDMをstudent_IDとした辞書データを返す
    # 返り値　{ student_ID:{'name':'...' , 'slack_ID':'...'}, ... }
    user_ids = get_user_id_list(client, channel_id)
    user_dict = {}
    for user_id in user_ids:
        user_info = get_user_info(client, user_id)
        if user_info:
            # ユーザーの情報を取得したときにエラーが出ていないか？
            if not user_info["user"]["is_bot"]:
                # botではないか？
                dm_id = open_DM_channnel(client, user_id)
                if dm_id:
                    # DMをつないだ時にエラーがではないか？
                    text = get_text(client, dm_id)
                    if text:
                        # 一番新しいテキストを取得したときにエラーが出ていないか？
                        user_dict.update(
                            [(text, {"name": user_info['user']['profile']['real_name'], "slack_ID": user_id})])
                    else:
                        print(user_info['user']['profile']['real_name'])
    return user_dict


def get_user_dict(token, channel_id):
    # これをmainで呼び出す
    client = WebClient(token=token)
    user_dict = create_user_dict(client, channel_id)
    return user_dict


def main():
    tokens = get_token_channel_id()
    user_dict = get_user_dict(tokens[0], tokens[1])
    print("=========================")
    for user_id in user_dict.keys():
        print(user_id, " : ", user_dict[user_id])
        print()


if __name__ == '__main__':
    main()
