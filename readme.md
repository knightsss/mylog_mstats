1.登陆采用POST请求，后续考虑异步请求。

2.数据库字段加密采用django自带的加密方式。

3.数据库连接使用本地的数据库。

4.权限单独设计一张表，通过用户权限表将用户表和权限表关联。

5.测试可以通过http://192.168.8.206:8005/login/访问，测试前需要在内网启动django服务。

6.主界面开发完成，图表使用echarts，柱状图和饼状图，框架使用bootstrap。

7.数据收集通过ajax的异步请求，通过http的get方式获取数据，目前只是预留获取的方式，具体数据后续完成。

8.新增数据监控界面，通过折线图实时展示。

9.每张图形通过异步请求获取数据，没5s更新一次。
