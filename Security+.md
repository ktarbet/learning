


|                Old                |     New      |
|-----------------------------------|--------------|
| WEP(Wired Equivalent Privacy)     | WPA2 or WAP3 |
| DES (Digital Encryption Standard) | AES          |
| SSL                               | TLS          |
| TLS 1.0/1.2                       | TLS 1.2, 1.3  [microsoft](https://learn.microsoft.com/en-us/microsoft-365/compliance/technical-reference-details-about-encryption?view=o365-worldwide) |






## Tools


|                Name                | Purpose |    ref      |
|-----------------------------------|--------------|--------------|
|hydra| password checker | https://github.com/vanhauser-thc/thc-hydra |
|nmap | network scanner | https://nmap.org/ |




## services

|virustotal.com  | check logs |



## RAID Redudant array of inexpensive Disks

| Level  | What it is|   
|--------------|--------------|
| 0 | disk striping (fast, but failure on any disk failure) |
| 1 | disk mirror data written to both disks|
| 5 | striping with parity (can rebuild with failure)  |
| 6 | 4+disks striping with dual parity -two disks can fail  |
| 10 |4+disks raid 1 + 0 (mirror + striping)  |


