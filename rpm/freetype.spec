Name:       freetype
Summary:    A free and portable font rendering engine
Version:    2.10.4
Release:    1
License:    FTL or GPLv2+
URL:        https://www.freetype.org/
Source0:    %{name}-%{version}.tar.bz2
Patch0:     0001-Enable-TrueType-GX-AAT-and-OpenType-table-validation.patch
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: pkgconfig(zlib)
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(libpng)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   %{name}-bytecode

%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%package devel
Summary:    FreeType development libraries and header files
Requires:   %{name} = %{version}-%{release}

%description devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static \
  --with-zlib=yes \
  --with-bzip2=yes \
  --with-png=yes \
  --enable-freetype-config \
  --with-harfbuzz=no \
  --with-brotli=no
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license docs/LICENSE.TXT docs/FTL.TXT docs/GPLv2.TXT
%{_libdir}/libfreetype.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/freetype2.pc
%{_mandir}/man1/*
