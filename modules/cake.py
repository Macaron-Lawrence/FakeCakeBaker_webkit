from re import template
from jinja2 import Environment, FileSystemLoader
import imgkit
import os

BASE = "file:///" + os.path.abspath('.').replace("\\","/")


class Cake(object):
    def __init__(self, txt, time):
        self.txt = txt
        # self.imagepath = imagepath,
        self.time = time

    def render(self, path, option = ""):
        self.html2jpg(self.getJinja2(self.txt), path)

    def getJinja2(self, option = ""):
        txt = self.txt.split('\n')
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
                    {"form": "image", "content": BASE + "/input/" + line[3:]})
            elif line == "<br>":
                content["text_in_line"].append({"form": "br", "content": line})
            else:
                content["text_in_line"].append({"form": "p", "content": line})
        content['time'] = self.time
        env = Environment(loader= FileSystemLoader('./view/'))
        template = env.get_template('article_text.html')
        return template.render(obj = content, BASE = BASE)


    def html2jpg(self, data, path):
        cfg = imgkit.config(wkhtmltoimage = "./modules/wkhtmltoimage.exe")
        opt = {'enable-local-file-access' : "",
               'encoding': "UTF-8",
               "enable-javascript":"",
            'debug-javascript':"",
            "javascript-delay": 1000,
            'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ]}
        data = data ##self.getJinja2(txt)
        imgkit.from_string(data, path, config=cfg, options=opt)
