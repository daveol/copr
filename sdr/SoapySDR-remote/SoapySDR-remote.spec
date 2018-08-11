%global gitname SoapyRemote
%global tagname soapy-remote

Name:           SoapySDR-remote
Version:        0.4.3
Release:        1%{?dist}
Summary:        Use any Soapy SDR remotely (client)

License:        Boost
URL:            https://github.com/pothosware/%{gitname}/wiki
Source0:        https://github.com/pothosware/%{gitname}/archive/%{tagname}-%{version}.tar.gz

# Tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
# Libraries
BuildRequires:  cmake(SoapySDR)
BuildRequires:  avahi-devel
BuildRequires:  systemd

Requires:	%{gitname}-sysctl = %{version}-%{release}

%description
A client to use a Soapy SDR device form a %{gitname} server


%package -n %{gitname}-sysctl
Summary:	Sysctl settings for %{gitname}/%{name}
BuildArch:	noarch

%description -n %{gitname}-sysctl
Some sysctl settings provided for %{gitname} and %{name}


%package -n %{gitname}
Summary:	Use any Soapy SDR remotely (server)
Requires:	%{gitname}-sysctl = %{version}-%{release}

%description -n %{gitname}
Use any Soapy SDR remotely using this server


%prep
%autosetup -n %{gitname}-%{tagname}-%{version}


%build
%cmake .
%make_build


%install
%make_install

%post -n %{gitname}-sysctl
%sysctl_apply SoapySDRServer.conf

%files
%license LICENSE_1_0.txt
%doc Changelog.txt
%{_libdir}/SoapySDR/modules0.6/*

%files -n %{gitname}
%license LICENSE_1_0.txt
%{_unitdir}/SoapySDRServer.service
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{gitname}-sysctl
%{_sysctldir}/SoapySDRServer.conf
