// copy from other Sheet in same Spreadsheet.
function copy() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheets()
  var data = sheet.getDataRange().getValues();
  var newSheet = ss.getSheets()[1];
  newSheet.getRange(1, 1, data.length, data[0].length).setValues(data);
}