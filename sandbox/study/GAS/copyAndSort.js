// copy with range specification from a specific Sheet in other Spreadsheet.
function copyAndSort() {
  var ss = SpreadsheetApp.openById("SpreadsheetID"); // fill SpreadsheetID
  var sheet = ss.getSheetByName("SheetName") // fill SheetName
  var startRow = 2;  // とってくるデータの最初の行
  var lastRow = sheet.getLastRow();   // 最後の行
  var dataRange = sheet.getRange(startRow, 1, lastRow - startRow, 5) //最初の2つがはじまりのセルで最後の2つが終わりのセル 5は最後のColumn
  var data = dataRange.getValues(); 
   
  var newSs = SpreadsheetApp.getActiveSpreadsheet();
  var newSheet = newSs.getSheets()[1];
  newSheet.getRange(2, 1, data.length, data[0].length).setValues(data);
  newSheet.sort(5);  //5の列で昇順にソート
}
