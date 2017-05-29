package com.pingxx.selenium.lib;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxProfile;

public class Common {
	/**
	 * 创建 firefox 的 WebDriver
	 * 
	 * @return WebDriver
	 */
	public WebDriver browserFirefox() {
		FirefoxProfile profile = new FirefoxProfile();
		profile.setEnableNativeEvents(false);
		WebDriver driver = new FirefoxDriver();// 实例化WebDriver
		driver.manage().window().maximize();
		return driver;
	}

	/**
	 * 登录系统
	 * 
	 * @param driver
	 */
	public void login(WebDriver driver, String username, String pwd) {
		driver.findElement(By.id("email")).sendKeys(username);
		driver.findElement(By.id("pwd")).sendKeys(pwd);
		driver.findElement(By.id("btn_login")).submit();
	}

	/**
	 * 登出系统
	 * 
	 * @param driver
	 */
	public void logout(WebDriver driver) {
		driver.findElement(By.id("btn_logout")).click();
	}

	/**
	 * 退出 driver
	 * 
	 * @param driver
	 */
	public void driverQuit(WebDriver driver) {
		driver.quit();// 退出
	}
}
