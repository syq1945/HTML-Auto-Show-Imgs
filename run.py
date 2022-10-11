import os

path = r".\static\img"  # 文件夹路径

# p=os.getcwd()

# print(p)

# path = "./static/img"  # 文件夹路径
countlst = []
count = 0
pernum = 0
pernum1 = 0
num = 0
imgs = ""

for file in os.listdir(path):  # file 表示的是文件名
    count = count + 1
    imgi = r'            <img src="static/img/'+file+ \
        '" alt="" height="800px" width="1280px"> \n'
    imgs = imgs+imgi

strhtml = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Title</title>
    <!-- https://v3.bootcss.com/ -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css" />
    <!-- https://fontawesome.dashgame.com -->
    <link rel="stylesheet" href="static/plugins/font-awesome-4.7.0/css/font-awesome.css" />
    <!-- <link rel="stylesheet" href="static/css/style.css"> -->
    <link rel="stylesheet" href="static/css/tvshowpic.css">

    <style>
        .navbar {
            border-radius: 0px;
        }
    </style>
</head> 

<body>
    <!--html从这里开始写 -->
    <div id="tv">

        <div id="screen">
'''

strhtml = strhtml+imgs

strhtml1 = '''
        </div>
    </div>
    <!-- https://jquery.com/ -->
    <script src="static/js/jquery-3.6.1.min.js"></script>
    <!-- https://jquery.com/ 引入bootstrap的js -->
    <script src="static/plugins/bootstrap-3.4.1/js/bootstrap.min.js"></script>
    <!-- Javascript代码推荐位置: -->
    <script type="text/javascript">
        //利用jQuery中的功能实现某些效果
        //框架启动后, 就能运行的代码, 不用等所有都加载完, 可以节省些时间
        $(function ()
        {

        })
    </script>
</body>
</html>
'''

strhtml = strhtml+strhtml1

strcss1 = '''
body {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

#screen {
    width: 9999px;
    height: 9999px;
'''

while (1 == 1):
    str_least_time = input("您希望每个图片显示几秒钟, 请输入数字:")
    try:
        least_time = int(str_least_time)
        break
    except:
        print('请输入整数 数字 ')

strcss1 = strcss1 + "    animation: " + \
    str(count*least_time)+"s nshow infinite; "

strcss2 = '''
}
#screen img {
    float: left;
}

#tv {
    width: 1280px;
    height: 800px;
    overflow: hidden;
}
'''

strcss1 = strcss1 + strcss2

num = int(100 / count)
width = 1280
pxlst = []
for i in range(0, width * count, width):
    pxlst.append(i)

 
nshowhead = '''
@keyframes nshow {
    0% {}  
'''
 
nshowfoot = '''
}
'''

lstnshow = nshowhead

for i in range(0, count):
    n = i * num + 1
    n1 = (i+1) * num
    n0 = (i+1) * num

    pernum0 = "%.0f%%" % (n0)
    pernum = "%.0f%%" % (n)
    pernum1 = "%.0f%%" % (n1)
 
    if (i == 0):
        item0 = "    " + str(pernum0) + " { transform: translateX( 0px);  }"
        lstnshow = lstnshow + item0
    else:
        item = "\n    " + \
            str(pernum) + \
            " { transform: translateX(" + str(-pxlst[i]) + "px); }"
        item1 = "\n    " + \
            str(pernum1) + \
            " { transform: translateX(" + str(-pxlst[i]) + "px); }"
        lstnshow = lstnshow + item + item1
 
finallst = lstnshow + nshowfoot
strcss1 = strcss1 + finallst
# print(strcss1)
 
with open(r".\static\css\tvshowpic.css", "w+", encoding="utf-8") as f:
    f.write(strcss1)

print("*" * 72)
prcss = '* 文件已经生成".\static\css\\tvshowpic.css"  *'
print(prcss)

with open(r".\\1TV-Show.html", "w+", encoding="utf-8") as f1:
    f1.write(strhtml)

pr3 = '^-^ 您可以双击\\1TV-Show.html 这个文件来显示内容了.^-^'

print(pr3)
print("\n")
