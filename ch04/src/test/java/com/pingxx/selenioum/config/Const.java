package com.pingxx.selenioum.config;

public class Const {
	// This is the list of System Variables
	// Declared as 'public', so that it can be used in other classes of this
	// project
	// Declared as 'static', so that we do not need to instantiate a class
	// object
	// Declared as 'final', so that the value of this variable can be changed
	// 'String' & 'int' are the data type for storing a type of value
	public static final String URL = "http://www.dashboard.com";
	public static final String Path_TestData = "C:\\Workspace\\PGS\\src\\main\\java\\dataEngine\\DataEngine.xlsx";
	public static final String Path_OR = "C:\\Workspace\\PGS\\src\\main\\java\\config\\OR.txt";
	public static final String File_TestData = "DataEngine.xlsx";

	// List of Data Sheet Column Numbers
	public static final int Col_TestCaseID = 0;
	public static final int Col_TestScenarioID = 1;
	// This is the new column for 'Page Object'
	public static final int Col_PageObject = 3;
	// This column is shifted from 3 to 4
	public static final int Col_ActionKeyword = 4;
	// Test case sheet name
	public static final int Col_TestCaseSheetName = 1;

	public static final int Col_RunMode = 3;

	// New entry in Constant variable
	public static final String Sheet_TestCasesList = "TestCases";
	// List of Test Data
	public static final String UserName = "testuser_3";
	public static final String Password = "Test@123";
}
