import json
from handle_mongo import handle_save_data

def response(flow):
    #抖音
    if 'aweme.snssdk.com/aweme/v1/aweme' in flow.request.url:
        douyin_data_dict = json.loads(flow.response.text)
        for douyin_item in douyin_data_dict['aweme_list']:
            handle_save_data(douyin_item)
    # 快手
    if 'api.gifshouw.com/rest/n/feed/hot' in flow.request.url:
        kuaishou_data_dict = json.loads(flow.response.text)
        for kuaaishou_item in kuaishou_data_dict['feeds']:
            handle_save_data(kuaaishou_item)
    # 今日头条
    if 'is.snssdk.com/api/news/feed' in flow.request.url:
        jrtt_data_dice = json.loads(flow.response.text)
        for jinritoutiao_item in jrtt_data_dice['data']:
            handle_save_data(jinritoutiao_item)