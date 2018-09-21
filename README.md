本项目是一个Http/Https代理获取程序。

代理来自于开源项目<a href ="https://github.com/fate0/proxylist">proxylist</a>

文件会自动读取上述开源项目的Proxy代理列表，将其输出的JSON转换为三种可用的文档

第一种文档：协议名：//IP：Port 对应的文件是listall.txt 输出样例：http://175.45.176.68:80

第二种文档：通用代理软件模式。对应的文件是listipport.txt 输出样例 175.45.177.130:8080

第三种文档：CSV格式，方便在Excel里直观的选择你所想要的数据，内含IP地址，端口，代理类型，国家，响应时间。

