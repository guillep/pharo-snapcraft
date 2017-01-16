# Pharo Snapcraft package

Snapcraft (http://snapcraft.io/) package of Pharo (http://www.pharo.org).
This package builds a snap package containing a pharo-vm. Using this snapcraft packaging, the pharo-vm is built from scratch and packaged with all its dependencies. This should make sure that your vm runs on the ubuntu/debian system of your preference.

## How to use

### Installing Snapcraft

To build a snap package from this repository, you'll first need to install snapcraft in your system. Something like this will do:

```bash
$ sudo apt install snapcraft
$ sudo apt install build-essential git
``` 

Otherwise, you can follow the instructions in the snapcraft webpage: http://snapcraft.io/create/

### Building the Snap

Get inside the root of this repository and run

```bash
snapcraft
```

This will:
 - install all dependencies
 - download vm sources
 - download pharo runtime sources (.sources file required for the runtime to run)
 - building
 - packaging inside a .snap file

### Installing the Snap

Once the snap file is created, you can install it in your system by doing:

```bash
sudo snap install --dangerous --devmode pharo-vm_6.0_amd64.snap
```

## Using the snapped VM

Once the vm is snapped and installed, you'll have available in your system the following commands:

 - **pharo-vm**: The VM invoked in headless mode. 
 - **pharo-vm.pharo-ui**: the VM invoked in UI mode (opening a window with the IDE and so on...)

###Download an image

Notice the packaged snap does not contain an image. You can download one by doing one of the following:

- Zeroconf scripts

To get stable release Pharo 5
```bash
$ wget -O- get.pharo.org\50 | bash
```

Or latest in-development Pharo 6
```bash
$ wget -O- get.pharo.org\60 | bash
```

- Manual downloads

Of stable release pharo 5
```bash
wget http://files.pharo.org/image/50/Pharo-Image-5.0-latest.zip
unzip Pharo-Image-5.0-latest.zip
```
Or latest in-development Pharo 6
```bash
wget http://files.pharo.org/image/60/Pharo-Image-6.0-latest.zip
unzip Pharo-Image-5.0-latest.zip
```

###Run it!

Now you can run pharo using the snapped commands like this:

```bash
$ pharo-vm Pharo.image eval 1+2
```

```bash
$ pharo-vm.pharo-ui Pharo.image
```
