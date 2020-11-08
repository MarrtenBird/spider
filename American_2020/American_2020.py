import parsel
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')                                        # 创建浏览器对象

driver.get('http://datanews.caixin.com/interactive/2020/us-president-election/')     # 使用对象打开网址


data = driver.page_source                                                           # 获得网页渲染后的代码

html = parsel.Selector(data)                                                         # 吧渲染好的源代码转换成树对象

MuBiao = html.xpath('//div[@class="us-detail homepage"]/div[@class="chart"]/svg/g')[-1]    # 使用xpath语句，获得最后的一个g标签（返回的是列表，所以可以[-1]

ZhiChi_list = MuBiao.xpath('./rect/@value')                                                 # 对最后一个g标签内部的值进行处理
# print(zc)

for i in ZhiChi_list:
    #print(i.get())                                                                 # 为了检测是不是想要获取的数据

    with open('民调.csv','a',encoding='utf8') as f:                                 #  保存文件到本地
        f.write(i.get())
        f.write('\n')





