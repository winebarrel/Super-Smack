Name:		super-smack
Version:	1.3.2
Release:	1%{?dist}
Summary:	MySQL Super Smack is a benchmarking, stress testing, and load generation tool for MySQL.

Group:		Development/Tools
License:	GPLv2
URL:		https://github.com/winebarrel/super-smack
Source0:	super-smack-1.3.2.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc-c++ bison flex

%description
MySQL Super Smack is a benchmarking, stress testing, and load generation tool for MySQL.

%prep
%setup -q

%build
%configure --with-datadir=%{buildroot}/var/smack-data --with-smacks-dir=%{buildroot}/usr/share/smacks --with-mysql --with-mysql-lib=/usr/lib64
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir /usr/share/smacks
/usr/share/smacks/
/usr/bin/
