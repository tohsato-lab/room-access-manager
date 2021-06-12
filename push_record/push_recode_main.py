import shutil

from get_userdata_from_slack import get_user_dict
from create_xlsx import create_xlsx
import send_to_slack
import os
import glob
import schedule
import time

def get_data_set():
    template_xlsx="../template/template.xlsx"
    log_folder="../log"
    output_xlsx="../output"
    remove_file=False
    return template_xlsx,log_folder,output_xlsx,remove_file

def get_token_channelID():
    ini_path = "../token.ini"
    with open(ini_path, "r") as f:
        data=f.readlines()
    token = data[0].replace('\n','')
    channel_id = data[1].replace('\n','')
    return token,channel_id


def reset_log(log_folder:str):
    shutil.rmtree(log_folder)
    os.makedirs(log_folder, exist_ok=True)


def main():
    token, channel_id = get_token_channelID()

    user_dict = get_user_dict(token=token,channel_id=channel_id)

    template_xlsx,log_folder,output_xlsx,remove_file=get_data_set()
    sended_xlsx_path = create_xlsx(template=template_xlsx,
                                   log_folder=log_folder,
                                   output_xlsx=output_xlsx,
                                   remove_file=remove_file,
                                   user_dict=user_dict)

    result = send_to_slack.send_xlsx(token=token,channel_id=channel_id,sended_file_path = sended_xlsx_path)
    if result:
        print('reset log')
        reset_log(log_folder)
    #os.remove(sended_file_path)


if __name__ == '__main__':
    # main()
    schedule.every().saturday.at("10:00").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
