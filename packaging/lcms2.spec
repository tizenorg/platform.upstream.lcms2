%define lname libcms2
Name:           lcms2
Summary:        Little CMS Engine - A color managment library and tools
License:        MIT
Group:          Graphics/Libraries
Url:            http://www.littlecms.com/
Version:        2.4
Release:        0
BuildRequires:  libjpeg8-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
Source0:        http://sourceforge.net/projects/lcms/files/lcms/%{version}/%{name}-%{version}.tar.gz

%description
Littlecms is a small speed optimized color management engine.
Little CMS intends to be a small-footprint color management engine
with a special focus on accuracy and performance. It uses the International
Color Consortium standard (ICC), which is the modern standard when
regarding to color management. The ICC specification is widely used and is
referred to in many International and other de-facto standards.

%package -n libcms2
Summary:        Libraries for the Little CMS Engine
Group:          Graphics/Libraries

%description -n libcms2
Little CMS Engine - A color managment library and tools.

%package -n liblcms2-devel
Summary:        Include Files and Libraries Mandatory for Development
Group:          Development/Libraries
Requires:       libcms2 = %{version}
Requires:       glibc-devel

%description -n liblcms2-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q

chmod a-x doc/* COPYING AUTHORS

%build
%configure --disable-static
make %{?_smp_flags}

%install
%make_install

%post -n libcms2 -p /sbin/ldconfig

%postun -n libcms2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING 
%{_bindir}/*

%files -n libcms2
%defattr(-,root,root)
%{_libdir}/liblcms2.so.2*

%files -n liblcms2-devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%docs_package
