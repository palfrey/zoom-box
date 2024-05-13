# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

let
  core-user = "palfrey";
  zoom-link = pkgs.writeTextFile {
    name = "zoom-link";
    destination = "/home/" + core-user + "/Desktop/zoom-link.html";
    text = ''
      <a href="https://us04web.zoom.us/j/5648707839?pwd=eGqsghELAHAIAs0BArrDo4Lk1N0OqN.1">Tom personal zoom room</a>
    '';
  };
in
{
  imports =
    [
      # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  # Bootloader.
  boot.loader = {
    systemd-boot.enable = true;
    efi.canTouchEfiVariables = true;
  };

  networking = {
    hostName = "zoom-box";
    # wireless.enable = true;  # Enables wireless support via wpa_supplicant.

    # Configure network proxy if necessary
    # proxy.default = "http://user:password@proxy:port/";
    # proxy.noProxy = "127.0.0.1,localhost,internal.domain";

    networkmanager.enable = true;
  };

  services.fwupd.enable = true;
  powerManagement.powertop.enable = true;

  # Set your time zone.
  time.timeZone = "Europe/London";

  # Select internationalisation properties.
  i18n.defaultLocale = "en_GB.UTF-8";

  i18n.extraLocaleSettings = {
    LC_ADDRESS = "en_GB.UTF-8";
    LC_IDENTIFICATION = "en_GB.UTF-8";
    LC_MEASUREMENT = "en_GB.UTF-8";
    LC_MONETARY = "en_GB.UTF-8";
    LC_NAME = "en_GB.UTF-8";
    LC_NUMERIC = "en_GB.UTF-8";
    LC_PAPER = "en_GB.UTF-8";
    LC_TELEPHONE = "en_GB.UTF-8";
    LC_TIME = "en_GB.UTF-8";
  };

  # Enable the X11 windowing system.
  services.xserver = {
    enable = true;

    # Enable the XFCE Desktop Environment.
    displayManager.lightdm.enable = true;
    desktopManager.xfce.enable = true;

    # Configure keymap in X11
    layout = "gb";
    xkbVariant = "";

    # Enable automatic login for the user.
    displayManager.autoLogin = {
      enable = true;
      user = core-user;
    };
  };

  environment.xfce.excludePackages = [ pkgs.xfce.xfce4-volumed-pulse ];

  # Configure console keymap
  console.keyMap = "uk";

  hardware.pulseaudio = {
    enable = true;
    package = pkgs.pulseaudioFull;
  };
  security.rtkit.enable = true;

  # Enable touchpad support (enabled default in most desktopManager).
  # services.xserver.libinput.enable = true;

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.palfrey = {
    isNormalUser = true;
    description = core-user;
    extraGroups = [ "networkmanager" "wheel" ];
  };

  # Allow unfree Zoom packages
  nixpkgs.config.allowUnfree = true;

  # List packages installed in system profile. To search, run:
  # $ nix search wget
  environment = {
    systemPackages = with pkgs; [
      vim
      #updated_zoom.zoom-us
      zoom-us
      htop
      pavucontrol
      #pciutils
      #lshw
      firefox
      zoom-link
    ];
    # etc = {
    #   "modprobe.d/alsa-base.conf".text = "options snd-hda-intel dmic_detect=0";
    #   "modprobe.d/blacklist.conf".text = "blacklist snd_soc_skl";
    # }
  };

  # List services that you want to enable:

  # Enable the OpenSSH daemon.
  services.openssh.enable = true;

  # This value determines the NixOS release from which the default
  # settings for stateful data, like file locations and database versions
  # on your system were taken. It‘s perfectly fine and recommended to leave
  # this value at the release version of the first install of this system.
  # Before changing this value read the documentation for this option
  # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
  system.stateVersion = "23.05"; # Did you read the comment?

  nix.settings.experimental-features = "nix-command flakes";
}
