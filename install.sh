#/bin/sh
#pkgcheck - fast and easy way to be sure that your package does not miss some files http://safrm.net/projects/pkgcheck
#author:  Miroslav Safr <miroslav.safr@gmail.com>
BINDIR=/usr/bin
DOCDIR=/usr/share/doc
MANDIR=/usr/share/man

#root check
USERID=`id -u`
[ $USERID -eq "0" ] || { 
    echo "I cannot continue, you should be root or run it with sudo!"
    exit 0
}
#automatic version 
if command -v appver &>/dev/null; then . appver; else APP_SHORT_VERSION=NA ; APP_FULL_VERSION_TAG=NA ; APP_BUILD_DATE=`date +'%Y%m%d_%H%M'`; fi

mkdir -p -m 0755 $BINDIR
install -m 0777 -v ./pkgcheck  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/pkgcheck && rm -f $BINDIR/pkgcheck.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=$APP_BUILD_DATE/" $BINDIR/pkgcheck && rm -f $BINDIR/pkgcheck.bkp

MANPAGES=`find ./doc/manpages -type f`
sudo install -d -m 755 $MANDIR/man1
sudo install -m 644 $MANPAGES $MANDIR/man1

DOCS="./README ./LICENSE.LGPL"
sudo install -d -m 755 $DOCDIR/pkgcheck
sudo install -m 644 $DOCS $DOCDIR/pkgcheck
