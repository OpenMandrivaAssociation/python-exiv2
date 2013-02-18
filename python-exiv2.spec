Name:		python-exiv2
Version:	0.3.0
Release:	4
Summary:	Python binding to exiv2
License:	GPLv2+
Group:		Development/Python
Source:		http://tilloy.net/dev/pyexiv2/releases/pyexiv2-%{version}.tar.bz2
Patch3:		pyexiv2-0.2.2-link.patch
URL:		http://tilloy.net/dev/pyexiv2/
BuildRequires:	libexiv-devel
BuildRequires:	boost-devel
BuildRequires:	scons
BuildRequires:	python >= 2.7
Provides:	pyexiv2 = %{version}

%description
pyexiv2 is a python binding to exiv2, the C++ library for
manipulation of EXIF and IPTC image metadata. It is a python module
that allows your python scripts to read and write metadata (EXIF,
IPTC, thumbnail) embedded in image files (JPEG, TIFF, ...).

It is designed as a high level interface to the functionalities
offered by exiv2 (and is built on top of it). Using python's built-in
data types and standard modules, it provides easy manipulation of
image metadata.

%files
%defattr(-,root,root,-)
%doc todo README
%{py_platsitedir}/*

%prep
%setup -q -n pyexiv2-%{version}
%patch3 -p0

%build
%setup_compile_flags
%scons

%install
%__rm -rf %{buildroot}
%setup_compile_flags
%scons_install

%clean
%__rm -rf %{buildroot}


%changelog
* Mon Jul 02 2012 Crispin Boylan <crisb@mandriva.org> 0.3.0-3
+ Revision: 807857
- Rebuild for new boost

* Tue Apr 03 2012 Crispin Boylan <crisb@mandriva.org> 0.3.0-2
+ Revision: 789037
- Rebuild for new boost

* Wed Feb 01 2012 Andrey Bondrov <abondrov@mandriva.org> 0.3.0-1
+ Revision: 770364
- New version 0.3.0

* Thu Mar 17 2011 Funda Wang <fwang@mandriva.org> 0.2.2-2
+ Revision: 645714
- rebuild

* Sun Dec 05 2010 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 609584
- add versioned provides
- new version 0.2.2

* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 0.1.3-10mdv2011.0
+ Revision: 598992
- rebuild for py2.7

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 0.1.3-9mdv2011.0
+ Revision: 572531
- rebuild for new boost

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 0.1.3-8mdv2011.0
+ Revision: 566292
- rebuild for new boost

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 0.1.3-7mdv2011.0
+ Revision: 565546
- rebuild for new exiv2

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.1.3-6mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.1.3-5mdv2010.1
+ Revision: 500337
- rebuild for new boost

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 0.1.3-4mdv2010.1
+ Revision: 486835
- Add upstream patch (via Debian) to fix build with exiv2 0.19
- Rebuild for new libexiv2

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new exiv

* Mon Aug 24 2009 Funda Wang <fwang@mandriva.org> 0.1.3-2mdv2010.0
+ Revision: 420245
- rebuild for new libboost

  + John Balcaen <mikala@mandriva.org>
    - Clean spec file

* Tue Aug 11 2009 John Balcaen <mikala@mandriva.org> 0.1.3-1mdv2010.0
+ Revision: 414504
- Fix BuildRequires
- Add Patch for lib64 path support
- import python-exiv2

