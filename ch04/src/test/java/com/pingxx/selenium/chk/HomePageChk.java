package com.pingxx.selenium.chk;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

import org.testng.Assert;

public class HomePageChk extends BaseChk{

	/**
	 * 通过判断登录后页面显示的信息是否有 “LogOff” 字符串来判断是否登录成功
	 * @param driver
	 * @param id
	 */
	public void loginChk(WebDriver driver, String id){
		String logoff = driver.findElement(By.id(id)).getText();
		Assert.assertEquals("LogOff",logoff);
	}
}
