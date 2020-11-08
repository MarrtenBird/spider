# Selenium

# 爬取网页中js动态加载的文件

使用调用浏览器对象，可视化爬取 selenium

需要用到的两个库：

selenium

parsel





本次目标是财经网，关于2020大选的民调数据；

这个数据是通过js后期加载到网页中的，在代码中可以看到这里有大量的<g>标签

![image-20201108190230684](C:\Users\MarrtenBird\AppData\Roaming\Typora\typora-user-images\image-20201108190230684.png)



但是到源代码中，却没有

![image-20201108190301951](C:\Users\MarrtenBird\AppData\Roaming\Typora\typora-user-images\image-20201108190301951.png)



所以我判断这段文字是动态后期加载上来的

