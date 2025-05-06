; Copyright (C) 2025  Darko Milošević <daremc86@gmail.com>

; This program is free software: you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation, either version 3 of the License, or
    ; (at your option) any later version.

; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.

    
!include "mui2.nsh"
Name "DMYoutube2MP3"
OutFile "DMYoutube2MP3_1.0_BETA.exe"
Unicode True
InstallDir "$PROGRAMFILES64\DMYoutube2MP3"
RequestExecutionLevel admin
Icon "res/DMYoutube2MP3.ico"

!define MUI_ABORTWARNING
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "license"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

VIAddVersionKey /LANG=${LANG_ENGLISH} "ProductName" "DMYoutube2MP3 Setup"
VIAddVersionKey /LANG=${LANG_ENGLISH} "Comments" "DMYoutube2MP3 Setup"
VIAddVersionKey /LANG=${LANG_ENGLISH} "CompanyName" "Darko Milošević"
VIAddVersionKey /LANG=${LANG_ENGLISH} "LegalTrademarks" "DMYoutube2MP3 Setup is a trademark of Darko Milošević"
VIAddVersionKey /LANG=${LANG_ENGLISH} "LegalCopyright" "© Darko Milošević"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileDescription" "DMYoutube2MP3 setup program"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileVersion" "1.0.0"
VIProductVersion "1.0.0.0"

Section "Install"
SetOutPath "$INSTDIR"
File "dist\DMYoutube2MP3\DMYoutube2MP3.exe"
File "LICENSE"
File "config.json"
File "README.md"
File "res\DMYoutube2MP3.ico"
SetOutPath "$INSTDIR\_internal"
File /r "dist\DMYoutube2MP3\_internal\*"
File "config.json"
SetOutPath "$INSTDIR\_internal\languages"
File /r "languages\*"
SetOutPath "$APPDATA\DMYoutube2MP3"
IfFileExists "$APPDATA\DMYoutube2MP3\config.json" skip_config
File "config.json"
skip_config:
WriteUninstaller "$INSTDIR\Uninstall.exe"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DMYoutube2MP3" \
"DisplayName" "DMYoutube2MP3"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DMYoutube2MP3" \
"UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
SectionEnd

Section "CreateShortcuts"
CreateDirectory "$SMPROGRAMS\DMYoutube2MP3"
CreateShortcut "$SMPROGRAMS\DMYoutube2MP3\DMYoutube2MP3.lnk" "$INSTDIR\DMYoutube2MP3.exe" "" "$INSTDIR\DMYoutube2MP3.ico" 0
CreateShortcut "$SMPROGRAMS\DMYoutube2MP3\View License.lnk" "$INSTDIR\LICENSE"
CreateShortcut "$SMPROGRAMS\DMYoutube2MP3\View Readme.lnk" "$INSTDIR\README.md"
CreateShortcut "$SMPROGRAMS\DMYoutube2MP3\Uninstall DMYoutube2MP3.lnk" "$INSTDIR\Uninstall.exe"
CreateShortcut "$DESKTOP\DMYoutube2MP3.lnk" "$INSTDIR\DMYoutube2MP3.exe" "" "$INSTDIR\DMYoutube2MP3.ico" 0
SectionEnd

Section "Uninstall"
DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\DMYoutube2MP3"
Delete "$INSTDIR\*.*"
Delete "$INSTDIR\_internal\*.*"
RMDir /r "$INSTDIR\_internal"
Delete "$SMPROGRAMS\DMYoutube2MP3\*.*"
RMDir /r "$SMPROGRAMS\DMYoutube2MP3"
Delete "$DESKTOP\DMYoutube2MP3.lnk"
RMDir /r "$INSTDIR"
SectionEnd
