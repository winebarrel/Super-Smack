Name:		super-smack
Version:	1.3.3
Release:	1%{?dist}
Summary:	MySQL Super Smack is a benchmarking, stress testing, and load generation tool for MySQL.

Group:		Development/Tools
License:	GPLv2
URL:		https://github.com/winebarrel/super-smack
Source0:	super-smack.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc-c++ bison flex

%description
MySQL Super Smack is a benchmarking, stress testing, and load generation tool for MySQL.

%prep
%setup -q -n src

%build
%configure --with-mysql --with-mysql-lib=$(mysql_config --variable=pkglibdir)
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} DATADIR=%{buildroot}/var/smack-data SMACKS_DIR=%{buildroot}/usr/share/smacks

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/var/smack-data
%dir /usr/share/smacks
/usr/share/smacks/
/usr/bin/gen-data
/usr/bin/super-smack
