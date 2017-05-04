# language: zh-CN
# Created by applewu at 6/21/16
特性: 删除邮件

  场景: 根据邮件标题删除某一封指定邮件
    首先 发送一封主题为Mail_Should_Be_Removed的邮件给自己
    当 用户进入收件箱
    并且 勾选邮件标题为Mail_Should_Be_Removed前方的多选框
    并且 点击删除按钮
    那么 页面提示删除成功