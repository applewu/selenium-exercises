# -*- coding:utf-8 -*-
# language: zh-CN

# Created by applewu at 6/14/16
特性: 登陆163邮箱
  从163邮箱首页登陆

  场景: 用户使用正确的用户名密码登陆
    首先 用户访问163邮箱首页
    当 用户输入用户名wuziteng2006@163.com
    并且 用户输入密码Password01!
    并且 用户点击登录按钮
    那么 用户wuziteng2006@163.com会登录成功

#  场景模板: 用户使用错误的信息登录
#    首先 用户访问163邮箱首页
#    当 用户输入用户名 <user_name>
#    并且 用户输入密码 <password>
#    并且 用户点击登录按钮
#    那么 用户会登录成功
#
#  例如:
#    | user_name | password |
#    | 0         | 1      |
#    | 1         | 1      |
#    | 2         | 2      |