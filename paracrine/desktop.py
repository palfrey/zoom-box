from pathlib import Path
from typing import cast
from paracrine.helpers.debian import apt_install
from paracrine.helpers.fs import link, make_directory, set_file_contents_from_template, set_owner, set_mode
from paracrine.helpers.systemd import systemd_set
from paracrine.helpers.config import core_config, build_config

def run():
    LOCAL = build_config(core_config())
    username = cast(str, LOCAL["USER"])
    apt_install(["lightdm-autologin-greeter", "lightdm", "xorg", "accountsservice", "xfce4", "aptitude", "firefox-esr", "pavucontrol", "htop", "pulseaudio"])
    lightdm_conf_dir = Path("/etc/lightdm/lightdm.conf.d")
    config_change = make_directory(lightdm_conf_dir)
    config_change = set_file_contents_from_template(lightdm_conf_dir.joinpath("01-custom.conf"), "lightdm-custom.conf.j2", USERNAME=username)
    systemd_set("lightdm", enabled=True, running=True, restart=config_change)
    link("/etc/systemd/system/default.target", "/lib/systemd/system/graphical.target")

    desktop_folder = Path(f"~{username}/Desktop").expanduser()
    make_directory(desktop_folder)

    def create_desktop_file(name: str, template_name: str) -> None:
        desktop_file = desktop_folder.joinpath(name)
        set_file_contents_from_template(desktop_file, template_name, ignore_changes=False, **LOCAL)
        set_mode(desktop_file, "0755")
        set_owner(desktop_file, username)

    create_desktop_file("Suspend.desktop", "suspend.desktop")
    create_desktop_file("Zoom.desktop", "zoom.desktop")
