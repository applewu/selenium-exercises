package com.pingxx.selenium.util;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFFormulaEvaluator;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import com.pingxx.selenioum.config.Const;

public class ExcelUtil {
	private static XSSFSheet ExcelWSheet;
	private static XSSFWorkbook ExcelWBook;
	private static XSSFCell Cell;

	/**
	 * This method is to set the File path and to open the Excel file Pass Excel
	 * Path and SheetName as Arguments to this method
	 * 
	 * @param Path
	 * @throws Exception
	 */
	public static void setExcelFile(String Path) throws Exception {
		FileInputStream ExcelFile = new FileInputStream(Path);
		ExcelWBook = new XSSFWorkbook(ExcelFile);
	}

	/**
	 * This method is to read the test data from the Excel cell In this we are
	 * passing Arguments as Row Num, Col Num & Sheet Name
	 * 
	 * @param RowNum
	 * @param ColNum
	 * @param SheetName
	 * @return String
	 * @throws Exception
	 */
	public static String getCellData(int RowNum, int ColNum, String SheetName) throws Exception {
		ExcelWSheet = ExcelWBook.getSheet(SheetName);
		try {
			Cell = ExcelWSheet.getRow(RowNum).getCell(ColNum);
			String CellData = Cell.getStringCellValue();
			return CellData;
		} catch (Exception e) {
			return "";
		}
	}

	// This method is to get the row count used of the excel sheet
	public static int getRowCount(String SheetName) {
		ExcelWSheet = ExcelWBook.getSheet(SheetName);
		int number = ExcelWSheet.getLastRowNum();
		return number;
	}

	// This method is to get the Row number of the test case
	// This methods takes three arguments(Test Case name , Column Number & Sheet
	// name)
	public static int getRowContains(String sTestCaseName, int colNum, String SheetName) throws Exception {
		int i;
		ExcelWSheet = ExcelWBook.getSheet(SheetName);
		int rowCount = ExcelUtil.getRowCount(SheetName);
		for (i = 0; i < rowCount; i++) {
			if (ExcelUtil.getCellData(i, colNum, SheetName).equalsIgnoreCase(sTestCaseName)) {
				break;
			}
		}
		return i;
	}

	/**
	 * This method is to get the count of the test steps of one test case 
	 * This method takes three arguments (Sheet name, Test Case Id and Test case row number)
	 * @param SheetName
	 * @param sTestCaseID
	 * @param iTestCaseStart
	 * @return test steps in total
	 * @throws Exception
	 */
	public static int getTestStepsCount(String SheetName, String sTestCaseID, int iTestCaseStart) throws Exception {
		for (int i = iTestCaseStart; i <= ExcelUtil.getRowCount(SheetName); i++) {
			if (!sTestCaseID.equals(ExcelUtil.getCellData(i, Const.Col_TestCaseID, SheetName))) {
				int number = i;
				return number;
			}
		}
		ExcelWSheet = ExcelWBook.getSheet(SheetName);
		int number = ExcelWSheet.getLastRowNum();
		return number;
	}

	/*
	 * row and column are all greater than or equal to 0
	 */
	public String get_Value_InSpecifiedCell_FromExcel(String ExcelPath, String sheetName, int row, int column) {
		String cellValue = "";
		try {
			File file = new File(ExcelPath);
			FileInputStream fis = new FileInputStream(file);
			// Get the workbook instance for XLS file
			XSSFWorkbook workbook = new XSSFWorkbook(fis);
			// Get the specified sheet from the workbook
			XSSFSheet sheet = workbook.getSheet(sheetName);
			if (sheet.getRow(row).getCell(column) != null) {
				XSSFCell cell = sheet.getRow(row).getCell(column);
				switch (cell.getCellType()) {
				case XSSFCell.CELL_TYPE_FORMULA:
					XSSFFormulaEvaluator evaluator = workbook.getCreationHelper().createFormulaEvaluator();
					evaluator.evaluateFormulaCell(cell);
					cellValue = String.valueOf((cell.getNumericCellValue()));
					cellValue = cellValue.substring(0, cellValue.length() - 2);
					break;
				case XSSFCell.CELL_TYPE_STRING:
					cellValue = cell.getStringCellValue();
					break;
				case XSSFCell.CELL_TYPE_NUMERIC:
					cellValue = String.valueOf((cell.getNumericCellValue()));
					cellValue = cellValue.substring(0, cellValue.length() - 2);
					break;
				}
			}
			fis.close();
		} catch (NullPointerException e) {
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return cellValue;
	}

	/*
	 * Add value mean set another value in the specified cell where there is no
	 * value createrow means create it as a new row, so there is no value or
	 * remove all values if there is createcell means create it as a new cell,
	 * so there is no value or remove all values if there is row and column are
	 * all greater than or equal to 0
	 */
	public void add_Value_InSpecifiedCell__FromExcel(String ExcelPath, String sheetName, int row, int column,
			String specifiedValue) {
		try {
			File file = new File(ExcelPath);
			FileInputStream fis = new FileInputStream(file);
			// Get the workbook instance for XLS file
			XSSFWorkbook workbook = new XSSFWorkbook(fis);
			// Get the specified sheet from the workbook
			XSSFSheet sheet = workbook.getSheet(sheetName);
			// Create a new cell
			sheet.getRow(row).createCell(column).setCellValue(specifiedValue);
			fis.close();
			FileOutputStream fos = new FileOutputStream(file);
			workbook.write(fos);
			fos.close();
		} catch (NullPointerException e) {
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	/*
	 * Add value mean set another value in the specified cell where there is no
	 * value You can't update the cell if you has remove the cell row and column
	 * are all greater than or equal to 0
	 */
	public void delete_Value_InSpecifiedCell__FromExcel(String ExcelPath, String sheetName, int row, int column) {
		try {
			File file = new File(ExcelPath);
			FileInputStream fis = new FileInputStream(file);
			// Get the workbook instance for XLS file
			XSSFWorkbook workbook = new XSSFWorkbook(fis);
			// Get the specified sheet from the workbook
			XSSFSheet sheet = workbook.getSheet(sheetName);
			sheet.getRow(row).removeCell(sheet.getRow(row).getCell(column));
			fis.close();
			FileOutputStream fos = new FileOutputStream(file);
			workbook.write(fos);
			fos.close();
		} catch (NullPointerException e) {
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	/*
	 * Update value mean set another value in the specified cell where there is
	 * value; You can update the cell if you has update the cell to "" row and
	 * column are all greater than or equal to 0
	 */
	public void update_Value_InSpecifiedCell__FromExcel(String ExcelPath, String sheetName, int row, int column,
			String specifiedValue) {
		try {
			File file = new File(ExcelPath);
			FileInputStream fis = new FileInputStream(file);
			// Get the workbook instance for XLS file
			XSSFWorkbook workbook = new XSSFWorkbook(fis);
			// Get the specified sheet from the workbook
			XSSFSheet sheet = workbook.getSheet(sheetName);
			sheet.getRow(row).getCell(column).setCellValue(specifiedValue);
			fis.close();
			FileOutputStream fos = new FileOutputStream(file);
			workbook.write(fos);
			fos.close();
		} catch (NullPointerException e) {
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
