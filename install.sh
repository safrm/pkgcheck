#/bin/sh
#pkgcheck - fast and easy way to be sure that your package does not miss some files https://github.com/safrm/pkgcheck
#author:  Miroslav Safr <miroslav.safr@gmail.com>
BINDIR=/usr/bin

#root check
USERID=`id -u`
[ $USERID -eq "0" ] || { 
    echo "I cannot continue, you should be root or run it with sudo!"
    exit 0
}
#automatic version 
. appver

mkdir -p -m 0755 $BINDIR
install -m 0777 -v ./pkgcheck  $BINDIR/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=$APP_FULL_VERSION_TAG/" $BINDIR/pkgcheck && rm -f $BINDIR/pkgcheck.bkp
