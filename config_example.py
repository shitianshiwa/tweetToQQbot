# -*- coding: UTF-8 -*-
from nonebot.default_config import *
#也可以在此处对nonebot进行设置

#超级管理员，拥有最高权限
SUPERUSERS.add(123456) #多个就复制多行

#命令起始标识
COMMAND_START = {'!','！'}

#维护者姓名
mastername = "" #例如：master(123456)

#nonebot的debug开关
DEBUG = True
#nonebot的监听地址与启动端口
NONEBOT_HOST = '0.0.0.0'
NONEBOT_PORT = 8190 #须和CQP中地址一致
API_ROOT = '0.0.0.0:8890'#使用HTTP协议时POST发送地址
#默认botQQ 默认推送用的bot，错误信息会使用此bot推送。
default_bot_QQ = ''
bot_waring_printID = '' #bot警告信息推送到的Q号，为None时不进行推送

#自动消息推送开关
feedback_push_switch : bool = True #推送反馈信息
error_push_switch : bool = True #推送错误信息

#推特更新检测方法(TweetApi,RSShub,PollingTweetApi,Twint)-暂不支持Twint
UPDATA_METHOD = "PollingTweetApi"#使用何种方法进行监听

#烤推图片路径(用于支持酷Q远程连接) 路径：{trans_img_path}/transtweet/transimg/file
trans_img_path = 'pycache_test' #可以是本地路径 也可以是远程路径 本地路径时无法远程连接bot(需要软链接)
#如使用本地路径 可以填写形如file:///<地址>(即默认的当前文件夹位置/cache) 如file:///D:\tweetToQQbot\cache

#图片发送超时时间
img_time_out : str= '15' #图片下载超时时间(秒)

#RSShub推送配置
#基础地址 https://rsshub.app http://192.168.71.150:1300
RSShub_base = 'https://rsshub.app' #默认是公用的https://rsshub.app
RSShub_proxy = '' #代理地址(IP:PORT)
RSShub_updata_interval = 300 #更新间隔-秒(每个监测对象会多消耗1秒以上的时间)
RSShub_silent_start = False #静默启动，启动时不检测更新

#twitter_api需填写
#推特API代理
api_proxy = "" #127.0.0.1:10809
#填写twitter提供的开发Key和secret
consumer_key = '7yZj***************d'
consumer_secret = 'fIgX******************************SJ'
access_token = '848*************************************A'
access_token_secret = 'ShW****************************************oy'

#pollingTwitterApi可填写的多个应用密钥对 -> ['key','secret']
#推特API应用轮询系统，可增加请求量
polling_silent_start = False #静默启动，启动时不检测更新
polling_interval = 60 #轮询监测间隔 单位秒，每对API速率限制约为1.5次每秒(建议60秒及以上)
polling_consumers = [
    #示例 ['7*********************d','fIgX*****************************SJ'],
    [consumer_key,consumer_secret],#基础密钥对，删除影响运行
    #['******************','********************************************'],
]


#机翻引擎配置(腾讯(tencent)->需要API 需要安装模块,谷歌(google))
MachineTrans_default = 'google' #默认翻译引擎
MachineTransApi = {
    'tencent':{
        "switch":True,#开关，配置完成后请设置为True,关闭为False
        #地区 ap-guangzhou->广州 ap-hongkong->香港 na-ashburn->美国(靠近纽约)
        #更多详见 https://cloud.tencent.com/document/api/551/15615#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8
        "Region":"ap-guangzhou",
        "key":"AK****************************8KI",
        "secret":"sW************************w8"
    },
    'google':{
        "switch":True,#开关
    }
}


#推送开关默认设置(每个选项默认值不能缺失，否则将影响运行)
pushunit_default_config = {
    'upimg':0,#是否连带图片显示(默认不带)-发推有效,转推及评论等事件则无效

    #推特推送模版(为空使用默认模版)
    'retweet_template':'',
    'quoted_template':'',
    'reply_to_status_template':'',
    'reply_to_user_template':'', 
    'none_template':'',
    
    #推特推送开关
    'retweet':0,#转推(默认不开启)
    'quoted':1,#带评论转推(默认开启)
    'reply_to_status':1,#回复(默认开启)
    #'reply_to_status_limit':0,#智能回复推送(默认关闭)-开启后仅推送监测人与有足够被关注数的人的回复
    'reply_to_user':1,#提及某人-多数时候是被提及但是被提及不会接收(默认开启)
    'none':1,#发推(默认开启)

    #智能推送(仅限推送单元设置，无法全局设置)
    'ai_retweet':0,#智能推送本人转推(默认不开启)-转发值得关注的人的推特时推送
    'ai_reply_to_status':0,#智能推送本人回复(默认不开启)-回复值得关注的人时推送
    'ai_passive_reply_to_status':0,#智能推送 被 回复(默认不开启)-被值得关注的人回复时推送
    'ai_passive_quoted':0,#智能推送 被 带评论转推(默认不开启)-被值得关注的人带评论转推时推送
    'ai_passive_reply_to_user':0,#智能推送 被 提及(默认不开启)-被值得关注的人提及时推送

    #个人信息变化推送(非实时)
    'change_ID':0, #ID修改(默认关闭)
    'change_name':1, #昵称修改(默认开启)
    'change_description':0, #描述修改(默认关闭)
    'change_headimgchange':1, #头像更改(默认开启)
}

