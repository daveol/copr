%global bootstrap 0
%global _program_prefix  %{esp32_target}-

# strip for the target
%global __strip %{_bindir}/%{esp32_target}-strip
%global __objdump %{_bindir}/%{es32_target}-objdump

Name:           esp32-gcc
Version:        5.2.0
Release:        2%{?dist}
Epoch:          1
Summary:        GNU GCC for cross-compilation for %{esp32_target} target

License:        GPLv2+ and GPLv3+ and LGPLv2+ and BSD
URL:            https://github.com/espressif/crosstool-NG

Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.gz

# Overlay from: https://github.com/espressif/crosstool-NG
Source1:        xtensa_esp32.tar

# Patches from: https://github.com/espressif/crosstool-NG
Patch0:    0001-WIP-don-t-bring-extra-u-int_least32_t-into-std.patch
Patch1:    0002-xtensa-report-stack-usage.patch
Patch2:    0003-xtensa-add-HW-FPU-sequences-for-DIV-SQRT-RECIP-RSQRT.patch
Patch3:    0004-xtensa-Fix-PR-target-78118.patch
Patch4:    0005-xtensa-Fix-PR-target-78603.patch
Patch5:    0006-xtensa-add-support-for-SSP.patch
Patch6:    0007-xtensa-add-workaround-for-pSRAM-cache-issue-in-ESP32.patch
Patch7:    0008-libstdc-enable-defines-for-pthreads-support.patch
Patch8:    0009-xtensa-gcov-custom-runtime-file-I-O-API-support.patch
Patch9:    0010-Fix-81037-by-adjutng-headers.patch
Patch10:    0011-libstdc-No-weak-functions-are-required-for-gthread-n.patch
Patch11:    0012-xtensa-Configurable-exception-emergency-pool-size.patch
Patch12:    0013-Fix-psram-workaround-behaviour-for-conditional-branc.patch
Patch13:    0014-gcc-config-xtensa-build-multilib-for-esp32-psram-wor.patch
Patch14:    100-uclibc-conf.patch
Patch15:    110-xtensa-implement-trap-pattern.patch
Patch16:    130-build_gcc-5_with_gcc-6.patch
Patch17:    201-libgcc-remove-unistd-header.patch
Patch18:    301-missing-execinfo_h.patch
Patch19:    810-arm-softfloat-libgcc.patch
Patch20:    830-arm_unbreak_armv4t.patch
Patch21:    840-microblaze-enable-dwarf-eh-support.patch
Patch22:    850-libstdcxx-uclibc-c99.patch
Patch23:    860-cilk-wchar.patch
Patch24:    870-xtensa-add-mauto-litpools-option.patch
Patch25:    871-xtensa-reimplement-register-spilling.patch
Patch26:    872-xtensa-use-unwind-dw2-fde-dip-instead-of-unwind-dw2-.patch
Patch27:    873-xtensa-fix-_Unwind_GetCFA.patch
Patch28:    874-xtensa-don-t-use-unwind-dw2-fde-dip-with-elf-targets.patch
Patch29:    900-libitm-fixes-for-musl-support.patch
Patch30:    901-fixincludes-update-for-musl-support.patch
Patch31:    902-unwind-fix-for-musl.patch
Patch32:    903-libstdc++-libgfortran-gthr-workaround-for-musl.patch
Patch33:    904-musl-libc-config.patch
Patch34:    905-add-musl-support-to-gcc.patch
Patch35:    906-mips-musl-support.patch
Patch36:    907-x86-musl-support.patch
Patch37:    908-arm-musl-support.patch
Patch38:    909-aarch64-musl-support.patch
Patch39:    039-isl-gcc.patch
Patch40:    910-Fix-partial-template-specialization-syntax-in-wide-int.h.diff

# Tools
BuildRequires:  gcc-c++
BuildRequires:  esp32-binutils
BuildRequires:  zlib-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  libmpc-devel
BuildRequires:  isl-devel
BuildRequires:  flex
BuildRequires:  autogen
BuildRequires:  texinfo
BuildRequires:  python2-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gettext
BuildRequires:  esp32-newlib

Requires:       esp32-binutils

Provides:       xtensa-esp32-elf-gcc = %{version}


%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %{esp32_target} platform, instead of for the
native %{_arch} platform.
This package is based on the crosstool-NG xtensa-1.22.x release,
which includes ESP32 target support.

%if ! 0%{bootstrap}

%package c++
Summary:        Cross Compiling GNU GCC targeted at %{target}
Group:          Development/Languages
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       xtensa-esp32-elf-gcc-c++ = %{version}

%description c++
This package contains the Cross Compiling version of g++, which can be used to
compile c++ code for the %{target} platform, instead of for the native
%{_arch} platform.
%endif



%prep
%autosetup -n gcc-%{version} -p 1

# untar overlay
tar --strip-components=1 -xv -f %{SOURCE1} gcc


%build
cat <<EOFL | sed 's/-Werror=format-security//g' > ./.cflags
%{set_build_flags}
EOFL

source ./.cflags

%configure \
	--target=%{esp32_target} \
	--with-sysroot=%{esp32_prefix} \
	--with-newlib \
	--with-gmp \
	--with-mpfr \
	--with-mpc \
	--with-isl \
	--with-cloog \
	--with-libelf \
	--without-long-double-128 \
	--disable-__cxa_atexit \
	--disable-libgomp \
        --disable-libmudflap \
        --disable-libssp \
        --disable-libquadmath \
        --disable-libquadmath-support \
        --disable-nls \
	--disable-shared \
	--enable-lto \
	--enable-target-optspace \
	--enable-threads=posix \
%if 0%{bootstrap}
	--enable-languages=c
%else
	--with-python-dir=share/%{esp32_target}/gcc-%{version}/python \
	--enable-cxx-flags="-fno-rtti -ffunction-sections" \
	--enable-languages=c,c++ \
	--enable-gcov-custom-rtio \
	--disable-libstdcxx-verbose
%endif

%make_build configure-gcc configure-libcpp configure-build-libiberty
%make_build all-libcpp all-build-libiberty

%make_build configure-libdecnumber
%make_build -C host-%{_host}/libdecnumber libdecnumber.a

%make_build configure-libbacktrace
%make_build -C host-%{_host}/libbacktrace

%make_build -C host-%{_host}/gcc libgcc.mvars

%make_build all-gcc

%make_build configure-target-libgcc

#weird fix
sed -i -e 's/^host_subdir[^$]\+/host_subdir = host-%{_host}/g' \
        $(find xtensa-esp32-elf -name Makefile)

%make_build all-target-libgcc

%if ! 0%{bootstrap}
%make_build configure-target-libstdc++-v3

#weird fix
sed -i -e 's/^host_subdir[^$]\+/host_subdir = host-%{_host}/g' \
	$(find xtensa-esp32-elf -name Makefile)

%make_build all-target-libstdc++-v3
%endif

# Just to make sure
%make_build all-target all-host


%install
%make_build DESTDIR=%{buildroot} \
	install-gcc \
	install-target-libgcc \
%if ! 0%{bootstrap}
	install-target-libstdc++-v3
%endif

# Remove unnessecary stuff
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_mandir}/man7



%files
%doc README
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{esp32_target}
%{_libdir}/gcc/%{esp32_target}/%{version}
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{esp32_target}
%{_libexecdir}/gcc/%{esp32_target}/%{version}
%{_bindir}/%{_program_prefix}*
%{_mandir}/man1/%{_program_prefix}*.1.gz
%if ! 0%{bootstrap}
%{esp32_libdir}/*
%exclude %{esp32_includedir}/c++
%exclude %{_bindir}/%{_program_prefix}*c++
%exclude %{_libexecdir}/gcc/%{esp32_target}/%{version}/cc1plus
%exclude %{_mandir}/man1/%{_program_prefix}*++.1.gz
%endif

%if ! 0%{bootstrap}
%files c++
%{_bindir}/%{_program_prefix}*c++
%{_mandir}/man1/%{_program_prefix}*++.1.gz
%{_libexecdir}/gcc/%{esp32_target}/%{version}/cc1plus
%{esp32_includedir}/c++
%{_datadir}/%{esp32_target}/gcc-%{version}/python
%endif


%changelog
* Sat Sep 01 2018 Dave Olsthoorn <dave@bewaar.me> - 0:5.2.0-2
- Add fix for template errors
- disable shared objects

* Tue Aug 28 2018 Dave Olsthoorn <dave@bewaar.me> - 0:5.2.0-1
- Initial spec file
