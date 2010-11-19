%define name python-exiv2
%define version 0.1.3
%define release %mkrel 10

Summary:	Python binding to exiv2
Name:		%{name}
Version:	%{version}
License:	GPLv2+
Group:		Development/Python 
Release:	%{release}
Source:		http://tilloy.net/dev/pyexiv2/releases/pyexiv2-%{version}.tar.bz2
Patch0:		python-exiv-patch-forlib64.patch
Patch1:		python-exiv-0.19.patch
URL:		http://tilloy.net/dev/pyexiv2/
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:  libexiv-devel
BuildRequires:  boost-devel
BuildRequires:	scons
Provides:	pyexiv2

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
%doc ChangeLog  COPYING  README  todo
%py_platsitedir/libpyexiv2.so
%py_platsitedir/pyexiv2.py


%prep
%setup -q -n pyexiv2-%{version}
%patch0 -p0
%patch1 -p1 -b .exiv-0.19

%build
%scons

%install

%__rm -rf %{buildroot}
%scons_install

%clean
%__rm -rf %{buildroot}
