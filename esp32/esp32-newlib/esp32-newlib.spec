# FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for esp32.
# The related discussion can be found here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global _binaries_in_noarch_packages_terminate_build 0

# specify tools for the target
%global __strip %{_bindir}/%{esp32_target}-strip
%global __objdump %{_bindir}/%{es32_target}-objdump

# when bootstrapping only install header files
%global bootstrap 0

Name:           esp32-newlib
Version:        2.2.0
Release:        3%{?dist}
Epoch:          1
Summary:        C library intended for use on %{esp32_target} embedded systems
BuildArch:      noarch

License:        BSD and MIT and LGPLv2+ and ISC
URL:            https://github.com/espressif/crosstool-NG

Source0:        https://sourceware.org/pub/newlib/newlib-%{version}.tar.gz

# Overlay from: https://github.com/espressif/crosstool-NG
Source1:        xtensa_esp32.tar

# Patches from: https://github.com/espressif/crosstool-NG
Patch0:         0001-xtensa-add-port.patch
Patch1:         0002-xtensa-cleanups.patch
Patch2:         0003-xtensa-enable-sqrt.patch
Patch3:         0004-xtensa-Add-weak-symbols-for-locking-functions.patch
Patch4:         0005-Add-xtensa-machine-_default_types.h-overriding-gener.patch
Patch5:         0006-Fixed-up-_default_types.h-so-uint_least8-16-32_t-are.patch
Patch6:         0007-xtensa-Add_intsup.h-to-disable-__has_long32-allows-P.patch
Patch7:         0008-Add-xtensa-esp8266-specific-config.h.patch
Patch8:         0009-Shrink-default-xtensa-fd-buffer-size-to-128-bytes.patch
Patch9:         0010-nano-malloc-Uncomment-locking-primitives-commented-b.patch
Patch10:        0011-libgcc-doesn-t-have-__ieee754_remainderf-so-don-t-us.patch
Patch11:        0012-Enable-__DYNAMIC_REENT__-remove-default-__getreent-i.patch
Patch12:        0013-Fix-configuration-overlay.patch
Patch13:        0014-Make-some-data-const.patch
Patch14:        0015-Move-xtensa-specific-stuff-to-global-config.patch
Patch15:        0016-Make-sure-_impure_ptr-and-_impure_data-are-not-defin.patch
Patch16:        0017-Prevent-locale-loading-code-from-being-pulled-in.patch
Patch17:        0018-Don-t-initialize-environ-by-default.patch
Patch18:        0019-Update-xtensa-config-in-core-isa.h.patch
Patch19:        0020-math-enable-__ieee754_remainder-f-__ieee754_fmod-f-f.patch
Patch20:        0021-stdatomic.h-add-stdint.h-include.patch
Patch21:        0022-xtensa-enable-pthreads-support.patch

BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  gcc
BuildRequires:  esp32-filesystem
%if ! 0%{bootstrap}
BuildRequires:  esp32-gcc
%endif

%description


%prep
%autosetup -n newlib-%{version} -p 1

# untar overlay
tar --strip-components=1 -xv -f %{SOURCE1} newlib


%build
%if ! 0%{bootstrap}
%configure \
	--target=%{esp32_target} \
        --disable-newlib-io-c99-formats \
        --disable-newlib-io-long-long \
        --disable-newlib-io-float \
        --disable-newlib-io-long-double \
        --disable-newlib-supplied-syscalls \
        --enable-target-optspace

%make_build
%endif


%install
%if 0%{bootstrap}
mkdir -p "%{buildroot}%{esp32_includedir}"
cp -a newlib/libc/include/. %{buildroot}%{esp32_includedir}
cp -r newlib/libc/sys/xtensa/include/. %{buildroot}%{esp32_includedir}

%else
%make_install

# This is a crosstool, so we nuke the infodir
rm -rf %{buildroot}%{_infodir}
%endif



%files
%doc README
%{esp32_includedir}/*
%if ! 0%{bootstrap}
%{esp32_libdir}/*
%endif


%changelog
* Sat Sep 01 2018 Dave Olsthoorn <dave@bewaar.me> - 1:2.2.0-3
- add proper (non-)bootstrap support
- make noarch

* Fri Aug 31 2018 Dave Olsthoorn <dave@bewaar.me> - 0:2.2.0-2
- fix typo

* Thu Aug 30 2018 Dave Olsthoorn <dave@bewaar.me> - 0:2.2.0-1
- Initial specfile

