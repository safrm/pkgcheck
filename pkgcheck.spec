%define APP_BUILD_DATE %(date +'%%Y%%m%%d_%%H%%M')

Name:       pkgcheck
Summary:    fast and easy way to be sure that your package does not miss some files
Version:    1.0.0
Release:    1
Group:      System/Libraries
License:    LGPL v2.1
BuildArch:  noarch
URL:        http://safrm.net/projects/pkgcheck
Vendor:     Miroslav Safr <miroslav.safr@gmail.com>
Source0:    %{name}-%{version}.tar.bz2
Autoreq: on
Autoreqprov: on
BuildRequires:  appver >= 1.1.1
BuildRequires: jenkins-support-scripts >= 1.2.3

%description
fast and easy way to be sure that your package does not miss some files


%prep
%setup -c -n ./%{name}-%{version}

%build
jss-docs-update ./doc -sv %{version} 

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 755 ./pkgcheck %{buildroot}%{_bindir}
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}%{_bindir}/pkgcheck && rm -f %{buildroot}%{_bindir}/pkgcheck.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}%{_bindir}/pkgcheck && rm -f %{buildroot}%{_bindir}/pkgcheck.bkp

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 ./doc/manpages/pkgcheck.1* %{buildroot}%{_mandir}/man1/


%check
for TEST in $(  grep -r -l -h "#\!/bin/sh" . )
do
		sh -n "$TEST"
		if  [ $? != 0 ]; then
			echo "syntax error in $TEST, exiting.." 
			exit 1
		fi
done

%files
%defattr(-,root,root,-)
%{_bindir}/pkgcheck
%{_mandir}/man1/pkgcheck.1*




