expand :
	ansible-playbook -i inventory/jessielite --sudo --user pi expand.yml

app :
	ansible-playbook -i inventory/vid --sudo --user pi app.yml

clean: 
	sed -i -e '/raspberry/ d' -e '/vidpi/ d' ~/.ssh/known_hosts
	ssh-copy-id -i ~/.ssh/mouse_id_rsa pi@raspberrypi
	ssh pi@raspberrypi echo cool, now make expand

