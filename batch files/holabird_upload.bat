@echo off

"C:\Program Files (x86)\WinSCP\WinSCP.com" ^
  /command ^
    "open sftp://squash9@squashsource.com:2222/ -hostkey=""ssh-ed25519 256 /4ojnKIwhuAyvONfPWcK9mi8NOoydNFZcWIOl4uBcqk="" -privatekey=""C:\Users\pbastien.CFGLOBAL\.ssh\inmotion.ppk"" -passphrase=""A}H9nSJQCEoK"" -rawsettings Cipher=""aes,chacha20,3des,WARN,des,blowfish,arcfour""" ^
    "lcd C:\Users\pbastien.CFGLOBAL\Dropbox\Bitbucket\Scrapy\crawlers\scrapyproduct" ^
    "cd /home/squash9/public_html/wp-content/uploads/wpallimport/files" ^
    "put holabird.csv" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)

PAUSE

exit /b %WINSCP_RESULT%
