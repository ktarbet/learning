
|acronym|Name|
|--|--|
|SOAR|Security Orchestration Automation and Response |
|SIEM|SEM+SIM Security Information and Event Management|
|CVE| Common Vulnerabilities and Exposures mitre.org |
|CVSS| Common Vulnerability Scoring System(CVSS)|
|Syslog|logging protocol |
|OSINT| Open Source Intelligence|
|SUID| Set owner user ID|
|CSIRT| Computer Security Inciden Response Teams|




|SysLog Codes| What |
|--|--|
|0|Emergency|
|1|Alert|
|2|Critical|
|3|Error|
|4|Warning|
|5|Notice|
|6|Information|
|7|Debug|



|                Old                |     New      |
|-----------------------------------|--------------|
| WEP(Wired Equivalent Privacy)     | WPA2 or WAP3 |
| DES (Digital Encryption Standard) | AES          |
| SSL                               | TLS          |
| TLS 1.0/1.2                       | TLS 1.2, 1.3  [microsoft](https://learn.microsoft.com/en-us/microsoft-365/compliance/technical-reference-details-about-encryption?view=o365-worldwide) |
| SHA-1,MD5                           | SHA-2       |







## Tools


|                Name                | Purpose |    ref      |
|-----------------------------------|--------------|--------------|
|hydra| password checker | https://github.com/vanhauser-thc/thc-hydra |
|nmap | network scanner | https://nmap.org/ |
|arp -a| view arp entries ||
|snort| intrusion detection (ITS) |/etc/snort/snort.conf, /etc/snort/rules/local.rules|
|iwconfig| view wireless (linux?) ||
|airodump-ng| see live MAC addresses and other wireless info||
|ipconfig| view network config ||


## Attacks
|         Name                | what?| Prevention |
|------------------------|--------------|--------|
|ARP cache poisoning|directs local network machines to MAC of in/line MIM |keep attacker out of LAN, static ARP cache only |
|MAC address flood|overloaded switch acts like hub||
|Broadcast storm|| Spanning Tree Protocol STP - BPDU, static MAC address in switch|


## IPsec

VPN often  IPsec Tunnel



## services/Sites

|link | description|
|--|--|
|virustotal.com  | check logs |
|https://hackmageddon.com/| stats on cyber events, etc.|


## RAID Redudant array of inexpensive Disks

| Level  | What it is|   
|--------------|--------------|
| 0 | disk striping (fast, but failure on any disk failure) |
| 1 | disk mirror data written to both disks|
| 5 | striping with parity (can rebuild with failure)  |
| 6 | 4+disks striping with dual parity -two disks can fail  |
| 10 |4+disks raid 1 + 0 (mirror + striping)  |



