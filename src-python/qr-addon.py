#coding=utf-8
import qrcode
import codecs

# https://pypi.python.org/pypi/qrcode
# TODO
# - use short URL, smaller image
# - read Chinese char, use Unicode to generate the zdic URL
# - put all QR code on an A4 paper
# - put Chinese char at the center of the QR code image?

# IDEAS
# - The Chinese Characters can be store in a text file then python open
#   then process the chars
# - can also use the heredoc

charlist = ['天', '地', '人', '你', '我', '他', '一', '二']

# 人教版一年级上册识字表(1)
"""
天地人你我他一二
三四五上下口耳目
手足站坐日月水火
山石田禾对云雨风
花鸟虫六七八九十
爸妈马土不画打棋
鸡字词语句子桌纸
文数学音乐妹奶白
皮小桥台雪儿草家
是车羊走也秋气了
"""

# 人教版一年级上册识字表(2)
"""
树叶片大飞会个的
船两头在里看见闪
星江南可采莲鱼东
西北尖说春青蛙夏
弯就冬男女开关正
反远有色近听无声
去还来多少黄牛只
猫边鸭苹果杏桃书
包尺作业本笔刀课
早校明力尘从众双
"""

# 人教版一年级上册识字表(3)
"""
木林森条心升国
旗中红歌起么美
丽立午晚昨今年
影前后黑狗左右
它好朋友比尾巴
谁长短把伞兔最
公写诗点要过给
当串们以成彩半
空问到方没更绿
出睡那海真老师
"""

# 人教版一年级上册识字表(4)
"""
吗同什才亮时候
觉得自己很穿衣
服快蓝又笔着向
和贝娃挂活金哥
姐弟叔爷群竹牙
用几步为参加洞
乌鸦处找办旁许
法放进高住孩玩
吧发芽爬呀久回
全变工厂医院生
"""

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

url_base = 'http://www.zdic.net/z/17/js/'
url_tail = '.htm'

# here we need a loop

a = charlist[0].decode("utf-8")
b = str(hex(ord(a)))
c = b[2:6]
d = url_base + c + url_tail
print d

# qr.add_data('http://www.zdic.net/z/17/js/5929.htm')
qr.add_data(d)
qr.make(fit=True)

img = qr.make_image()
# should encode the sequence number and unicode in the image file name
# for the further image processing
img.save("tian_qrcode.png")


