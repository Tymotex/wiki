---
title: Arch Linux
---

Arch Linux is a fully independent Linux distribution with a rolling-release model. It’s loved for being incredibly minimal, configurable and rewarding because of how much you learn in setting it up exactly as you like it.

The [official Arch installation guide](https://wiki.archlinux.org/title/Installation_guide) is the main guide to consult. Everything else is not guaranteed to work. These notes just collect some pointers on pitfalls I ran into and how I resolved them as well as directions for further customisation.

## Installation
Dual booting Windows 11 and Arch Linux. Assumes you’re running Windows 11 in UEFI BIOS mode with GPT formatted drive. I sourced these instructions from the [official installation guide](https://wiki.archlinux.org/title/Installation_guide) and [Ksk Royal](https://www.youtube.com/watch?v=JRdYSGh-g3s&ab_channel=KskRoyal).
1. Using Windows’ [Disk Management](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/overview-of-disk-management), create a partition with unallocated space for the Linux installation. I did this by shrinking the Windows partition and giving myself around 500GB.
2. Get the [ISO file](https://archlinux.org/download/) and create the *installation media*. On Windows, you can create a bootable USB drive with the Arch Linux ISO using [Rufus](https://rufus.ie/en/).
3. **Network**
    `ip -c a` — list all network interfaces.
    In my case, I’m using a wireless network interface that ships with my motherboard (ROG STrix x570-E). The process for connecting to the network involved using [iwctl](https://wiki.archlinux.org/title/Iwd#iwctl) (internet wireless control utility).
    Sanity check that you’re connected to the internet with: `ping [archlinux.org](http://archlinux.org)`.
    ⚠️ I needed to turn off ‘fast boot’ or ‘fast startup’ through the Windows control panel to get the wireless network interface to show up in the output of `ip link` or `ip -c a`.
4. **Verify you’re booted in UEFI mode: `ls /sys/firmware/efi/efivars/` → this should produce a big list of text.**
5. **System clock**
    ```bash
    timedatectl list-timezones
    timedatectl set-timezone Australia/Sydney # → use Sydney’s timezone.
    timedatctl status                         # → use this to verify that the local time is correct.
    ```
6. **Keyboard layout**
    `ls /usr/share/kbd/keymaps/i386/qwerty` → show all keyboard layouts
    `loadkeys <path_to_layout>`
7. **Creating partitions**
    `lsblk` → lists all drives connected to your PC and their partitions.
    - **Drive names:** `/dev/sda1` is the first partition of the first drive (the ‘sd’ means SATA device, the ‘a’ is just an identifier for the drive, the number is the partition number). Similarly, `/dev/sdb2` would be the second partition of the second drive.
    - Use `fdisk -l` for more information for each drive.
    - Note: we will be install the GRUB boot loader in `/dev/sda1`.
    `cfdisk /dev/<drive_name>` → starts an interactive menu that lets you manage partitions. This is basically a neat wrapper around `fdisk`.
    Note: for Arch Linux, we should create 3 partitions: 
    - *root* —  Strictly speaking, this root partition is the only one that’s required. Aim for somewhere around 25-45GB.
    - *home* — for the user’s personal files such as pictures, documents, projects, etc. This should take up as much space as you have or are willing to allocate.
    - *swap* — for virtual RAM. When infrequently accessed data gets evicted from RAM, it gets cached in this swap partition.
        - Won’t [SSDs die](https://techreport.com/review/27909/the-ssd-endurance-experiment-theyre-all-dead/) with too many writes? Don’t worry about it — on systems with a decent amount of RAM, the swap partition is very rarely used at all. [Read more](https://askubuntu.com/questions/652337/why-are-swap-partitions-discouraged-on-ssd-drives-are-they-harmful).
8. **Formatting partitions** 
    To ‘format’ a drive or partition means to set up a filesystem for it. 
    - For the root partition: `mkfs.ext4 /dev/<root_partition>`
    - For the home partition: `mkfs.ext4 /dev/<home_partition>`
    - For the swap partition: `mkswap /dev/<swap_partition>`, then run `swapon /dev/<swap_partition>` to tell the OS that it’s free to use this partition as a swap partition.
9. **Mounting partitions**
    Now that we have the EXT4 filesystem set up for the root and home partitions, we need to tell the OS that they’re accessible by using `mount` and supplying a *mount point*, which is a path at which we can access the partition.
10. **Selecting mirror servers**
    Packages are downloaded from the mirror servers listed in `/etc/pacman.d/mirrorlist`.
    ```bash
    cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak                  # create a backup file for the original mirrors.
    pacman -Sy                                                                # updates the package database to latest versions.
    pacman -S pacman-contrib                                                  # gives you the rankmirrors bash script which tests download speeds and figures out the faster mirror servers for you.
    rankmirrors -n 10 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirrorlist # writes the 10 best mirror servers into /etc/pacman.d/mirrorlist.
    ```
11. **Install Arch Linux to the root partition, plus other essential packages**
    `pacstrap -i /mnt base base-devel linux linux-lts linux-headers linux-firmware amd-ucode sudo nano vim git neofetch networkmanager dhcpcd pulseaudio bluez wpa_supplicant`
    - Substitute `amd-ucode` for `intel-ucode` for Intel processors.
12. **Generate filesystem table**
    `genfstab -U /mnt >> /mnt/etc/fstab`
13. **Chroot to newly installed system**
    `arch-chroot /mnt`
14. **Set root user password and make a new user**
    ```bash
    passwd                                     # → prompts you to set the root user password.
    useradd -m <username>                      # → makes a new user without a password.
    passwd <username>                          # → prompts you to set the new user’s password
    usermod -aG wheel,storage,power <username> # → adds the new user to a set of groups.
    ```
    Now, run `visudo` to edit the sudoers file with Vim and uncomment the line: `%wheel ALL=(ALL:ALL) ALL`.
15. **Set system language**
    In `/etc/locale.gen`, locate and uncomment `en_US.UTF-8 UTF-8`.
    Then run:
    ```bash
    locale-gen
    echo LANG=en_US.UTF-8 > /etc/locale.conf
    export LANG=en_US.UTF-8
    ```
16. **Set hostname**
    `echo arch > /etc/hostname` → where ‘arch’ is the name I’ve chosen for my PC.
17. **Set hosts**
    Populate the `/etc/hosts` file which contains hostname → IP address mappings.
    ```
    # Static table lookup for hostnames.
    # See hosts(5) for details.
    
    127.0.0.1   localhost
    ::1		      localhost
    127.0.1.1	  **arch**.localdomain	   localhost   # Substitute arch for your chosen hostname.
    ```
18. **Set the timezone**
    Search for your timezone along the path: `/usr/share/zoneinfo`.
    Set your timezone by creating a symbolic link to `/etc/localtime` by running: `ln -sf /usr/share/zoneinfo/Australia/Sydney /etc/localtime`.
    Update the hardware clock with: `hwclock --systohc`.
19. **Install the GRUB boot loader in /boot/efi**
    ```bash
    mkdir /boot/efi
    mount /dev/sda1 /boot/efi     # Use `lsblk` to confirm that the boot partition has been mounted at /boot/efi.
    pacman -S grub efibootmgr dosfstools mtools
    ```
    Now, in the file `/etc/default/grub`, uncomment `GRUB_DISABLE_OS_PROBER=false` so that Windows is discoverable by GRUB.
    ```bash
    pacman -S os-prober
    grub-install --target=x86_64-efi --bootloader-id=grub_uefi --recheck
    grub-mkconfig -o /boot/grub/grub.cfg   # This should report a line like 'Found Windows Boot Manger on ...'.
    ```
20. **Enable network services**
    ```bash
    systemctl enable dhcpcd.service
    systemctl enable NetworkManager.service
    ```
    ⚠️ I wasn’t able to have wifi working post-installation. I solved it with the help of this [thread](https://bbs.archlinux.org/viewtopic.php?id=256456).
21. **Wrapping up**
    ```bash
    exit             # Get out of the chroot environment.
    umount -lR /mnt  # Unmount all partitions.
    ```
    Shut down, eject the installation media, then boot into Arch Linux from the GRUB menu (at this point, you should be able to boot between Linux/Windows).
22. **Display server and desktop environment**
    First, sync the pacman databases with `sudo pacman -Sy`. Now, we’ll install some necessary packages to get a KDE plasma desktop environment (which can be readily dropped for a different desktop environment or window manager anytime later).
    ```bash
    sudo pacman -S xorg xorg-xinit xterm plasma plasma-desktop kde-applications kdeplasma-addons sddm xorg-server xorg-init
    echo 'exec startkde' > ~/.xinitrc
    sudo systemctl enable sddm.service
    ```
    Upon rebooting, you should boot directly into login greeting screen and be able to access the desktop environment.
23. **Proceeding to post-installation**
    Now you’ll need to get everything else working… like bluetooth, graphics card drivers, etc.

## Post-Installation
### **Bluetooth**
- **Connection:**
I paired and connected bluetooth through `bluetoothctl` as suggested by the [official guide](https://wiki.archlinux.org/title/bluetooth). I encountered the error `bluetoothctl: No default controller available` and had to use the legacy package, `bluez-util-compat`. I also could not successfully connect to my headset initially, but this was solved by simply installing `pulseaudio-bluetooth` ([source](https://bbs.archlinux.org/viewtopic.php?id=270465)).
- **Crackling:**
I experienced serious crackling due to the interference of WiFi and bluetooth when connected to a 2.4GHz network.
    - I initially fixed this by using 5GHz as suggested by the [official guide](https://wiki.archlinux.org/title/Bluetooth_headset#Connecting_works,_but_there_are_sound_glitches_all_the_time). I didn’t use this solution long-term since the 5GHz connection was [less reliable](https://beambox.com/what-s-the-difference-between-2-4ghz-and-5ghz-wifi) for me due to physical obstructions and distance from the router.
    - I don’t know exactly what worked, but I tried replacing `pulseaudio` with `pipewire` by running `sudo pacman -S pipewire-pulse pipewire-alsa` ([source](https://www.reddit.com/r/archlinux/comments/lv5ihv/what_is_the_most_proper_way_to_replace_pulseaudio/)).
- **Automatic bluetooth controller power-on:**
I just followed the [official guide](https://wiki.archlinux.org/title/bluetooth#Auto_power-on_after_boot/resume).

### **NVIDIA Proprietary Drivers**

My graphics card is GeForce GTX 1060 6GB. By default, the nouveau drivers are used. I had terrible web browser performance (even with hardware acceleration turned on) which indicated that I might need to adopt the proprietary NVIDIA drivers. I couldn’t use Figma or view websites using three.js for 3D rendering. 

I struggled for hours with this. When I followed the main installation instructions in the [official NVIDIA guide](https://wiki.archlinux.org/title/NVIDIA), `startx` would no longer work and I’d be met with a blank screen and a blinking cursor on boot. My mistake was not carefully reading the subsequent information below the main installation guide. In the end, I’m not sure how I got it working but these were the main things I did:

- Install `nvidia` and `nvidia-utils`. This automatically blacklists nouveau from being used.
- Ran `nvidia-xconfig`.
- Added the kernel parameter: `nvidia-drm.modeset=1`. I did this by modifying the grub config file at `/etc/default/grub` and setting:
    - `GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet **nvidia-drm.modeset=1**"`

I confirmed that the proprietary drivers were in use instead of nouveau by checking the output of `lspci -v`.

```
05:00.0 VGA compatible controller: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] (rev a1) (prog-if 00 [VGA controller])
	Subsystem: eVga.com. Corp. Device 6161
	Flags: bus master, fast devsel, latency 0, IRQ 77, IOMMU group 14
	Memory at fb000000 (32-bit, non-prefetchable) [size=16M]
	Memory at d0000000 (64-bit, prefetchable) [size=256M]
	Memory at e0000000 (64-bit, prefetchable) [size=32M]
	I/O ports at e000 [size=128]
	Expansion ROM at 000c0000 [virtual] [disabled] [size=128K]
	Capabilities: <access denied>
	**Kernel driver in use: nvidia**
	Kernel modules: nouveau, nvidia_drm, nvidia
```

As further visual confirmation, I ran `sudo pacman -S virtualgl` and executed a 3D rendering test with `glxspheres64`.

I had noticeable screen tearing on all 3 of my monitors. I fixed it by running the following (sourced from the [official guide’s suggestion](https://wiki.archlinux.org/title/NVIDIA/Troubleshooting#Avoid_screen_tearing)):

```bash
nvidia-settings --assign CurrentMetaMode="DVI-D-0: nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }, DP-0: nvidia-auto-select +2560+0 { ForceFullCompositionPipeline = On }, DP-4: nvidia-auto-select +6000+0 { ForceFullCompositionPipeline = On }"
```

### **Multi-Monitor**
I was not bothered to learn how to use the `xrandr` CLI, so I just installed and used a simple GUI, `arandr` to create the correct monitor layout. I saved the layout into `~/.screenlayout/main.sh`, used `chmod 755 ~/.screenlayout/main.sh`, and added `exec_always ~/.screenlayout/main.sh` to the i3 config file so that it would always be run.

I had the following setup at the time:

- Left monitor (2560x1440) at DVI-D-0.
- Central ultrawide monitor (3440x1440) at DP-0.
- Right monitor (2560x1440) at DP-4.

### **Terminal Emulator**
Terminal emulators are programs that let you use a shell from Xorg. They make your shell prettier and more user-friendly by giving you theme customisability (transparency, colour schemes, etc.), tabs, power user shortcuts, etc. Some examples of popular terminal emulators include:

- GNOME terminal (default for GNOME).
- Konsole (default for KDE).
- Alacritty. This was the one I went with.

### **Display Manager**
The display manager is the login GUI that might additionally handle things like letting you choose which desktop environment or window manager to load.

There are many options like `lightdm`, `gdm` (for GNOME), `sddm` (for KDE). I went with `lightdm` simply because I had seen it in a tutorial.

### **File Manager**
I didn’t overthink this and chose the familiar default file manager that ships with Ubuntu, `nautilus`. There are popular alternatives like `dolphin`.

### Network
[NetworkManager](https://wiki.archlinux.org/title/NetworkManager) ships with a daemon, the `nmcli` CLI and `nmtui` GUI. Use either to explicitly connect to different access points or see what access points are available to your device.

```bash
systemctl enable NetworkManager.service    # Enable the daemon which will automatically connect you to an available network.

nmtui                      # Launch the curses-based GUI.

# **═════ nmcli ═════**
nmcli connection           # Shows a list of available access points and which one you're connected to.

nmcli device wifi connect <access_point> password <password>     # Connect to a different access point.

# Rescan for connections.
nmcli device wifi rescan 
nmcli device wifi list     # List all connections. Source: https://superuser.com/questions/164059/how-to-force-network-manager-to-rescan-connections.
```

### Desktop Environment
A *desktop environment* (DE) is basically a user-friendly GUI that ships with an app menu, wallpapers, widgets, etc. which enables you to use your mouse. It’s really just a frontend, it doesn’t add any additional core functionality. Without a desktop environment, you’re stuck with using the terminal, however using [[window managers]] without a full-blown DE can help optimise your workflow.

- Desktop environments are usually not coupled to the Linux distribution you’re using. You can use most desktop environments regardless of whether you’re running Ubuntu or Kali.
- Linux servers typically won’t have a desktop environment. It’s just a waste of computing resources, especially if its purpose is to run some web server 24/7 that needs every bit of RAM it can get.

**Popular Desktop Environments:**
- [GNOME](https://www.gnome.org/) — minimal and pretty. Ubuntu uses this by default.
- [Xfce](https://xfce.org/) — has a lower RAM footprint (however you still cannot beat window managers in performance which requires only ~50MB instead of hundreds).
- [KDE](https://kde.org/plasma-desktop/) — highly customisable. Seems to be recommended most often by Arch Linux users.
- [Budgie](https://ubuntubudgie.org/) — modern and pretty.

### Window Managers
Window managers let you snap and automatically resize windows instantly and intuitively. They also minimise/eliminate the need to use your mouse to resize windows and get them where you want and set keybindings to speed up your workflow.

**Popular Window Managers:**

- i3 ← I chose this one because it seemed to most popular and beginner-friendly.
- AwesomeWM
- DWM
- Qtile
- Xmonad

### VSCode
Everything worked for me out of the box, except sign-in and settings sync. 

- Sign-in: I followed VSCode’s [troubleshooting guide](https://code.visualstudio.com/docs/editor/settings-sync#_linux) to resolve keychain errors.
- Settings sync: I was able to sync everything (settings, keybindings, etc.) except for extensions. I could not find a solution for this, however I worked around it fairly easily by doing the following:
    - Bring up the VSCode command palette and run: `Settings Sync: Show Synced Data`. Find the latest `extensions.json` remote file, then save it to a local file. Pass that JSON through a pipeline of `sed` commands to get only the id field, then run the VSCode CLI command: `code --install-extension <extension_name>`.

### Printer
I installed `cups`, `cups-pdf`, `avahi`, `nss-mdns`. Then, I made the [necessary edits](https://wiki.archlinux.org/title/Avahi#Hostname_resolution) to `/etc/nsswitch.conf` and started and enabled `avahi-daemon.service`, `cups.service`. I checked that my printer was discoverable over the network by using `avahi-discover` and I was able to print PDFs afterwards.

### Picom
Picom is a *compositor* for Xorg. It lets you have things like transparent, blurry, rounded windows.

Config file at `~/.config/picom/picom.conf`.

## System Maintenance
You need to regularly run commands to maintain a stable system over time. The basics are:
```sh
systemctl --failed     # Look for failed systemd services
pacman -Syu            # Upgrading does carry risks.
```

### pacman
The Arch Linux **pac**kage **man**ager.

```bash
pacman -sS <package_name>    # Queries for downloadable packages. Doesn't install anything.
```

### **yay**
TODO.

### AUR
Arch User Repository is a community repository for a bunch of useful packages that can be installed with `pacman`.

TODO.

## Troubleshooting
In my experience, everything was able to be solved through forums on [bbs.archlinux.org](http://bbs.archlinux.org) and the official Arch Linux wiki, given patience and tweaking the Google search query.

**Arch-Chroot Rescue:**
A powerful way to debug and save an Arch Linux installation when it won’t boot is by mounting the root partition from an installation media and then chrooting into the main installation’s root filesystem.

```bash
fdisk -l    # Confirm that you know where the boot loader and Arch installation's root partition is.
lsblk       # Alternative to `fdisk -l`.

mount /dev/sda6 /mnt         # Mount the root partition (for me, this is sda6).
mount /dev/sda1 /mnt/boot    # Mount the boot loader partition.
arch-chroot /mnt             # chroot into the root partition.

# From here, try to inspect logs, invalid configuration files, etc.
# Once done:
exit                         # Exit the chroot environment.
umount /mnt/boot
umount /mnt
reboot
```

I misconfigured lightdm and used this method to save my Arch installation.

--- 

Stuff to try:
- Try out i3wm window manager
- Ranger for file manger
- Rofi for opening applications
- [https://www.reddit.com/r/archlinux/comments/hppf0t/productivity_apps_on_linux/](https://www.reddit.com/r/archlinux/comments/hppf0t/productivity_apps_on_linux/)
- Keybindings
    - Eg alt+ctrl+shift+1 does `code ~/Projects/timz.dev`
        - Bonus if I can get VSCode to automatically start the project by running yarn dev in a terminal for example.
- Emoji typer [https://www.youtube.com/watch?v=GKviflL9XeI&ab_channel=LukeSmith](https://www.youtube.com/watch?v=GKviflL9XeI&ab_channel=LukeSmith).
- Quick Python calculator by shortcut.
- `cbonsai`
- Google drive file manager integration.
- Set up a proper forced shutdown time with adequate warning

Personal Checklist
- ~~Test that you can get into Windows no problem.~~
- ~~Install dmenu or rofi~~
    - Rofi Rice:
        - Install papirus-icon-theme.
        - Select theme with `rofi-theme-selector`
        - Installed `rofimoji`.
            - You can pick one of the 10 most recently used emojis with `alt+<num>`
        - Installed a custom launcher and powermenu at https://github.com/adi1090x/rofi
- ~~Set up Logid.~~
- ~~Can I get a volume indicator somewhere? (volnoti? or how to get floating system notifications)~~
    - Using `dunst` for system notifications and `i3-volume`.
- ~~GUI to configure audio input and output.~~ → Using `pavucontrol`
- ~~How to get a system font? I can’t see emojis on LinkedIn.~~
    - Install ttf-dejavu, adobe-source-han-sans-cn-fonts, adobe-source-han-sans-kr-fonts,adobe-source-han-sans-jp-fonts
    - List fonts with `fc-list`
- [https://github.com/polybar/polybar/wiki](https://github.com/polybar/polybar/wiki)
- ~~Learn basics of i3~~
- ~~Start setting up i3 keybindings~~
- ~~Using a file manager, bring over all your old data.~~
- LightDM beautification.
- ~~Customise the taskbar.~~
    - Polybar config at ~/.config/polybar/config.ini
    - Using module/spotify: https://github.com/PrayagS/polybar-spotify. I just put the script in ~/Scripts. Clickable.
    - Using these pulseaudio modules to see input and output volumes. They’re controllable through the mouse wheel. https://github.com/marioortizmanero/polybar-pulseaudio-control
    - Using picom opacity rule to make the bar transparent.
    - Using `iwgetid` from `wireless_tools`, I spawn the `nmtui` network manager GUI on left click and rescan for networks on right click.
- Set up redshift properly. Maybe get it to work on a specific keybinding.
- Set the refresh rate correctly for the dell monitor.
- Install cool retro term [https://snapcraft.io/cool-retro-term](https://snapcraft.io/cool-retro-term).
- ~~Need to install proprietary Nvidia drivers instead of nouveau. Trying this causes startx to fail, leaving me with no window manager, desktop manager or desktop environment. ☹️. This video looks promising though: [https://www.youtube.com/watch?v=AOjOd3wIPu8&ab_channel=Octalbits](https://www.youtube.com/watch?v=AOjOd3wIPu8&ab_channel=Octalbits).~~
- Need to fix screen tearing on all monitors. [https://www.youtube.com/watch?v=MfL_JkcEFbE&ab_channel=NeonCipher](https://www.youtube.com/watch?v=MfL_JkcEFbE&ab_channel=NeonCipher).

---
    