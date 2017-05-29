package com.pingxx.selenium.chk;

import org.testng.Assert;

public class BaseChk {

	/**
	 * msg 中是否包含指定的 字符串 errorMsg
	 * @param msg
	 * @param errorMsg
	 */
	public void errorChk(String msg, String errorMsg){
		Assert.assertTrue(msg.contains(errorMsg));
	}
}
