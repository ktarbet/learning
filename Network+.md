
### OSI 7 Layer model

|Layer | Name | description |
|---|---|---|
|1 |Physical|wires, radio waves |
|2 |Data link| Frames (MAC addresses) |
|3 |Networking | Logical (IP addresses) |
|4 |Transport | Ports join/assemble data|
|5 |Session | connection to service (ports needed)|
|6 |Presentation|encoding/encryption of data|
|7 |Application | wget|



MAC address 48 bits Hex

### IP Version 4
32 bits = 4,294,967,296  ~4.2 billion addresses  2^32
example: 192.168.1.51  
network: 192.168.1
host: .51
most common mask /24

### IP Version 6
128 bits
2^128
example: 2607:f8b0:4023:1002::64
most common mask /64


### protocols

|Protocol | Name | description |
|---|---|---|
|ARP|Address resolution | IP<-->MAC  LAN only traffic|
|UDP|User Datagram Protocol| quick and efficient, not-connection based, not as reliable as TCP|
|TCP|Transmission Control Protocol| handles errors, connection/session based |
|PPP| Point to Point Protocol|older|
|EAP|Extensible Authentication Protocol|newer more common |


|Port | Service|
|---|---|
|TCP 21| ftp|
|TCP 23| telnet|
|TCP 25| SMTP Simple Mail Transfer Protocol|
|UDP 53|DNS|
|TCP 80| http|
|TCP 110| POP3 Post office Protocol v3 (messages on server) |
|TCP 443| https|
|TCP 445| Windows Network/interprocess communication|
|TCP 3389| Windows Remote Desktop|
|TCP 3389| Windows Remote Desktop|


Private IP Addresses

|Class|Range |
|--|--|
|Class A| 10.0.0.0 - 10.255.255.255|
|Class B| 172.16.0.0 to 172.31.255.255|
|Class C| 192.168.0.0 to 192.168.255.255|



### Tools
|Name| what is it?| example|
|--|--|
|ping|check if host up|ping 192.168.0.122|
|Nmap| what hosts are servers are running on your network| nmap --top ports 20 localhost|


ping 8.8.8.8  # dns.google
ping 8.8.8.8 -t  


ipconfig /?
ipconfig/displaydns

Books/vendors
Lammle
Meyers "All in One"
Sybex
youtube: prof. Messer, NetworkChuck (https://www.youtube.com/watch?v=5WfiTHiU4x8) , CBT Nuggets, Technuggets

ss64.com # command line reference
https://12ft.io/  # view search engine cached results
https://automatetheboringstuff.com/
https://www.eff.org/
https://packetpushers.net/network-documentation-series-logical-diagram/

