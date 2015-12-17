Name:		super-smack
Version:	1.3.2
Release:	2%{?dist}
Summary:	MySQL Super Smack is a benchmarking, stress testing, and load generation tool for MySQL.

Group:		Development/Tools
License:	GPLv2
URL:		https://github.com/winebarrel/super-smack
# https://github.com/winebarrel/super-smack/archive/1.3.3.tar.gz
Source0:	super-smack-1.3.3.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc-c++ bison flex

%description
MySQL Super Smack is a benchmarking, stress testing, and load generation tool for MySQL.

%prep
%setup -q

%build
%configure --with-mysql --with-mysql-lib=/usr/lib64
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/var
mv /var/smack-data %{buildroot}/var
chmod 777 %{buildroot}/var/smack-data
mkdir -p %{buildroot}/usr/share
mv /usr/share/smacks %{buildroot}/usr/share

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/var/smack-data
%dir /usr/share/smacks
/usr/share/smacks/
/usr/bin/
