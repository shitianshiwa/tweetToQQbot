---
title: 命令使用文档
date: 2020-06-08 10:17:51
tags:
 - 功能
 - 使用
 - 文档
 - 命令
---

## 本BOT推送命令使用说明

1. **调用命令**实现功能需要以`<命令标识符><命令> <参数表>`的形式调用，具体格式已在各命令中说明。

   - 默认标识符为`!`或`！`，故在调用时请添加命令标识符，例如使用帮助命令时，请在聊天室(群/私聊)中键入：

     ```
     !about
     ```

     而非仅发送`about`。

   - 关于权限，部分命令由于涉及重要推送设置或推送大量信息。为了保护BOT正常运行以及群内使用体验，故操作需要管理权限(超级管理员/群主/管理员)进行操作才会进行响应。

   - 在权限中有`@bot`字段的，群聊消息需要在添加标识符的同时@所使用的的BOT账号，如：

     ```
     <@BOT> !getuserinfo shirakamifubuki
     ```

2. 命令和参数表，以及参数表各参数之间需要以**一个半角空格**作为空格，**空参数亦不能省略空格**。

   - 同义格式可以替换`<命令>`使用，功能完全相同(通常提供中文支持或缩写)

3. 参数注释

   - 推文推送命令列表中提到的`<推特用户ID>`是指由英文数字组成的用户名（即在@时会显示的文本）。

   - 烤推命令列表中提到的`<推文ID>`为推文`status`字段后19位(或以上)10进制数码，`<压缩推文ID>`为推文推送时附带的字符串，可使用相关命令互相转换。

4. **!注意!：如果监听列表里没有监听对象则全局设置会被重置。**

## 命令列表

### BOT相关命令

#### 帮助 `about`

- 命令格式：`about`
- 同义格式：`帮助`、`关于`、`help`
- 所需权限：无限制
- 功能说明：返回转推bot的关于消息

#### 信息反馈 `feedback`

- 命令格式：`feedback <信息>`
- 同义格式：`Feedback`、`反馈`
- 所需权限：超级管理员/群管理/群主
- 功能说明：所发送的信息将会反馈到后台日志供开发者查看 并可由开发者查看后处理回复反馈

#### *处理反馈 `dealfeedback`*

- 命令格式：`feedback <编号> <反馈内容>`
- 同义格式：`处理反馈`、`反馈处理`、`dealFeedback`
- 所需权限：仅开发者
- 功能说明：开发者用于回复信息反馈内容的命令

### 

### 推文推送命令

#### 启动监听 `runTweetListener`

- 命令格式：`runTweetListener`

- 同义格式：`启动监听`

- 所需权限：超级管理员, @bot

- 功能说明：用于推特流断连后尝试重启监听 如已启动则会警告

#### 移除全部监听 `delall`

- 命令格式：`delall`

- 同义格式：`这里单推bot`

- 所需权限：超级管理员/群主, @bot

- 功能：移除当前私聊/群的所有监听

#### 查看监听列表 `getpushlist`

- 命令格式：`getpushlist <页码-可选>`

- 同义格式：`DD列表`

- 所需权限：超级管理员/群管理/群主/好友私聊

- 功能：获取当前私聊/群的监听列表，页数默认为1。

![image-20200428114040218](https://raw.githubusercontent.com/chenxuan353/tweetToQQbot/master/readme/image-20200428114040218.png)

#### 获取用户信息 `getuserinfo`

- 命令格式：`getuserinfo <推特用户ID>`

- 同义格式：`查询推特用户 <推特用户ID>` 

- 所需权限：超级管理员/好友私聊/群管理/群主, @bot

- 功能：获取当前私聊/群的监听列表

例：``getuserinfo shiranuiflare``

![image-20200428113938381](https://raw.githubusercontent.com/chenxuan353/tweetToQQbot/master/readme/image-20200428113938381.png)

#### 添加监听对象 `addone`

- 命令格式：`addone <推特用户ID> <称呼> <描述>`

- 同义格式：`给俺D一个 <推特用户ID> <称呼> <描述>`

- 所需权限：超级管理员/好友私聊/群管理/群主, @bot

- 功能说明：添加一个用户到本群监听

- 使用例：`给俺D一个 shirakamifubuki 吹雪 我永远喜欢小狐狸`

  (不设置昵称)使用例：`给俺D一个 shirakamifubuki  我永远喜欢小狐狸`
  
  (完全无参数)使用例：`给俺D一个 shirakamifubuki`
  
  **※ 跨参数设置同样需要空格分割，完全不设置参数时可以不添加空格**

![image-20200428113806819](https://raw.githubusercontent.com/chenxuan353/tweetToQQbot/master/readme/image-20200428113806819.png)

#### 删除监听对象 `delone`

- 命令格式：`delone <推特用户ID>`

- 同义格式：`我不想D了`

- 所需权限：超级管理员/群管理/群主/好友私聊, @bot

- 功能说明：移除一个本群监听的用户



#### 显示BOT推送设置 getGroupSetting

- 命令格式：`getGroupSetting`

- 同义格式：`全局设置列表`

- 所需权限：超级管理员/群管理/群主/好友私聊, @bot

- 功能说明：显示当前私聊/群的全局推送设置



#### 显示推送设置 getSetting

- 命令格式：`getSetting <推特用户ID>`

- 同义格式：`对象设置列表`

- 所需权限：超级管理员/群管理/群主/好友私聊, @bot

- 功能说明：显示当前私聊/群的某个监听对象的推送设置



#### 设置推送属性 setGroupAttr

- 命令格式：`setGroupAttr <属性> <值>`

- 同义格式：`全局设置`

- 所需权限：超级管理员/群管理/群主/好友私聊, @bot

- 功能说明：移除一个本群监听的用户

例：setGroupAttr 转推 关

##### 支持的属性列表(大小写不敏感)

**※ 属性名称，别名1，...，别名n**

###### 	携带图片发送

> upimg，图片，img

#####     消息模版(参数为模版字符串)

> retweet_template,转推模版
>
> quoted_template,转推并评论模版
>
> reply_to_status_template,回复模版
>
> reply_to_user_template,被提及模版
>
> none_template,发推模版

#####     推特转发各类型开关

- 属性

> retweet,转推
>
> quoted,转推并评论
>
> reply_to_status,回复
>
> reply_to_user,被提及
>
> none,发推

- 值

> true,开,打开,开启,1
>
> false,关,关闭,0

#####     推特个人信息变动推送开关

###### 	属性

> change_id,ID改变
>
> change_name,名称改变
>
> change_description,描述改变
>
> change_headimgchange,头像改变

###### 	支持的值

> true,开,打开,开启,1
>
> false,关,关闭,0

#### 模版字符串说明

##### 默认模版

###### 	发推

```
推特ID：$tweet_id_min，【$tweet_nick】发布了：\n$tweet_text\n$media_img
```

###### 	转推

```
推特ID：$tweet_id_min，【$tweet_nick】转了【$related_user_name】的推特：\n$tweet_text\n$media_img
```

###### 	转发并评论

```
推特ID：$tweet_id_min，【$tweet_nick】转发并评论了【$related_user_name】的推特：\n$tweet_text\n====================\n$related_tweet_text\n$media_img
```

###### 	回复与被提及

```
推特ID：$tweet_id_min，【$tweet_nick】回复了【$related_user_name】：\n$tweet_text\n$media_img
```

###### 模版支持的变量

​	注：使用`\n`替代换行符，理论上直接换行也可以但是十分不推荐

> $tweet_id 推特ID
>
> $tweet_id_min 压缩推特id
>
> $tweet_nick 操作人昵称
>
> $tweet_user_id 操作人ID
>
> $tweet_text 发送推特的完整内容
>
> $related_user_id 关联用户ID
>
> $related_user_name 关联用户昵称-昵称-昵称查询不到时为ID(被评论/被转发/被提及)
>
> $related_tweet_id 关联推特ID(被评论/被转发)
>
> $related_tweet_id_min 关联推特ID的压缩(被评论/被转发)
>
> $related_tweet_text 关联推特内容(被转发或被转发并评论时存在)
>
> $media_img 推特携带的图片

#### 更改监听对象属性 setAttr

- 命令格式：`setAttr <监听用户UID> <属性> <值>`

- 同义格式：`对象设置`

- 所需权限：超级管理员/群管理/群主/好友私聊, @bot

- 功能说明：设置指定监听对象的属性

例：`setGroupAttr 997786053124616192 转推 关`

​		`setGroupAttr 997786053124616192 昵称 `

​		`setGroupAttr 997786053124616192 昵称 FBKwaring`

※ UID可以通过命令**getpushlist**查看，大部分属性与**setGroupAttr**命令相同

##### 特有的属性支持

**※ 属性名称，别名1，...，别名n**

> nick,昵称
>
> des,描述



#### 删除推送对象 globalRemove

- 命令格式：`globalRemove 消息类型 Q号/群号`

- 同义格式：`全局移除`

- 所需权限：超级管理员/好友私聊, @bot

- 功能说明：移除某个人或某个群的所有监听，用于修复配置错误(退出群/删除好友时不在线)

##### 消息类型

> 私聊,好友,private
>
> 群聊,群,group

例：`globalRemove 群聊 123456`



#### 查询推特用户信息 getuserinfo

- 命令格式：`getuserinfo <用户UID/用户ID>`

- 同义格式：`查询推特用户`

- 所需权限：超级管理员/好友私聊, @bot

- 功能说明：查询某个用户的信息，显示的头像将会更新(新增与减少监听不会重新下载头像)

  

#### 全局移除 globalRemove

- 命令格式：`globalRemove <private/私聊/group/群聊> <QQ号/群号>`
- 同义格式：`全局移除`
- 所需权限：超级管理员, @bot
- 功能说明：移除某个人或某个群的所有监测，用于修复配置错误(退出群/删除好友时不在线)

#### 压缩推特ID `entweetid`

- 命令格式：`entweetid <推文ID>`

- 同义格式：`推特ID压缩`、`压缩ID`

- 所需权限：无限制

- 功能说明：将推文ID压缩为缩写推文ID

#### 解压推特ID `detweetid`

- 命令格式：`detweetid <缩写推文ID>`

- 同义格式：`推特ID解压`、`解压ID`

- 所需权限：无限制

- 功能说明：将缩写推文ID解压为推文ID

### 推文翻译命令列表

#### 烤推授权 `transswitch`

- 命令格式：`globalRemove <private/私聊/group/群聊> <QQ号/群号>`

- 同义格式：`ts`、`烤推授权`

- 所需权限：群聊, 群主/超级管理员, @bot

- 功能说明：为群聊添加/移除烤推授权(开关功能)

#### 翻译推特 `trans`

- 命令格式：`trans <推文ID/缩写推文ID> <翻译文本>`

- 同义格式：`t`、`烤推`

- 所需权限：无限制

- 功能说明：为某条推文添加翻译，由BOT完成嵌字并返回。翻译文本支持多行，不支持转义字符(TODO: 对emoji的支持尚需完善)

#### 获取推特翻译列表 `translist`

- 命令格式：`translist <页数>`或 `translist`(translist默认值为1)

- 同义格式：`tl`、`烤推列表`

- 所需权限：无限制

- 功能说明：获取已翻译推特列表

#### 获取翻译文本 `gettrans`

- 命令格式：`gettrans <推文ID/缩写推文ID>`

- 同义格式：`gt`、`获取翻译`

- 所需权限：无限制

- 功能说明：获取某条推文的翻译文本

#### 获取烤推帮助 `transabout`

- 命令格式：`transabout`
- 同义格式：`ta`、`烤推帮助`
- 所需权限：无限制
- 功能说明：获取烤推流程相关命令帮助说明

#### *按类型获取推文翻译 `typeGettrans`*

- 命令格式：`typeGettrans <推文翻译类型>`
- 同义格式：`tgt`
- 所需权限：超级管理员/开发者
- 功能说明：仅供开发者使用的推文翻译获取方法

### *权限管理*

该部分仅供超级管理员/开发者使用

#### 获取合法权限组列表 `legalGroupList`

- 命令格式：`legalGroupList`
- 同义格式：`合法组权限列表`
- 所需权限：超级管理员/开发者
- 功能说明：获取合法可授权模块(合法权限组列表)

#### 获取合法权限列表 `legalPermList`

- 命令格式：`legalPermList <合法权限组名>`
- 同义格式：`合法权限列表`
- 所需权限：超级管理员/开发者
- 功能说明：获取某合法权限组内具体可用命令(具体合法权限)

#### 权限组列表 `permGroupList`

- 命令格式：`permGroupList <类型> <ID>`
- 同义格式：`权限组列表`
- 所需权限：超级管理员/开发者
- 功能说明：获取某群聊/聊天所有权限组列表

#### 权限列表 `permList`

- 命令格式：`permList <权限组名>`
- 同义格式：`tgt`
- 所需权限：超级管理员/开发者
- 功能说明：获取某群聊/聊天权限组内权限列表

#### 添加权限 `permAdd`

- 命令格式：`permAdd <群号> <权限组名>`
- 同义格式：`添加权限`
- 所需权限：超级管理员/开发者
- 功能说明：添加某群组/聊天权限

#### 移除权限 `permDel`

- 命令格式：`permDel <群号> <权限组名>`
- 同义格式：`移除权限`
- 所需权限：超级管理员/开发者
- 功能说明：移除某群组/聊天权限

### 翻译功能 

#### 翻译功能设置 `mtransopt`

- 命令格式：`mtransopt <设置>`
- 同义格式：`翻译设置`
- 所需权限：@bot
- 功能说明：进行机器翻译功能设置

##### 机翻功能说明

本BOT提供谷歌和腾讯两种翻译API：

- 腾讯为自动识别语言 翻译为中文
- 谷歌可指定源语言与目标语言

##### 设置选项

###### 谷歌翻译

```
<设置> = 谷歌 <源语言> <目标语言> 
```

使用例：

> !翻译设置 谷歌 中 日

即「使用谷歌API将中文翻译为日文」

###### 腾讯翻译

自动识别默认使用腾讯API
```
<设置> = 腾讯
```
即可

#### 机器翻译 `mtrans`

- 命令格式：`mtrans <文本内容>`
- 同义格式：`机翻`、`翻译`、`mt`
- 所需权限：@bot
- 功能说明：进行机器翻译