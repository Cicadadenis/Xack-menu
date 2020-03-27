
pkg install unstable-repo

sleep 5

pkg install metasploit

curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz


gunzip metasploit_5.0.65-1_all.deb.gz

dpkg -i metasploit_5.0.65-1_all.deb


apt -f install
