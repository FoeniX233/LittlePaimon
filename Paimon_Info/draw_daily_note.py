#素材来自于https://github.com/ctrlcvs/xiaoyao-cvs-plugin
import datetime
import random
from io import BytesIO
from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from littlepaimon_utils import aiorequests
from littlepaimon_utils.files import load_image

from ..utils.message_util import MessageBuild

res_path = Path() / 'resources' / 'LittlePaimon'


def get_font(size, font='msyhbd.ttc'):
    return ImageFont.truetype(str(res_path / font), size)


async def draw_ring(per):
    if per > 1:
        per = 1
    elif per < 0:
        per = 0
    per_list = [per, 1 - per]
    colors = ['#507bd0', '#FFFFFF']
    plt.pie(per_list, startangle=90, colors=colors)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(per_list,
           wedgeprops={'width': 0.18},
           startangle=90,
           colors=colors)
    bio = BytesIO()
    plt.savefig(bio, transparent=True)
    bio.seek(0)
    img = Image.open(bio).resize((266, 266)).convert('RGBA')
    plt.cla()
    plt.close("all")
    return img


async def draw_daily_note_card(data, uid):
    if not data:
        return '数据出错'
    if data['retcode'] == 10102:
        return f'uid{uid}没有在米游社公开信息哦,请到 个人主页-管理 中打开'
    elif data['retcode'] == 10104:
        return f'uid{uid}有误哦，检查一下或再手动输入一次uid吧'
    elif data['retcode'] != 0:
        return f'打工战士获取{uid}数据失败了，获取状态：\n{data["message"]},{data["retcode"]}'
    data = data['data']
    finished_icon = load_image(res_path / 'daily_note' / 'finished.png')
    bg_img = load_image(res_path / 'daily_note' / '01.png', mode='RGBA')

    xingqi_list=["星期一" , "星期二" , "星期三" , "星期四" , "星期五" , "星期六" , "星期日"]
    now = datetime.datetime.now().strftime('%m-%d %H:%M ')

    bg_draw = ImageDraw.Draw(bg_img)
    # uid和日期文字
    bg_draw.text((225, 65), f"{uid}\n{now}{xingqi_list[datetime.datetime.now().weekday()]}",
                 fill='black', font=get_font(22, 'HYWenHei-85W.ttf'))
    # 树脂文字
    bg_draw.text((200, 185), f"{data['current_resin']}/160", fill='#7b8386', font=get_font(30, 'HYWenHei-85W.ttf'))
    if data['current_resin'] == 160:
        bg_draw.text((201, 220), f"树脂满了哦~", fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
    else:
        recover_time = datetime.datetime.now() + datetime.timedelta(seconds=int(data['resin_recovery_time']))
        recover_time_day = '今天' if recover_time.day == datetime.datetime.now().day else '明天'
        recover_time_str = f'将于{recover_time_day}{recover_time.strftime("%H:%M")}回满~'
        bg_draw.text((201, 220), recover_time_str, fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))

    # 委托文字
    bg_draw.text((200, 260), f"{data['finished_task_num']}/4", fill='#7b8386',
                 font=get_font(30, 'HYWenHei-85W.ttf'))
    if data['finished_task_num'] == 4:
        bg_draw.text((201, 295), "今日委托已全部完成~", fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
    else:
        bg_draw.text((201, 295), "今日委托还未完成哦~", fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))

    # 周本文字
    bg_draw.text((200, 335), f"{3 - data['remain_resin_discount_num']}/3",fill='#7b8386',
                 font=get_font(30, 'HYWenHei-85W.ttf'))
    if data['remain_resin_discount_num'] == 0:
        bg_draw.text((201, 370), "周本减半次数用尽啦~", fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
    else:
        bg_draw.text((201, 370), f"还有{data['remain_resin_discount_num']}次周本减半呢~", fill='#7b8386',
                     font=get_font(12, 'HYWenHei-55W.ttf'))

    # 质变文字
    if data['transformer']['obtained']:

        rt = data['transformer']['recovery_time']
        if rt['Day'] == 0 and rt['reached']:
            bg_draw.text((200, 415), "可使用", fill='#7b8386', font=get_font(30, 'HYWenHei-85W.ttf'))
            bg_draw.text((201, 450), "您的质量参变仪可以用啦~",
                         fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
        elif rt['Day'] == 0 and not rt['reached']:
            bg_draw.text((200, 415), "冷却中", fill='#7b8386', font=get_font(30, 'HYWenHei-85W.ttf'))
            bg_draw.text((201, 450), f"{rt['Hour']}小时后可用~",
                         fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
        else:
            bg_draw.text((200, 415), "冷却中", fill='#7b8386', font=get_font(30, 'HYWenHei-85W.ttf'))
            bg_draw.text((201, 450), f"{rt['Day']}天后可使用~",
                         fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
    else:
        bg_draw.text((200, 415), "未获得", fill='#7b8386', font=get_font(30, 'HYWenHei-85W.ttf'))
    # # 深渊文字
    # abyss_new_month = datetime.datetime.now().month if datetime.datetime.now().day < 16 else datetime.datetime.now().month + 1
    # abyss_new_day = 16 if datetime.datetime.now().day < 16 else 1
    # abyss_new = datetime.datetime.strptime('2022.' + str(abyss_new_month) + '.' + str(abyss_new_day) + '.00:00',
    #                                        '%Y.%m.%d.%H:%M') - datetime.datetime.now()
    # abyss_new_total = datetime.datetime.strptime('2022.' + str(abyss_new_month) + '.' + str(abyss_new_day) + '.00:00',
    #                                              '%Y.%m.%d.%H:%M') - datetime.datetime.strptime(
    #     '2022.' + str(abyss_new_month if abyss_new_month == datetime.datetime.now().month else abyss_new_month - 1) + '.' + str(1 if datetime.datetime.now().day < 16 else 16) + '.00:00',
    #     '%Y.%m.%d.%H:%M')
    # bg_draw.text((337, 1358), f"{abyss_new.days}/{abyss_new_total.days}", fill='white',
    #              font=get_font(48, 'number.ttf'))
    # bg_draw.text((745, 1358), f"本期深渊还有{abyss_new.days if abyss_new.days <= abyss_new_total.days else abyss_new_total.days}天结束", fill='white',
    #              font=get_font(40, '优设标题黑.ttf'))
    # bg_img.alpha_composite(await draw_ring(abyss_new.days / abyss_new_total.days), (100, 1249))
    # 宝钱文字
    bg_draw.text((200, 500), f"{data['current_home_coin']}/{data['max_home_coin']}", fill='#7b8386',
                 font=get_font(30, 'HYWenHei-85W.ttf'))
    if data['current_home_coin'] == data['max_home_coin']:
        bg_draw.text((201, 535), f"洞天宝钱满了哦~", fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
    else:
        recover_time = datetime.datetime.now() + datetime.timedelta(seconds=int(data['home_coin_recovery_time']))
        recover_time_day = recover_time.day - datetime.datetime.now().day
        if recover_time_day == 1:
            recover_time_day_str = '明天'
        elif recover_time_day == 0:
            recover_time_day_str = '今天'
        else:
            recover_time_day_str = str(recover_time.day) + '日'
        recover_time_str = f'将于{recover_time_day_str}{recover_time.strftime("%H:%M")}达到上限~'
        bg_draw.text((201, 535), recover_time_str, fill='#7b8386', font=get_font(12, 'HYWenHei-55W.ttf'))
    # 派遣情况
    exp = data['expeditions']
    if exp:
        i = 0
        for role in exp:
            role_avatar = Path() / 'data' / 'LittlePaimon' / 'res' / 'avatar_side' / \
                          role['avatar_side_icon'].split('/')[-1]
            role_avatar = await aiorequests.get_img(url=role['avatar_side_icon'], size=(65, 65), mode='RGBA',
                                                    save_path=role_avatar)
            bg_img.alpha_composite(role_avatar, (533, 72 * i +112))
            if role['status'] == 'Ongoing':
                # hour = int(role['remained_time']) // 3600
                #
                # minute = int(role['remained_time']) % 3600 // 60
                finish_sec = int(role['remained_time'])
                finish_time = datetime.datetime.now() + datetime.timedelta(seconds=finish_sec)
                finish_day = finish_time.day > datetime.datetime.now().day and '明天' or '今天'
                finish_str = f'{finish_day}{finish_time.strftime("%H:%M")}'
                bg_draw.text((615, 72 * i + 142), f"{finish_str}完成", fill='#7b8386',
                             font=get_font(18, 'HYWenHei-55W.ttf'))
            else:
                bg_draw.text((615, 72 * i + 142), "已完成", fill='#7b8386',
                             font=get_font(18, 'HYWenHei-55W.ttf'))
            i += 1
        max_time = int(max([s['remained_time'] for s in exp]))
        if max_time == 0:
            bg_draw.text((580, 90), "探索派遣已全部完成", fill='#7b8386',
                             font=get_font(30, 'HYWenHei-85W.ttf'))
        else:
            last_finish_time = datetime.datetime.now() + datetime.timedelta(seconds=max_time)
            last_finish_day = last_finish_time.day > datetime.datetime.now().day and '明天' or '今天'
            last_finish_str = f'{last_finish_day}{last_finish_time.strftime("%H:%M")}'
            bg_draw.text((580, 90), f"最快将于{last_finish_str}完成", fill='#7b8386',
                             font=get_font(30, 'HYWenHei-85W.ttf'))
    else:
        bg_draw.text((580, 90), "没有进行探索派遣", fill='#7b8386',
                             font=get_font(30, 'HYWenHei-85W.ttf'))
    role_img = load_image(random.choice(list((res_path / 'emoticons').iterdir())), size=1, mode='RGBA')
    bg_img.alpha_composite(role_img, (330, 645))

    return MessageBuild.Image(bg_img, size=1, quality=100, mode='RGB')
