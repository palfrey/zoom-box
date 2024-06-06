# Zoom box for a Dell Wyse 5070

A lot of this will work elsewhere, but this is what it's targeted at.

1. Install Debian (I'd advise setting up [Ventoy](https://www.ventoy.net) on a stick and then copying over [a netinst image](https://www.debian.org/distrib/))
2. Copy `config.yaml.example` to `config.yaml`, and edit the `box` block
    * USER: whatever your login was to Debian
    * ZOOM_URL: The single-click login to your Zoom room
3. Edit `box/inventory.yaml` and fix the IP, `ssh_user` and `ssh_key` if you need to (easiest way to do this is `ssh-copy-id <username>@<ip of zoom box>`)
4. Goto the root of this source code, and run `make zoom-install`
