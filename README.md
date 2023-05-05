# CFuzzy
![image](https://user-images.githubusercontent.com/16538325/234744580-cfa8b30b-6b72-46e0-b696-99d7791a1627.png)
## So, wtf is this ?
its a gui made for [This Masterpiece](https://github.com/GFW-knocker/gfw_resist_tls_proxy) code which make some socket stuff to your cloudflare requestes and get it pass through Goofy Firewall (GFW) and similar ones.

## How to use it?
```console
wget "https://github.com/Ali-Frh/CFuzzy/archive/refs/heads/main.zip" && unzip main.zip && cd CFuzzy-main && python3 main.py
```   

or even make a shortcut for main.py and double-click on it.  
ps. If you Use **Linux**, make sure you have **tk** Package. (available in Arch/Debian/Ubuntu/Fedora etc. Repos)


## Why this app looks ancient ?
because i made it with Tkinter which is a ancient graphical toolkit, it doesnt look good but it is included in python3 standard package, it has simple syntax, small size, ...

## Why you made this ?
to change their value and using it easier for users and testers.

## My pyprox_tcp.py Differences to the Original one
~~added some random.randint() feature to send_data_in_fragment() function, which suggested by [This Dude](https://twitter.com/joje_twit/status/1651341798046826496)~~  
i will not tweaking the tcpproxy script anymore because the original project is very active and i just modify the script for make it compatible with the GUI.  
ps. I clearified my additions by #CFuzzy comment in the code.

## TODO:
- make this thing save last settings when closed.
- adding an internal xray core for supporting yt feature and more.
- maybe making a server choosing menu from (yebekhe/cf-clean-ip-resolver)
- maybe adding Farsi
- maybe adding some server killer feature in case that you closed app accidentally

## License
i was wanted to choose MIT but the original project used GPL-3, so...
