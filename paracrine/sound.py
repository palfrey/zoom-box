from paracrine.helpers.debian import debian_repo,apt_install
from paracrine.helpers.fs import insert_or_replace, set_file_contents
import re

def run():
    debian_repo("bookworm-backports", "deb http://deb.debian.org/debian bookworm-backports main")
    apt_install({"linux-image-amd64": "6.2.0"})
    insert_or_replace("/etc/default/grub", re.compile("GRUB_CMDLINE_LINUX=.+"), "GRUB_CMDLINE_LINUX=\"snd-intel-dspcfg.dsp_driver=1\"")
    set_file_contents("/etc/modprobe.d/snd-blacklist.conf", "blacklist snd_soc_skl")
