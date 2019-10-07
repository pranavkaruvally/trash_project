sudo mv master_program.service /lib/systemd/system/master_program.service

sudo systemctl daemon-reload
sudo systemctl enable dummy.service
