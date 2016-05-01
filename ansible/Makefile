expand :
	sed -i -e '/raspberrypi/ d' ~/.ssh/known_hosts
	ssh-copy-id -i ~/.ssh/mouse_id_rsa pi@raspberrypi
	ssh pi@raspberrypi echo cool, now make expand
	ansible-playbook -i inventory/jessielite --sudo --user pi expand.yml

# Just install the pre-built code - for production system preparation
app : 
	sed -i -e '/vidpi/ d' ~/.ssh/known_hosts
	ssh pi@vidpi echo known host added
	ansible-playbook -i inventory/vid --sudo --user pi app.yml

# Build OpenFrameworks and install ofxOMXPlayer, ready for development
# Takes an age (about 90 mins).
dev :
	sed -i -e '/vidpi/ d' ~/.ssh/known_hosts
	ssh pi@vidpi echo known host added
	ansible-playbook -i inventory/vid --sudo --user pi dev.yml

# is also part of dev.... but this way we can do it separately to retry
opf:
	ansible-playbook -i inventory/vid --sudo --user pi opf.yml

# is also part of dev.... but this way we can do it separately to retry
ofx:
	ansible-playbook -i inventory/vid --sudo --user pi ofx.yml

