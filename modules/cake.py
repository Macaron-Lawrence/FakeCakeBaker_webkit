from re import template
from jinja2 import Environment, FileSystemLoader
import imgkit
import os

BASE = "file:///" + os.path.abspath('.').replace("\\","/") + "/view"


class Cake(object):
    # def __init__(self, txtsrc):
    #     self.bline = 70
    #     self.bline_text = 80
    #     self.width = 2480
    #     self.imgarray = [header(self.width)]
    #     self.txt = self.fromtxt(txtsrc)
    #     self.cake = None

    def getJinja2(self, txt):
        txt = txt.split('\n')
        content = {
            "text_in_line":[],
            "time":""
        }
        for line in txt:
            if line[0:3] == "###":
                content["text_in_line"].append(
                    {"form": "title", "content": line[3:]})
            elif line[0:3] == "{{{":
                content["text_in_line"].append(
                    {"form": "image", "content": BASE + "/static/image/" + line[3:]})
            elif line == "<br>":
                content["text_in_line"].append({"form": "br", "content": line})
            else:
                content["text_in_line"].append({"form": "p", "content": line})
        content['time'] = "2020年10月7日"
        env = Environment(loader= FileSystemLoader('./view/'))
        template = env.get_template('article_text.html')
        return template.render(obj = content, BASE = BASE)


    def html2jpg(self,txt):
        cfg = imgkit.config(wkhtmltoimage = "./modules/wkhtmltoimage.exe")
        opt = {'enable-local-file-access' : "",
               'encoding': "UTF-8",
               "enable-javascript":"",
            'debug-javascript':"",
            "javascript-delay": 1000,

            'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ]}
        data = self.getJinja2(txt)
        imgkit.from_string(data, 'out.png', config=cfg, options=opt)


i = Cake()

txt = """
###[活动预告]故事集「红松林」即将开启
{{{1.jpg
<b>一、全新故事集「红松林」限时开启</b>
<b>关卡开放时间：</b>10月15日 16:00 - 10月22日 03:59
<b>关卡解锁条件：</b>通关主线1-10
<b>关卡掉落：</b>松果印章、素材等
<b>活动说明：</b>活动期间将限时开放「红松林」活动关卡，玩家可通过活动作战收集【松果印章】后在【松林集会地】中兑换活动奖励及事相碎片。事相碎片可用于当期及往期故事集的剧情解锁
<b>【松林集会地】兑换时间：</b>10月15日 16:00 - 10月25日 03:59
<b>【松林集会地】兑换奖励：</b><red>【★★★★★：焰尾】</red><red>【巫异盛宴】系列 -  安息处的怪盗 - 卡达</red>、<red>事相碎片</red>、家具零件、作战记录、招聘许可、高级素材等
<br>
注意：本次活动结束后该故事集将收录至【情报处理室】中
{{{2.png
<b>二、【追影逐光】限时寻访开启</b>
<b>活动时间：</b>10月15日 16:00 - 10月29日 03:59
<b>活动说明：</b>活动期间【追影逐光】限时寻访开启，该寻访中以下干员出现率上升
<red>★★★★★★：苍羽</red>（占6★出率的50%）
<red>★★★★★：焰尾 / 临光</red>（占5★出率的50%）
<br>
注意：本次活动【追影逐光】寻访为【标准寻访】
{{{3.jpg
<b>三、新干员登场，【标准寻访】常驻</b>
<b>新增干员：</b>以下新增干员除加入【追影逐光】寻访外，将在10月28日04:00后加入并常驻其余【标准寻访】卡池
<red>★★★★★★：苍羽</red>
<red>★★★★★：焰尾</red>
<br>
注意：
◆新增干员<red>【焰尾】</red>仅在「红松林」活动中获取，暂不加入【追影逐光】及任何【标准寻访】
◆本次活动关卡开放期间以上新增干员信赖获取提升
{{{4.png
<b>四、【巫异盛宴】系列，新装限时上架</b>
<b>活动时间：</b>10月15日 16:00 - 10月29日 03:59
<b>活动说明：</b>活动期间以下干员新增时装将在时装商店上架并进行限时贩售：
◆<red>【巫异盛宴】系列 - 铸剑村的神匠 - 瑕光</red>
◆<red>【巫异盛宴】系列 - 复活点的勇者 - 雪雉</red>
{{{5.png
<b>五、新增【卡西米尔森林小屋】主题家具，限时上架</b>
<b>家具商店贩售时间：</b>10月15日 16:00 - 10月29日 03:59
{{{6.jpg
<b>六、特别行动记述【记录修复】功能开启</b>
该功能开启后，可以挑战特别行动记述的对应关卡来获取对应的活动限定奖励内容（【干员的私人信件】、【家具收藏包】、活动奖励头像），本次将同步开放【战地秘闻】活动限定奖励常驻获取。
同时，本次还将同步开放【骑兵与猎人】活动限定奖励常驻获取。
<br>
更多活动内容请持续关注《罗德岛蜜饼工坊》。
"""

i.html2jpg(txt)

