from paracrine.helpers.debian import apt_install
from paracrine.helpers.fs import run_command, render_template

def run():
    apt_install(["deborphan"])
    found_packages = run_command("deborphan -anp required --no-show-section", dry_run_safe=True).splitlines()
    ok_packages = render_template("ok-packages.txt").splitlines()

    for found_package in found_packages:
        if found_package not in ok_packages:
            run_command(f"apt remove --yes {found_package}")
    run_command("apt autoremove --yes")
