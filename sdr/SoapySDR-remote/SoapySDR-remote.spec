%global gitname SoapyRemote
%global tagname soapy-remote

Name:           SoapySDR-remote
Version:        0.4.3
Release:        1%{?dist}
Summary:        Use any Soapy SDR remotely

License:        MIT
URL:            https://github.com/pothosware/%{gitname}/wiki
Source0:        https://github.com/pothosware/%{gitname}/archive/%{tagname}-%{version}.tar.gz

# Tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
# Libraries
BuildRequires:  cmake(SoapySDR)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  systemd

%description
A server that enables clients to use its Soapy SDR devices


%prep
%autosetup -n %{gitname}-%{tagname}-%{version}


%build
%cmake .
%make_build


%install
%make_install

%post
%sysctl_apply SoapySDRServer.conf

%files
%doc Changelog.txt
%{_bindir}/*
%{_mandir}/man1/*
%{_sysctldir}/SoapySDRServer.conf
%{_unitdir}/SoapySDRServer.service
%{_libdir}/SoapySDR/modules0.6/*
