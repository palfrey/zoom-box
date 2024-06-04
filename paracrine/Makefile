requirements.txt: requirements.in
	pip-compile

2023-05-03-raspios-bullseye-arm64-lite.img:
	wget https://downloads.raspberrypi.org/raspios_lite_arm64/images/raspios_lite_arm64-2023-05-03/2023-05-03-raspios-bullseye-arm64-lite.img.xz
	xz -d -v 2023-05-03-raspios-bullseye-arm64-lite.img.xz

write-drive: 2023-05-03-raspios-bullseye-arm64-lite.img
	sudo dd if=2023-05-03-raspios-bullseye-arm64-lite.img of=/dev/mmcblk0 bs=1M status=progress
