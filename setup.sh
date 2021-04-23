rm -rf /etc/motd
rm -rf /etc/profile

wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/profile
wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/motd

chmod +x *

./install.aex -y

reset

cat /etc/motd
