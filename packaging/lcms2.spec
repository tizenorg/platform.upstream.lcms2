%define lname libcms2
Name:           lcms2
Summary:        Little CMS Engine - A color managment library and tools
License:        MIT
Group:          Productivity/Graphics/Other
Url:            http://www.littlecms.com/
Version:        2.3
Release:        0
BuildRequires:  libjpeg8-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://sourceforge.net/projects/lcms/files/lcms/%{version}/%{name}-%{version}.tar.gz

%description
Littlecms is a small speed optimized color management engine.
Little CMS intends to be a small-footprint color management engine
with a special focus on accuracy and performance. It uses the International
Color Consortium standard (ICC), which is the modern standard when
regarding to color management. The ICC specification is widely used and is
referred to in many International and other de-facto standards.

%package -n %{lname}
Summary:        Libraries for the Little CMS Engine
Group:          System/Libraries

%description -n %{lname}
Little CMS Engine - A color managment library and tools.

%package -n liblcms2-devel
Summary:        Include Files and Libraries Mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version} glibc-devel

%description -n liblcms2-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n liblcms2-doc
Summary:        User and developer documentation for lcms2
Group:          Documentation/Other
BuildArch:      noarch

%description -n liblcms2-doc
This package contains user and developer documentation for lcms2.


%prep
%setup -q

chmod a-x doc/* COPYING AUTHORS

%build

%configure --disable-static

make %{?_smp_flags}

%install

%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING AUTHORS
%{_bindir}/*
%{_mandir}/man?/*.*

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/liblcms2.so.2*

%files -n liblcms2-devel
%defattr(-,root,root)

%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n liblcms2-doc
%defattr(-,root,root)
%doc doc/*.pdf
