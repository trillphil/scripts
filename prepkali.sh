#!/bin/bash

# install additional packages
sudo apt-get update
sudo apt-get install ftp

# download tools from github
sudo git clone https://github.com/magnumripper/JohnTheRipper.git /opt/john/
sudo git clone https://github.com/Ne0nd0g/scripts.git /opt/russ_scripts/
sudo git clone https://github.com/trillphil/scripts.git /opt/phil_scripts/
sudo git clone https://github.com/NotSoSecure/password_cracking_rules.git /opt/password_cracking_rules/

# install john
cd /opt/john/src/
./configure && make

# add terminal padding
mkdir -p ~/.config/gtk-3.0/
tee ~/.config/gtk-3.0/gtk.css << SWAG
VteTerminal,
TerminalScreen,
vte-terminal {
    padding: 10px 10px 10px 10px;
    -VteTerminal-inner-border: 10px 10px 10px 10px;
}
SWAG

# add impacket folder to path
export PATH="$PATH:/usr/share/doc/python-impacket/examples/"
echo "export PATH=\"\$PATH:/usr/share/doc/python-impacket/examples/\"" >> ~/.bashrc
