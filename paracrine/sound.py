from paracrine.helpers.debian import debian_repo,apt_install
from paracrine.helpers.fs import set_file_contents, run_command
import re

def run():
    debian_repo("bookworm-backports", "deb http://deb.debian.org/debian bookworm-backports main")
    apt_install({"linux-image-amd64": "6.2.0"})

    existing = open("/etc/default/grub").read()
    results = re.compile("GRUB_CMDLINE_LINUX=\"(.*)\"").search(existing)
    if results is not None:
        if "snd-intel-dspcfg.dsp_driver" not in results.group(1):
            changes = set_file_contents(
                "/etc/default/grub", existing[: results.start(1)] + results.group(1) + " snd-intel-dspcfg.dsp_driver=1" + existing[results.end(1) :]
            )
            if changes:
                run_command("update-grub")

    set_file_contents("/etc/modprobe.d/snd-blacklist.conf", "blacklist snd_soc_skl")
