%global gitname SoapyRTLSDR
%global tagname soapy-rtlsdr


Name:           SoapySDR-rtlsdr
Version:        0.2.5
Release:        1%{?dist}
Summary:        Vendor and platform neutral SDR support library

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

Supplements:	SoapySDR

%description
A fresh and clean vendor neutral and platform independent SDR support library


%prep
%autosetup -n %{gitname}-%{tagname}-%{version}


%build
%cmake .
%make_build


%install
%make_install


%files
%doc Changelog.txt
%{_libdir}/SoapySDR/modules0.6/librtlsdrSupport.so
