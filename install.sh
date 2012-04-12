#/bin/sh
#pkgcheck - fast and easy way to be sure that your package does not miss some files https://github.com/safrm/pkgcheck
#author:  Miroslav Safr <miroslav.safr@gmail.com>
BINDIR=/usr/bin

sudo mkdir -p -m 0755 $BINDIR
sudo install -m 0777 -v ./pkgcheck  $BINDIR/

