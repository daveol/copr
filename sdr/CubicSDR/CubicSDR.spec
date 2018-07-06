Name:		CubicSDR
Version:	0.2.3
Release:	4%{?dist}
Summary:	Cross-Platform Software-Defined Radio Application

License:	GPLv2
URL:		http://www.cubicsdr.com/
Source0:	https://github.com/cjcliffe/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Tools
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:  desktop-file-utils
# Libs
BuildRequires:	liquid-dsp-devel
BuildRequires:	pkgconfig(rtaudio)
BuildRequires:	hamlib-devel
BuildRequires:	wxWidgets-devel
BuildRequires:	cmake(SoapySDR)

Provides:	bundled(tinyxml) = 2.6.2
Provides:	bundled(lodepng) = 20161127
Provides:	bundled(CubicVR-2) = 20141026 

%description
CubicSDR is the software portion of Software Defined Radio. By Using hardware
that converts RF spectrum into a digital stream we are able to build complex
radios to do many types of functions in software instead of traditional
hardware.

%prep
%autosetup


%build
%cmake . -DUSE_SYSTEM_RTAUDIO:BOOL=ON -DUSE_HAMLIB:BOOL=ON
%make_build
# Wayland crashes CubicSDR
desktop-file-edit --set-key=Exec --set-value='env GDK_BACKEND=x11 CubicSDR %u' ./CubicSDR.desktop


%install
%make_install


%files
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/CubicSDR.desktop
%{_datadir}/cubicsdr
