#coding=utf-8
import qrcode
import codecs
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# qrcode lib:
# https://pypi.python.org/pypi/qrcode
#
# TODO
# - put Chinese char at the center of the QR code image?
#   better to put below it
# - Add a QR code for 汉语拼音方案 http://www.zdic.net/appendix/f8.htm
# - The code should accept parameters
#   like, make png: generate PNG files
#         make pdf: generate PDF files

# Ideas
# - use short URL, smaller image
# - The Chinese Characters can be store in a text file then python open
#   then process the chars


# 人教版一年级上册识字表(1)
# 10x8
char_tab1 = [
'天地人你我他一二',
'三四五上下口耳目',
'手足站坐日月水火',
'山石田禾对云雨风',
'花鸟虫六七八九十',
'爸妈马土不画打棋',
'鸡字词语句子桌纸',
'文数学音乐妹奶白',
'皮小桥台雪儿草家',
'是车羊走也秋气了']

# 人教版一年级上册识字表(2)
# 10x8
char_tab2 = [
'树叶片大飞会个的',
'船两头在里看见闪',
'星江南可采莲鱼东',
'西北尖说春青蛙夏',
'弯就冬男女开关正',
'反远有色近听无声',
'去还来多少黄牛只',
'猫边鸭苹果杏桃书',
'包尺作业本笔刀课',
'早校明力尘从众双']

# 人教版一年级上册识字表(3)
# 10x7
char_tab3 = [
'木林森条心升国',
'旗中红歌起么美',
'丽立午晚昨今年',
'影前后黑狗左右',
'它好朋友比尾巴',
'谁长短把伞兔最',
'公写诗点要过给',
'当串们以成彩半',
'空问到方没更绿',
'出睡那海真老师']

# 人教版一年级上册识字表(4)
# 10x7
char_tab4 = [
'吗同什才亮时候',
'觉得自己很穿衣',
'服快蓝又笔着向',
'和贝娃挂活金哥',
'姐弟叔爷群竹牙',
'用几步为参加洞',
'乌鸦处找办旁许',
'法放进高住孩玩',
'吧发芽爬呀久回',
'全变工厂医院生']


char_tab_list = [char_tab1, char_tab2, char_tab3, char_tab4]


"""
for x in charlist1:
    for y in x.decode("utf-8"):
        print y
"""

# zdic PC version
# url_header = 'http://www.zdic.net/z/17/js/'
# url_tail = '.htm'

# zdic touch screen device version
# url_header = 'm.zdic.net/z/?u=' # without http://, only works for some browsers.
url_header = 'http://m.zdic.net/z/?u='


#------------------------------------------------
# Chinese char to string format of UTF-16 number
# eg. '天' --> '5929'
#------------------------------------------------
def ch2utf16(ch):
    str1 = str(hex(ord(ch)))
    utf16_str  = str1[2:6] # throw the prefix 0x
    return utf16_str

def gen_tab(tab):
    i = 0
    j = 0
    for e in tab:
        i = i + 1
        j = 0
        ch_str = e.decode("utf-8") # we get string in UTF-8
        ch_list = list(ch_str)     # now we get list, like [u'\u5929', u'\u5730', u'\u4eba', u'\u4f60', u'\u6211', u'\u4ed6', u'\u4e00', u'\u4e8c']
        for e in ch_list:
            j = j + 1
            url = url_header + ch2utf16(e)
            print url

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L, # M or L?
                box_size=2,
                border=0,
            )

            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image()
            filename = str(i) + "_" + str(j) + ".png" # name format is RowNo_ColNo.png 0_0.png, 0_1.png
            print filename
            image_file = open(filename,'w+')
            img.save(image_file, "PNG")

'''
600 dots/inch
600 dots/25.4mm
每个像素 = 25.4mm/600 = 0.0423
'''

'''
For example, for the 10x8 character table

   _______________________
  |   _____    _____
  |  |     |  |     |
  |  | 1,1 |  | 1,2 | ...
  |  |_____|  |_____|
  |
  .     .        .
  .     .        .
  .     .        .
  |   _____    _____
  |  |     |  |     |
  |  |10,1 |  |10,2 | ...
  |  |_____|  |_____|
  |
  |_______________________
  .
 /|\
  |
  +------- Lower left of the PDF page

'''


def emit_pdf(filename, tab, row, col):
    gen_tab(tab)
    # draw the generated Code on a PDF Canvas
    c = canvas.Canvas(filename)

    # add images in a loop
    for x in range (1, col+1):
        for y in range (1, row+1):
            filename = str(row+1 - y) + "_" + str(x) + ".png"
            print filename
            c.drawImage(filename, x*17*mm, y*17*mm, 15*mm, 15*mm)

    c.showPage()
    c.save()

# TODO
# use a better data structure, eg Dict?

emit_pdf('char_tab_01.pdf', char_tab_list[0], 10, 8)
emit_pdf('char_tab_02.pdf', char_tab_list[1], 10, 8)
emit_pdf('char_tab_03.pdf', char_tab_list[2], 10, 7)
emit_pdf('char_tab_04.pdf', char_tab_list[3], 10, 7)

