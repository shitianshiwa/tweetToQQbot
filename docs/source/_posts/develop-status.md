---
title: 开发情况
date: 2020-06-08 10:15:57
categories:
 - 项目简介
tags:
 - 简介
 - 情况
 - 开发
 - 注意事项
---

## 开发情况

目前测试中：烤推/转推功能

目前开发中：一键部署功能 动态获取功能

## 项目进度及注意事项

支持多个bot远程连接此后端，已经对可能的冲突进行了处理。

目前推特的推送流异常后将尝试5次重启(重启前等待十秒)，五次重启均失败时需要手动重启。

对监听的修改将立刻保存至文件中。

已经保证了每个群就算是多个BOT同时存在也只会添加一个相同监听对象的推送。

现在配置文件读取后会以JSON的形式输出到日志中，如果丢失了配置文件，可以凭日志回档。

并且在退群时会自动卸载监听(需要bot在线)，配置异常时可以手动清除检测。

## 注记

※ 接收推送的接口已经二次封装，只要事件符合推送事件处理器的数据格式，就可以正常推送。

※ 为了保证推送的正常运行使用了多线程。

※ 安装思源黑体CN之后可以修复字体问题。

## 其他

※ 部分周边功能开发见[分仓库](https://github.com/Cyame/OkayuTweetBot)