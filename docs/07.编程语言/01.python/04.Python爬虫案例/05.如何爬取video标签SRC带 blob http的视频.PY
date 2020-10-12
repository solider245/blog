大家好，我是烤鸭：

    之前玩爬虫的时候，看到过video标签中src属性引入的blob:http:xxxx，当时没找到解决思路，今天又遇到类似问题，就试着找了一下。

这是有人问过 [https://vimeo.com/](https://vimeo.com/) 这个网站的视频怎么下载。
      [https://superuser.com/questions/1033563/how\-to\-download\-video\-with\-blob\-url?answertab=votes](https://superuser.com/questions/1033563/how-to-download-video-with-blob-url?answertab=votes)

## 1.   分析

    以这个网址为例：
[https://open.gaodun.com/%E5%90%8D%E5%AE%B6%E8%AE%B2%E5%9D%9B/21.html](https://open.gaodun.com/%E5%90%8D%E5%AE%B6%E8%AE%B2%E5%9D%9B/21.html)

![](https://img-blog.csdn.net/20180914165442366?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FuZ3J5X01pbGxz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

看video标签中的src属性，发现
src="blob:https://open.gaodun.com/b9d3366f\-87ef\-4328\-9d97\-31110de519a1"

复制这个地址去浏览器什么也找不到。

## 2.   找真实地址

不管上面的问题。先去看一下视频到底从哪来的。以谷歌浏览器为例，选择XHR，发现加载了m3u8文件。

![](https://img-blog.csdn.net/20180914165620463?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FuZ3J5X01pbGxz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

m3u8是一种视频格式，看response中返回的.ts文件，直接复制ts文件的路径打开，就是视频片段。

![](https://img-blog.csdn.net/20180914165805148?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FuZ3J5X01pbGxz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

到这，文件其实已经找到了。但是video中的blob:https://xxxx是什么呢，是怎么找到的文件。
这篇文章给了解释。
        [https://blog.csdn.net/xingyun89114/article/details/80699527](https://blog.csdn.net/xingyun89114/article/details/80699527)
简单来说就是视频对象做了个标记，src指向的是标记。

## 3.     找关联

当我对着源码和请求的response对照的时候，发现播放器周围的html标签都是后生成的，找到了一个比较“可疑”的js文件。

![](https://img-blog.csdn.net/20180914165831108?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FuZ3J5X01pbGxz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

发现播放器代码附近的：

```javascript
<div class="playDiv" id="divid"> <script type="text/javascript" src="https://s.gaodun.com/web/static-player/loader.js?13p9Wv580v1a!!fs-3"></script> </div>
```

看了js的源码，再跟了下debug。

![](https://img-blog.csdn.net/20180914165954744?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FuZ3J5X01pbGxz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

找到了这个网页请求的m3u8地址是这个：https://vod.gaodun.com/13p9Wv580v1a!!fs/SD/1.m3u8。

![](https://img-blog.csdn.net/20180914170021159?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0FuZ3J5X01pbGxz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

直接浏览器访问就可以获取，就可以获取ts文件。ts文件就是一段段的视频，可以下载下来之后拼接成一个完整的文件。

## 4.     总结

    至此，关于video 标签 src 带有blob:http的 抓取的就写完了。但是每个网站的情况都不一样。

这里只是提供一种思路，比如刚开始写的 [https://vimeo.com/](https://vimeo.com/) 这个网站就不是js，而是json里边包含的视频地址。

欢迎有想法的朋友多交流。