bootstrap :
	ansible-playbook -i inventory/jessielite --sudo --user pi bootstrap.yml --ask-pass

clean: 
	sed -i -e '/raspberry/ d' -e '/vidpi/ d' ~/.ssh/known_hosts
	ssh-copy-id -i ~/.ssh/mouse_id_rsa pi@raspberrypi

