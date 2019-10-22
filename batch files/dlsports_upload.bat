@echo off

"C:\Program Files (x86)\WinSCP\WinSCP.com" ^
  /command ^
    "open ftp://squash9:V%%40774*OjS2eA@squashsource.com/" ^
    "lcd F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct" ^
    "cd /public_html/wp-content/uploads/wpallimport/files" ^
    "put dlsports.csv" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)

START "" "https://www.squashsource.com/wp-admin/admin.php?page=pmxi-admin-manage&id=12&action=update"

exit /b %WINSCP_RESULT%
