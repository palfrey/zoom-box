from pathlib import Path
from paracrine.helpers.debian import apt_install
from paracrine.helpers.fs import link, make_directory, set_file_contents_from_template, set_owner, set_mode
from paracrine.helpers.systemd import systemd_set

def run():
    apt_install(["lightdm", "xfce4", "aptitude", "firefox-esr", "pavucontrol", "htop", "pulseaudio"])
    lightdm_conf_dir = Path("/etc/lightdm/lightdm.conf.d")
    config_change = make_directory(lightdm_conf_dir)
    config_change = set_file_contents_from_template(lightdm_conf_dir.joinpath("01-custom.conf"), "lightdm-custom.conf.j2")
    systemd_set("lightdm", enabled=True, running=True, restart=config_change)
    link("/etc/systemd/system/default.target", "/lib/systemd/system/graphical.target")

    desktop_folder = Path("~palfrey/Desktop").expanduser()
    make_directory(desktop_folder)

    def create_desktop_file(name: str, template_name: str) -> None:
        desktop_file = desktop_folder.joinpath(name)
        set_file_contents_from_template(desktop_file, template_name)
        set_mode(desktop_file, "0755")
        set_owner(desktop_file, "palfrey")

    create_desktop_file("Suspend.desktop", "suspend.desktop")
    create_desktop_file("Zoom.desktop", "zoom.desktop")
