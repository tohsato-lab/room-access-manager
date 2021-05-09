from slack_sdk import WebClient
import re

def get_text(client,dm_id):
    """
    ダイレクトメールから一番新しいテキストを取得
    return       nomal : "........."
           slack error : False
         prosess error : False
    """
    try:
        response = client.conversations_history(channel=dm_id, limit=1)
        if response['ok'] == True:
            resent_text = response['messages'][0]['blocks'][0]['elements'][0]['elements'][0]['text']
            resent_text = re.sub(r"\D", "", resent_text)
            return str(int(resent_text))
        else:
            resent_text = False
            return resent_text
    except IndexError as e:
        print(e)
        resent_text = False
        return resent_text

def get_user_id_list(client,channel_id):
    """
    対象となるチャンネルに所属するメンバーのUSER_IDを取得
    return       nomal : [..., ..., ...]
           slack error : []
         prosess error : []
    """
    try:
        user_ids = client.conversations_members(channel=channel_id)
        if user_ids['ok'] == True:
            user_ids = user_ids["members"]
        else:
            user_ids=[]
        return user_ids
    except Exception as e:
        print(e)
        user_ids = []
        return user_ids

def get_user_info(client,user_id):
    """
    特定のユーザー情報を取得
    return          nomal : {'ok':True, 'user':{...}}
              slack error : False
            prosess error : False
    """
    try:
        user_info = client.users_info(user=user_id)
        if user_info['ok'] == True:
            return user_info
        else:
            user_info=False
            return user_info
    except Exception as e:
        #何かしらのエラーが出た時
        user_info = False
        return user_info

def open_DM_channnel(client,user_id):
    """
    ユーザーとのDMを開く
    return          nomal : DM_channel_id
              slack error : False
            prosess error : False
    """
    try:
        response = client.conversations_open(users=user_id)
        if response['ok'] == True:
            DM_channel_id = response['channel']['id']
            return DM_channel_id
        else:
            DM_channel_id = False
            return DM_channel_id
    except Exception as e:
        print(e)
        DM_channel_id = False
        return

def create_user_dict(client,channel_id):
    #チャンネルに所属しているメンバーのIDを取得
    #メンバーのIDからDMのIDを検索
    #一番新しいDMをstudent_IDとした辞書データを返す
    #返り値　{ student_ID:{'name':'...' , 'slack_ID':'...'}, ... }
    user_ids = get_user_id_list(client,channel_id)
    user_dict = {}
    for id in user_ids:
        user_info = get_user_info(client,id)
        if user_info != False:
            #ユーザーの情報を取得したときにエラーが出ていないか？
            if user_info["user"]["is_bot"] != True:
                #botではないか？
                dm_id = open_DM_channnel(client,id)
                if dm_id != False:
                    #DMをつないだ時にエラーがではないか？
                    text=get_text(client,dm_id)
                    if text != False:
                        #一番新しいテキストを取得したときにエラーが出ていないか？
                        user_dict.update([(text,{"name":user_info['user']['profile']['real_name'],"slack_ID":id})])
    return user_dict

def get_user_dict(token,channel_id):
    #これをmainで呼び出す
    client = WebClient(token=token)
    user_dict = create_user_dict(client,channel_id)
    return user_dict

if __name__ == '__main__':
    token = "xoxb-..."
    channel_id="hogehoge"
    user_dict=get_user_dict(token,channel_id)
    print("=========================")
    for id in user_dict.keys():
        print(id," : ",user_dict[id])
        print()
