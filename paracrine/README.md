https://pimylifeup.com/raspberry-pi-enable-ssh-without-monitor/

Ended up using imager from https://www.raspberrypi.com/software/ as I didn't have a micro HDMI at that point

lite 32-bit?

ssh-copy-id pi@raspberrypi

https://bbs.archlinux.org/viewtopic.php?id=285225

echo "options snd-hda-intel dmic_detect=0" | sudo tee -a /etc/modprobe.d/alsa-base.conf
echo "blacklist snd_soc_skl" | sudo tee -a /etc/modprobe.d/blacklist.conf
