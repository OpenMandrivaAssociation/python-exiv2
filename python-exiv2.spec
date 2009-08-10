%define name python-exiv2
%define version 0.1.3
%define release %mkrel 1

Summary:	Python binding to exiv2
Name:		%{name}
Version:	%{version}
License:	GPLv2+
Group:		Development/Python 
Release:	%{release}
Source: http://tilloy.net/dev/pyexiv2/releases/pyexiv2-%{version}.tar.bz2
URL:		http://tilloy.net/dev/pyexiv2/
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:  libexiv-devel
BuildRequires:  scons
BuildRequires:	boost
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
%py_platlibdir/libpyexiv2.so
%py_platlibdir/pyexiv2.py

%prep
%setup -q -n pyexiv2-%{version}

%build
%scons

%install
%__rm -rf %{buildroot}

%__mkdir -p %{buildroot}/%py_platlibdir/

#%scons DESTDIR="%{buildroot}" install

#%scons_install
%__cp  build/libpyexiv2.so %{buildroot}/%py_platlibdir/
%__cp  src/pyexiv2.py %{buildroot}/%py_platlibdir/
%clean
%__rm -rf %{buildroot}

