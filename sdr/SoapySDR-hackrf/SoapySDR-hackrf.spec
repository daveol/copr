%global gitname SoapyHackRF
%global tagname soapy-hackrf

Name:           SoapySDR-hackrf
Version:        0.3.3
Release:        1%{?dist}
Summary:        SoapySDR HackRF module

License:        MIT
URL:            https://github.com/pothosware/%{gitname}/wiki
Source0:        https://github.com/pothosware/%{gitname}/archive/%{tagname}-%{version}.tar.gz

# Tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
# Libraries
BuildRequires:  cmake(SoapySDR)
BuildRequires:  pkgconfig(libhackrf)

%description
Soapy SDR module for Hack RF


%prep
%autosetup -n %{gitname}-%{tagname}-%{version}


%build
%cmake .
%make_build


%install
%make_install


%files
%license LICENSE
%doc Changelog.txt
%{_libdir}/SoapySDR/modules0.6/*
