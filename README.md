## PYQT5 电商小工具
项目结构
- ToolUI.py
</br>主界面程序代码，使用PYQT5的designer产生的文件（ToolUI.ui）转换成的python代码
- ToolFuncs.py
</br>主要的函数部分，将界面与函数结合起来
- APIs.py
</br>爬虫API类，负责爬虫的运行，供主代码调用接口
- QSSwhite.py
</br>QSS代码，本来应该放在一个.css文件中调用的，但是打包之后调用不了，所以封装成Python文件直接调用，这样有个弊端就是打包之后不能随意换风格样式了。
- ToolUI.ui
</br>PYQT5的模板文件，可以转换成py文件
- White
</br>放置程序主界面及QSS调用的图片，只用到了一部分，但是懒得删其他的了
- 其他文件（可以自定义的）
    - PICs
    </br>一个存放下载图片的文件夹，是程序第三个模块默认存放图片的文件夹，可以按照保存路径的设置自行更改
    - dsr_ids.txt
    </br>程序第一个模块默认读取ID的文件，可以根据实际需求更改名称
    - link_ids.txt
    </br>程序第二个模块默认读取ID的文件，可以根据实际需求更改名称
    - img_links.txt
    </br>程序第三个模块默认读取链接的文件，可以根据实际需求更改名称

项目功能
- 参见程序的各个模块的说明

项目运行
- 按照每个模块的“操作流程”中的指示操作就行，很简单，不做解释
</br>直接放图看效果吧
- 三个模块的不同界面：
![头衔饼形图](https://github.com/Hopetree/TMTools/doc/001.png)
![头衔饼形图](https://github.com/Hopetree/TMTools/doc/002.png)
![头衔饼形图](https://github.com/Hopetree/TMTools/doc/003.png)
- 整体界面效果GIF动图：
![头衔饼形图](https://github.com/Hopetree/TMTools/doc/000.gif)
- 第一个模块操作效果的GIF动图：
![头衔饼形图](https://github.com/Hopetree/TMTools/doc/001.gif)


程序打包
- Pyinstaller
</br>打包方法：http://www.cnblogs.com/gopythoner/p/6337543.html

转载说明
- 只支持Fork，不支持其他形式转载，谢谢！
