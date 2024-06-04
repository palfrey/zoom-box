from paracrine.helpers.debian import add_trusted_key, debian_repo, apt_install

def run():
    keypath = add_trusted_key("https://mirror.mwt.me/zoom/gpgkey", "mwt-zoom", "749ffc985c6a8e42d5ecc1add78309305018479538647b4c346843d1db12deaa")
    debian_repo("mwt-zoom", f"deb [arch=amd64 signed-by={keypath}] https://mirror.mwt.me/zoom/deb any main")
    apt_install(["zoom"], always_install=True)
