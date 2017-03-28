all: get
	cd opensmalltalk-vm/build.linux32x86/pharo.cog.spur/build/ && ./mvm

get:
	git clone --depth 1 https://github.com/OpenSmalltalk/opensmalltalk-vm.git

install:
