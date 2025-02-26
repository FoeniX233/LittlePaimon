# LittlePaimon更新日志

+ 5.19
  - 米游社签到新增`全部重签`，仅限超级管理员使用，需@机器人
  - `原神猜语音`不再需要`我猜`，直接回答角色别名即可参与猜猜看
  - 异步请求库从`aiohttp`改用`httpx`，需安装依赖库`pip install httpx`
  - 修复`60秒读世界`在频道无法关闭推送的BUG
+ 5.20
  - 修复`ysc`缺少资源问题
  - 封装部分常用方法，优化导包
  - `Paimon_Chat`新增`更新派蒙语音`，实时更新语音
+ 5.21
  - 修复可能因ssl证书导致的静态资源下载问题
+ 5.23
  - 新增`xx原魔图鉴`
+ 5.25
  - `ys、ysc、ysa、sy`等和`wiki`模块指令可以对话式查询
+ 5.27
  - 新增`原神日历`[@nicklly](https://github.com/nicklly)
+ 5.28
  - `Paimon_Chat`聊天新增`学习群友发言`（魔改自[Pallas-Bot](https://github.com/InvoluteHell/Pallas-Bot/tree/master/src/plugins/repeater)），需安装`jieba_fast、pymongo、pypinyin依赖库`、`mongodb数据库`且在`.env.*`配置文件中添加mongodb连接参数`paimon_mongodb_url`，例如`paimon_mongodb_url=mongodb://localhost:27017/`
+ 6.3
  - 新增游戏内展柜角色面板卡片，使用`更新角色面板`来获取角色，`ysd角色名`来查看角色卡片
  - 修复部分不记录上次查询的uid的bug
  - 大幅缩短深渊指令`sy`的缓存时间
+ 6.6
  - 修复`模拟抽卡定轨`和`抽卡记录导出`bug
+ 6.7
  - 修复`原神猜语音`和`模拟抽卡`因`nonebot2.0.0b3`版本Union校验产生的bug，但`原神猜语音`将暂时无法私聊使用
+ 6.9
  - 新增`帮助菜单`指令 ~~(不太好看，继续美化)~~
+ 6.12
  - 新增`云原神签到`等功能[@nicklly](https://github.com/nicklly)
  - 修复部分bug，新增`好友、群新成员和龙王提醒`[#45](https://github.com/CMHopeSunshine/LittlePaimon/issues/45)
+ 6.19
  - 新增`米游币商品兑换`功能，私聊机器人发送`myb`跟着一步步指引来做，目前该功能还没有机会做测试，出现问题请提issue
  - `ysb`绑定cookie的方法增加腾讯文档
+ 6.21
  - 适配`nonebot2 beta4`插件元数据，请更新nb版本`pip install nonebot2 --upgrade`
  - `Paimon_Chat`现在可以发图片、视频等，可自行添加
  - 修复`Paimon_Wiki`搜索对象名结果只有一个时仍需要选择的bug
  - 对对联功能api更换
  - 增加部分注释文档
  - 更换原神日历样式[@nicklly](https://github.com/nicklly) ，需用到htmlrender插件`pip install nonebot-plugin-htmlrender`
  - 添加`pyproject.toml`和`poetry.lock`
+ 6.22
  - 增加文本敏感词过滤
  - fix `原神日历`和发送图片bug
+ 6.23
  - 新增查看所有已获取面板信息的角色的列表`ysda`
  - 暂时取消凌晨3点的自动更新角色面板操作
+ 6.25
  - 添加`requirements.txt`
+ 6.28
  - `ysd`现在支持查看`旅行者`面板信息，增加地区图标显示
  - 优化`ysd`圣遗物评分算法，现在以有效词条数来决定评级，能简单判断角色多种流派玩法[#40](https://github.com/CMHopeSunshine/LittlePaimon/issues/40)
  - 优化`ysd`面板属性和圣遗物词条不对齐的问题
  - `原神猜语音`新的角色也能正确匹配识别[#82](https://github.com/CMHopeSunshine/LittlePaimon/pull/82)
  - 修复`获取抽卡记录`问题[#81](https://github.com/CMHopeSunshine/LittlePaimon/issues/81)
+ 6.30
  - `ysd`支持查看`钟离、胡桃、雷电将军`的伤害计算(~~如果不准请反馈~~)
+ 7.1
  - 伤害计算新增`魈`
+ 7.3
  - 重构部分代码
  - **修改静态资源和用户数据目录**
    - 理论上会**自动迁移**，但`git pull`更新可能会将资源删除，所以最好**手动迁移，同时备份**
    - 1、将派蒙的`res`文件夹改名`LittlePaimon`，移到nonebot根目录的`resources`中（没有`resources`就新建一个）
    - 2、将派蒙的`user_data`文件夹移到nonebot根目录的`data/LittlePaimon`目录中（同理，没有就新建）
  - 静态资源改为启动时自动下载
+ 7.4
  - 回档部分7.3的修改
  - `ysd`新增`香菱、申鹤`伤害计算
  - 修复`60秒早报`接口bug
  - 修复神里绫人被识别为绫华别名的bug
  - 修复抽卡记录获取bug
+ 7.8
  - 增加`甘雨、夜兰、行秋、神里绫华、阿贝多、刻晴、八重神子`伤害计算
+ 7.9
  - 增加`优菈、达达利亚、迪卢克、凝光、菲谢尔、北斗、神里绫人、荒泷一斗、宵宫`伤害计算
+ 7.13
  - 增加`诺艾尔、烟绯、珊瑚宫心海`伤害计算
+ 7.14
  - ysd支持`鹿野院平藏`，增加`枫原万叶、鹿野院平藏`伤害计算
+ 7.15
  - 增加新武器的攻略，修复`ysd`命座天赋加成以及岩元素护盾数值
+ 7.17
  - `ysd`新增`班尼特、莫娜、七七、琴、温迪`伤害计算
  - `mys自动签到`支持私聊
  - `sy`修正深渊信息时间介绍
  - `sy`没有绑定cookie时将不再错误的展示空阵容信息
  - `ssbq`修复没有派遣时会报错的bug
+ 7.19
  - 新增`米游币自动获取`#124，不确保一定可用，如产生其他bug请反馈
+ 7.23
  - 深渊登场率数据改为2.8