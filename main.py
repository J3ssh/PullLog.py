import shutil
#shutil.copy2('src', 'dst')
#Basic Logs
shutil.copy2('C:\windows\System32\winevt\Logs\Application.evtx', 'C:\loot\Application.evtx')
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Operational.evtx', 'C:\loot\Microsoft-Windows-PowerShell%4Operational.evtx')
shutil.copy2('C:\windows\System32\winevt\Logs\System.evtx', 'C:\loot\System.evtx')
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4Operational.evtx', 'C:\loot\Microsoft-Windows-Windows Defender%4Operational.evtx')
shutil.copy2('C:\windows\System32\winevt\Logs\Security.evtx', 'C:\loot\Security.evtx')
#shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx', 'C:\loot\Microsoft-Windows-Sysmon%4Operational.evtx')

#remote logs
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx' , 'C:\loot\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx')
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-WinRM%4Operational.evtx' , 'C:\loot\Microsoft-Windows-WinRM%4Operational.evt')
#Runkey
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-Shell-Core%4Operational.evtx', 'C:\loot\Microsoft-Windows-Shell-Core%4Operational.evtx')
#Group Policy
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-GroupPolicy%4Operational.evtx', 'C:\loot\Microsoft-Windows-GroupPolicy%4Operational.evtx')
#Bits
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-Bits-Client%4Operational.evtx', 'C:\loot\Microsoft-Windows-Bits-Client%4Operational.evtx')
#extra_security
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-Security-Netlogon%4Operational.evtx', 'C:\loot\Microsoft-Windows-Security-Netlogon%4Operational.evtx')
shutil.copy2('C:\windows\System32\winevt\Logs\Microsoft-Windows-Security-Mitigations%4UserMode.evtx', 'C:\loot\Microsoft-Windows-Security-Mitigations%4UserMode.evtx')
