## USE YOUR OWN GDPROXY LINKS AND PUT THEM ALL IN THE GDPROXY.TXT FILE IN THIS FORMAT
```
http://x.com
https://xx.com
http://cool.com
https://thing.com
```
## Hosting
Install Ubuntu via WSL or a Linux PC then use this to get a public GDProxy link
```
ssh -R 80:localhost:8000 nokey@localhost.run
```
