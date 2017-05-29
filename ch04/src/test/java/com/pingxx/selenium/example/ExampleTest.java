package com.pingxx.selenium.example;

import static org.assertj.core.api.Assertions.*;

import org.testng.annotations.Test;
import com.pingxx.selenium.lib.Common;
import com.pingxx.selenium.util.*;
import org.testng.annotations.BeforeTest;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxProfile;
import org.testng.annotations.AfterTest;

public class ExampleTest {
	public WebDriver driver = null;
	public String url=null;
	Common common=new Common();  
	@BeforeTest
	public void beforeTest() {
		driver=common.browserFirefox();
		try {
			ExcelUtil.setExcelFile("../testDate.xlsx");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		url="https://www.dashboard.com";
	}
//	/**
//	 * 根据指定的订单号搜索订单
//	 */
//	@Test
//	public void searchSpecifiedOrderById() {
//		driver.get("https://www.dashboard.com");// 打开网页
//		common.login(driver);
//		driver.findElement(By.id("search")).click();
//		driver.findElement(By.id("order_id")).sendKeys("98909832451398");
//		driver.findElement(By.id("search_btn")).click();
//		common.logout(driver);
//	}
//	
//	/**
//	 * 根据指定的日期搜索订单
//	 */
//	@Test
//	public void searchSpecifiedOrderByDate() {
//		driver.get("https://www.dashboard.com");// 打开网页
//		common.login(driver);
//		driver.findElement(By.id("search")).click();
//		driver.findElement(By.id("date_From")).sendKeys("2016-07-07");
//		driver.findElement(By.id("date_To")).sendKeys("2016-07-08");
//		driver.findElement(By.id("search_btn")).click();
//		common.logout(driver);
//	}

	/**
	 * 根据指定的订单号搜索订单，数据存放在Excel中
	 * @throws Exception 
	 */
	@Test
	public void searchSpecifiedOrderByIdWithExcel() throws Exception {
		driver.get(url);// 打开网页
		//driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);
		common.login(driver,ExcelUtil.getCellData(1, 3, "testData01"),ExcelUtil.getCellData(1, 4, "testData01"));
		driver.findElement(By.id("search")).click();
		driver.findElement(By.id("order_id")).sendKeys(ExcelUtil.getCellData(2, 2, "testData01"));
		driver.findElement(By.id("search_btn")).click();
		assertThat(driver.findElement(By.id("orderid"))).isNotNull()
														.isEqualTo(ExcelUtil.getCellData(2, 2, "testData01"));
		common.logout(driver);
	}
	@AfterTest
	public void afterTest() {
		driver = null;
		common.driverQuit(driver);
	}
}
