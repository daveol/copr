Name:           SoapySDR
Version:        0.6.1
Release:        1%{?dist}
Summary:        Vendor and platform neutral SDR support library

License:        Boost
URL:            https://github.com/pothosware/%{name}/wiki
Source0:        https://github.com/pothosware/%{name}/archive/soapy-sdr-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  swig
BuildRequires:  python2-devel
BuildRequires:  python3-devel

%description

%package -n lib%{name}
Summary:        The %{name} libraries

%description -n lib%{name}
This package contains the libraries for %{name}

%package -n lib%{name}-devel
Summary:        The development files for %{name}

%description -n lib%{name}-devel
This package contains development files for the libraries of %{name}

%package -n python2-%{name}
Summary:        Python2 bindings for %{name}
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
These are the python2 bindings for %{name}

%package -n python3-%{name}
Summary:        Python2 bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
These are the python2 bindings for %{name}



%prep
%autosetup -n %{name}-soapy-sdr-%{version}


%build
%cmake .
%make_build


%install
%make_install


%files
%license LICENSE_1_0.txt
%doc Changelog.txt
%{_bindir}/*
%{_mandir}/man1/*

%files -n python2-%{name}
%{python2_sitearch}/*%{name}*

%files -n python3-%{name}
%{python3_sitearch}/*%{name}*
%{python3_sitearch}/__pycache__/*

%files -n lib%{name}
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc
%{_datarootdir}/cmake/*


%changelog
* Mon Jun 25 2018 Dave Olsthoorn <dave@bewaar.me> - 0.6.1-1
- Initial spec file
