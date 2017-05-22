package Login.test;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.*;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;
import cucumber.api.java.en.*;
import cucumber.api.java.*;
import static org.junit.Assert.assertEquals;

public class LoginStepDefs {

	protected WebDriver driver;

	@Before
	public void setUp() {
		driver = new FirefoxDriver();
	}

	@Given("the browser access the login page")
	public void the_browser_access_the_login_page() {
		driver.get("http://mail.163.com/");
	}

	@When("the user enters the correct user_name (.*)$")
	public void the_user_enters_the_correct_user_name(String username) {
		driver.findElement(By.id("idInput")).sendKeys(username);
	}

	@And("the user enters the correct password (.*)$")
	public void the_user_enters_the_correct_password(String pwd) {
		driver.findElement(By.id("pwdInput")).sendKeys(pwd);
	}

	@And("the user click the login button")
	public void the_user_click_the_login_button() {
		driver.findElement(By.id("loginBtn")).click();
	}

	@Then("the result (.*) will be displayed")
	public void the_user_login_successfully(String addr) {

		(new WebDriverWait(driver, 5)).until(new ExpectedCondition<Boolean>() {
			public Boolean apply(WebDriver d) {
				return d.getTitle().toLowerCase()
						.startsWith("网易邮箱");
			}
		});
		WebElement addr_element = driver.findElement(By.id("spnUid"));
		assertEquals(addr_element.getText(), addr);
	}

	@After
	public void tearDown() {
		driver.close();
	}
}