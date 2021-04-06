echo "[+]Updating"
apt-get update
echo
echo '[++] Installing Dependencies...'
echo '    Python3'
apt-get -y install python3 python3-pip
echo '    Requests'
pip3 install requests
echo '    DateTime'
pip3 install datetime
echo '    Colorama'
pip3 install colorama
echo '    Cfonts'
pip3 install python-cfonts
echo
echo '[+] Setting Permissions...'
chmod 777 log.txt
echo
echo '[+] Installed.'