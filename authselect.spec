#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : authselect
Version  : 1.0.2
Release  : 5
URL      : https://github.com/pbrezina/authselect/archive/1.0.2.tar.gz
Source0  : https://github.com/pbrezina/authselect/archive/1.0.2.tar.gz
Summary  : Select system authentication and identity sources.
Group    : Development/Tools
License  : GPL-3.0
Requires: authselect-bin = %{version}-%{release}
Requires: authselect-data = %{version}-%{release}
Requires: authselect-lib = %{version}-%{release}
Requires: authselect-license = %{version}-%{release}
Requires: authselect-locales = %{version}-%{release}
Requires: authselect-python = %{version}-%{release}
Requires: authselect-python3 = %{version}-%{release}
BuildRequires : cmocka-dev
BuildRequires : popt-dev
BuildRequires : sed

%description
Enable winbind for system authentication
========================================

%package bin
Summary: bin components for the authselect package.
Group: Binaries
Requires: authselect-data = %{version}-%{release}
Requires: authselect-license = %{version}-%{release}

%description bin
bin components for the authselect package.


%package data
Summary: data components for the authselect package.
Group: Data

%description data
data components for the authselect package.


%package dev
Summary: dev components for the authselect package.
Group: Development
Requires: authselect-lib = %{version}-%{release}
Requires: authselect-bin = %{version}-%{release}
Requires: authselect-data = %{version}-%{release}
Provides: authselect-devel = %{version}-%{release}

%description dev
dev components for the authselect package.


%package doc
Summary: doc components for the authselect package.
Group: Documentation

%description doc
doc components for the authselect package.


%package lib
Summary: lib components for the authselect package.
Group: Libraries
Requires: authselect-data = %{version}-%{release}
Requires: authselect-license = %{version}-%{release}

%description lib
lib components for the authselect package.


%package license
Summary: license components for the authselect package.
Group: Default

%description license
license components for the authselect package.


%package locales
Summary: locales components for the authselect package.
Group: Default

%description locales
locales components for the authselect package.


%package python
Summary: python components for the authselect package.
Group: Default
Requires: authselect-python3 = %{version}-%{release}

%description python
python components for the authselect package.


%package python3
Summary: python3 components for the authselect package.
Group: Default
Requires: python3-core

%description python3
python3 components for the authselect package.


%prep
%setup -q -n authselect-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550089407
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1550089407
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/authselect
cp COPYING %{buildroot}/usr/share/package-licenses/authselect/COPYING
%make_install
%find_lang authselect

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/authconfig
/usr/bin/authselect

%files data
%defattr(-,root,root,-)
/usr/share/authselect/default/nis/README
/usr/share/authselect/default/nis/REQUIREMENTS
/usr/share/authselect/default/nis/dconf-db
/usr/share/authselect/default/nis/dconf-locks
/usr/share/authselect/default/nis/fingerprint-auth
/usr/share/authselect/default/nis/nsswitch.conf
/usr/share/authselect/default/nis/password-auth
/usr/share/authselect/default/nis/postlogin
/usr/share/authselect/default/nis/system-auth
/usr/share/authselect/default/sssd/README
/usr/share/authselect/default/sssd/REQUIREMENTS
/usr/share/authselect/default/sssd/dconf-db
/usr/share/authselect/default/sssd/dconf-locks
/usr/share/authselect/default/sssd/fingerprint-auth
/usr/share/authselect/default/sssd/nsswitch.conf
/usr/share/authselect/default/sssd/password-auth
/usr/share/authselect/default/sssd/postlogin
/usr/share/authselect/default/sssd/smartcard-auth
/usr/share/authselect/default/sssd/system-auth
/usr/share/authselect/default/winbind/README
/usr/share/authselect/default/winbind/REQUIREMENTS
/usr/share/authselect/default/winbind/dconf-db
/usr/share/authselect/default/winbind/dconf-locks
/usr/share/authselect/default/winbind/fingerprint-auth
/usr/share/authselect/default/winbind/nsswitch.conf
/usr/share/authselect/default/winbind/password-auth
/usr/share/authselect/default/winbind/postlogin
/usr/share/authselect/default/winbind/system-auth

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libauthselect.so
/usr/lib64/pkgconfig/authselect.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/authselect/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libauthselect.so.1
/usr/lib64/libauthselect.so.1.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/authselect/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f authselect.lang
%defattr(-,root,root,-)

