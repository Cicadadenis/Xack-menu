rm -rf /etc/motd
rm -rf /etc/profile
cd
git clone https://github.com/Cicadadenis/airgeddon
cp -r /root/airgeddon/airgeddon.sh /bin/wifi-crack
git clone https://github.com/Cicadadenis/ipfy
cp -r /root/ipfy
wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/profile
wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/motd

chmod +x *

./install.aex -y

reset

cat /etc/motd
