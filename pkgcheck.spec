%define buildroot %{_topdir}/%{name}-%{version}-root
%define APP_BUILD_DATE %(date +'%%Y%%m%%d_%%H%%M')

Name:       pkgcheck
Summary:    fast and easy way to be sure that your package does not miss some files
Version:    1.0.0
Release:    1
Group:      System/Libraries
License:    LGPL v2.1
BuildArch:  noarch
URL:        https://github.com/safrm/pkgcheck
Vendor:     Miroslav Safr <miroslav.safr@gmail.com>
Source0:    %{name}-%{version}.tar.bz2
Autoreq: on
Autoreqprov: on
BuildRoot: %{buildroot}

%description
fast and easy way to be sure that your package does not miss some files



%prep
%setup -c -n ./%{name}-%{version}
# >> setup
# << setup

%build
# >> build pre
#qmake install_prefix=/usr
# << build pre
#make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -fr $RPM_BUILD_ROOT
# >> install pre
export INSTALL_ROOT=$RPM_BUILD_ROOT
# << install pre 
#make install
mkdir -p %{buildroot}%{_bindir}
install -m 755 ./pkgcheck %{buildroot}/usr/bin/
sed -i".bkp" "1,/^VERSION=/s/^VERSION=.*/VERSION=%{version}/" %{buildroot}%{_bindir}/pkgcheck && rm -f %{buildroot}%{_bindir}/pkgcheck.bkp
sed -i".bkp" "1,/^VERSION_DATE=/s/^VERSION_DATE=.*/VERSION_DATE=%{APP_BUILD_DATE}/" %{buildroot}%{_bindir}/pkgcheck && rm -f %{buildroot}%{_bindir}/pkgcheck.bkp
# >> install post
# << install post




%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/pkgcheck
# << files


