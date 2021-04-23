rm -rf /etc/motd
rm -rf /etc/profile

wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/profile
wget -P /etc https://raw.githubusercontent.com/Cicadadenis/Xack-menu/master/motd

reboot
