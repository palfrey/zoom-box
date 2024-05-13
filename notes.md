https://nixos.asia/en/tutorial/nixos-install

nix shell nixpkgs#git -c nixos-rebuild build --flake .

NIXPKGS_ALLOW_UNFREE=1 NIXOS_CONFIG=`pwd`/configuration.nix nix shell nixpkgs#git -c nixos-rebuild switch

sudo nix-collect-garbage --delete-older-than 2d
