@echo off

"C:\Program Files (x86)\WinSCP\WinSCP.com" ^
  /command ^
    "open ftp://squash9:3QSgJl%%40sFI12@squashsource.com/ -privatekey=""C:\Program Files\Putty\InMotion\id_rsa.ppk""" ^
    "lcd F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct" ^
    "cd /public_html/wp-content/uploads/wpallimport/files" ^
    "put squashgalaxy.csv" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)

START "" "https://www.squashsource.com/wp-admin/admin.php?page=pmxi-admin-manage&id=27&action=update"

exit /b %WINSCP_RESULT%
