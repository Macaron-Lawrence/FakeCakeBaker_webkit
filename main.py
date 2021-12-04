from modules.cake import Cake
txt = ""
txtpath = "./input/main.txt"

with open (txtpath, 'r',encoding='utf-8' ) as F:
    txt = F.read()


cake = Cake(txt, "2021年11月11日")


cake.render('output.png')