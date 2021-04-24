rm -rf /etc/motd
rm -rf /etc/profile
cd
git clone https://github.com/Cicadadenis/airgeddon
chmod +x /root/airgeddon/airgeddon.sh
cp -r /root/airgeddon/airgeddon.sh /bin/wifi-crack

git clone https://github.com/Cicadadenis/ipfy
chmod +x /root/ipfy/start-ipfy.sh
cp -r /root/ipfy/start-ipfy.sh /bin/ip-located 
wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/profile
wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/motd


./install.aex -y

reset

cat /etc/motd
