%global gitname SoapyAirspy
%global tagname soapy-airspy

Name:           SoapySDR-airspy
Version:        0.1.1
Release:        1%{?dist}
Summary:        Soapy SDR plugin for the Airspy

License:        MIT
URL:            https://github.com/pothosware/%{gitname}/wiki
Source0:        https://github.com/pothosware/%{gitname}/archive/%{tagname}-%{version}.tar.gz

# Tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
# Libraries
BuildRequires:  cmake(SoapySDR)
BuildRequires:  pkgconfig(libairspy)

%description
Soapy SDR plugin for Airspy


%prep
%autosetup -n %{gitname}-%{tagname}-%{version}


%build
%cmake .
%make_build


%install
%make_install


%files
%license LICENSE.txt
%doc Changelog.txt
%{_libdir}/SoapySDR/modules0.6/*
