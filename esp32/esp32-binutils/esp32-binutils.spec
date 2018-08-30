%global _program_prefix  %{esp32_target}-

Name:           esp32-binutils
Version:        2.25.1
Release:        2%{?dist}
Summary:        GNU Binutils for cross-compilation for %{esp32_target} target

License:        GPLv2+ and GPLv3+ and LGPLv2+ and BSD
URL:            https://github.com/espressif/crosstool-NG

Source0:        https://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.gz
# Overlay from: https://github.com/espressif/crosstool-NG
Source1:        xtensa_esp32.tar

# (Relevant) patches from: https://github.com/espressif/crosstool-NG
Patch2:         300-012_check_ldrunpath_length.patch
Patch5:         330-Dont-link-to-libfl-as-its-unnecessary.patch
Patch6:         905-Fix-trampolines-search-code-for-conditional-branches.patch
Patch7:         906-xtensa-optimize-check_section_ebb_pcrels_fit.patch
Patch8:         907-xtensa-optimize-removed_by_actions.patch
Patch9:         908-xtensa-optimize-find_removed_literal.patch
Patch10:        909-xtensa-replace-action-list-with-splay-tree.patch
Patch11:        910-xtensa-optimize-trampolines-relaxation.patch
Patch12:        911-xtensa-fix-localized-symbol-refcounting-with-gc-sect.patch
Patch13:        912-xtensa-fix-gas-segfault-with-text-section-literals.patch
Patch14:        913-xtensa-add-auto-litpools-option.patch
Patch15:        914-xtensa-fix-signedness-of-gas-relocations.patch
Patch16:        915-xtensa-fix-.init-.fini-literals-moving.patch

# Tools
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  texinfo
BuildRequires:  m4
BuildRequires:  perl
BuildRequires:  zlib-devel
BuildRequires:  git
BuildRequires:  esp32-filesystem

Requires:       esp32-filesystem

%description
TODO: write description


%prep
%autosetup -n binutils-%{version} -p 1

# untar overlay
tar --strip-components=1 -xv -f %{SOURCE1} binutils


%build
%configure \
	--target=%{esp32_target} \
	--enable-multilib \
	--enable-ld \
	--disable-gold \
	--disable-werror \
	--disable-nls \
	--with-sysroot=%{esp32_prefix} \
	--with-pkgversion="Fedora %{version}-%{release}" \
	--with-bugurl="https://bugzilla.redhat.com/"

%make_build


%install
%make_install

# This is a crosstool, so we nuke the infodir
rm -rf %{buildroot}%{_infodir}


%files
%doc README
%{esp32_libdir}/ldscripts
%{esp32_bindir}/*
%{_bindir}/%{_program_prefix}*
%{_mandir}/man1/%{_program_prefix}*


%changelog
* Thu Aug 30 2018 Dave Olsthoorn <dave@bewaar.me> - 2.25.1-2
- Rebuilt for esp32-filesystem bump

* Tue Aug 28 2018 Dave Olsthoorn <dave@bewaar.me> - 2.25.1-1
- Initial spec file
