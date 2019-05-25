Name:       freetype
Summary:    A free and portable font rendering engine
Version:    2.8.0
Release:    1
Group:      System/Libraries
License:    FTL or GPLv2+
URL:        http://www.freetype.org
Source0:    http://download.savannah.gnu.org/releases-noredirect/freetype/freetype-%{version}.tar.bz2
Patch0:     freetype-2.7.0-enable-valid.patch
BuildRequires: libtool
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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   zlib-devel

%description devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.



%prep
%setup -q -n %{name}-%{version}/%{name}

# freetype-2.2.1-enable-valid.patch
%patch0 -p1

%build
sh autogen.sh
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%makeinstall gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/libfreetype.so.*
%exclude %{_libdir}/libfreetype.la

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_libdir}/libfreetype.so
%{_libdir}/pkgconfig/*.pc

