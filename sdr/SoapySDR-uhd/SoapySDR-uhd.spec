%global gitname SoapyUHD
%global tagname soapy-uhd

Name:           SoapySDR-uhd
Version:        0.3.4
Release:        1%{?dist}
Summary:        Soapy SDR plugins for UHD supported SDR devices

License:        GPLv3
URL:            https://github.com/pothosware/%{gitname}/wiki
Source0:        https://github.com/pothosware/%{gitname}/archive/%{tagname}-%{version}.tar.gz

# Tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
# Libraries
BuildRequires:  cmake(SoapySDR)
BuildRequires:  cmake(UHD)
BuildRequires:  boost-devel

%description
A server that enables clients to use its Soapy SDR devices


%prep
%autosetup -n %{gitname}-%{tagname}-%{version}


%build
%cmake .
%make_build


%install
%make_install


%files
%license COPYING
%doc Changelog.txt
%{_libdir}/SoapySDR/modules0.6/*
%{_libdir}/uhd/modules/*
