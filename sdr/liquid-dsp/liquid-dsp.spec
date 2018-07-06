Name:           liquid-dsp
Version:        1.3.1
Release:        2%{?dist}
Summary:        digital signal processing library for software-defined radios

License:        MIT
URL:            http://liquidsdr.org/
Source0:        https://github.com/jgaeddert/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         liquid-dsp-sonamever.patch

# Tools
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  git
# Libraries
BuildRequires:  fftw-devel

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -S git


%build
./bootstrap.sh
%configure \
  --disable-static \
  --enable-simdoverride

%make_build


%install
mkdir -p %{?buildroot}/%{_includedir}/liquid/
mkdir -p %{?buildroot}/%{_libdir}/
install -m 755 -p libliquid.so.1.2.0 %{?buildroot}/%{_libdir}/
ln -s libliquid.so.1.2.0 %{?buildroot}/%{_libdir}/libliquid.so.0
ln -s libliquid.so.1.2.0 %{?buildroot}/%{_libdir}/libliquid.so
install -m 644 -p include/liquid.h %{?buildroot}/%{_includedir}/liquid/

%check
make check


%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
