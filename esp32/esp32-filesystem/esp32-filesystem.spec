%global target	xtensa-esp32-elf

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           esp32-filesystem
Version:        1
Release:        2%{?dist}
Summary:        filesystem and macros for %{target} cross-compilation tools

License:        MIT
URL:            http://fedoraproject.org/wiki/ESP32
BuildArch:      noarch

Source0:        macros.esp32

%description
This package contains the base filesystem layout, RPM macros and
environment for %{target} cross-compilation tools


%prep
%setup -q -c -T


%build
# nop


%install
mkdir -p "%{buildroot}%{_prefix}/%{target}/bin"
mkdir -p "%{buildroot}%{_prefix}/%{target}/lib"
mkdir -p "%{buildroot}%{_prefix}/%{target}/include"
mkdir -p "%{buildroot}%{_prefix}/%{target}/share"

mkdir -p "%{buildroot}%{macrosdir}"
install -m 644 %{SOURCE0} %{buildroot}%{macrosdir}

%files
%dir %{_prefix}/%{target}
%dir %{_prefix}/%{target}/bin
%dir %{_prefix}/%{target}/lib
%dir %{_prefix}/%{target}/include
%dir %{_prefix}/%{target}/share
%{macrosdir}/macros.esp32



%changelog
* Thu Aug 30 2018 Dave Olsthoorn <dave@bewaar.me> - 1-2
- Remove esp32_sysroot, we'll now use esp32_prefix as sysroot

* Wed Aug 29 2018 Dave Olsthoorn <dave@bewaar.me> - 1-1
- Initial specfile

