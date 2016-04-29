expand :
	sed -i -e '/raspberrypi/ d' ~/.ssh/known_hosts
	ssh-copy-id -i ~/.ssh/mouse_id_rsa pi@raspberrypi
	ssh pi@raspberrypi echo cool, now make expand
	ansible-playbook -i inventory/jessielite --sudo --user pi expand.yml

app :
	sed -i -e '/vidpi/ d' ~/.ssh/known_hosts
	ssh pi@vidpi echo known host added
	ansible-playbook -i inventory/vid --sudo --user pi app.yml

# is also part of app.... but this way we can do it separately to retry
opf:
	ansible-playbook -i inventory/vid --sudo --user pi opf.yml

# is also part of app.... but this way we can do it separately to retry
ofx:
	ansible-playbook -i inventory/vid --sudo --user pi ofx.yml

