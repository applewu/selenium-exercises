# language: zh-CN
# Created by applewu at 6/20/16

特性: 用163邮箱发送邮件
  # Enter feature description here

  场景: 发送一封主题为 Lettuce Selenium测试 的邮件给自己
    首先 用户使用正确的用户名hellotester@163.com密码xxxxxxxxxxxx登陆
    当 用户点击写信按钮
    并且 输入当前用户的邮箱地址，作为收件人地址
    并且 输入邮件主题为 Lettuce Selenium测试
    并且 输入邮件正文 这是脚本发送的邮件，可以删除
    并且 点击发送按钮
    那么 页面提示发送成功
