#/bin/sh
#pkgcheck - fast and easy way to be sure that your package does not miss some files http://safrm.net/projects/pkgcheck
#author:  Miroslav Safr <miroslav.safr@gmail.com>
. appver-installer

appver_basic_scripts_test

$MKDIR_755 $BINDIR
$INSTALL_755 ./pkgcheck  $BINDIR
appver_update_version_and_date $BINDIR/pkgcheck

$MKDIR_755 $COMPLETION_DIR
$INSTALL_755 ./pkgcheck_completion  $COMPLETION_DIR

