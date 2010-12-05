%define name python-exiv2
%define version 0.2.2
%define release %mkrel 1

Summary:	Python binding to exiv2
Name:		%{name}
Version:	%{version}
License:	GPLv2+
Group:		Development/Python 
Release:	%{release}
Source:		http://tilloy.net/dev/pyexiv2/releases/pyexiv2-%{version}.tar.bz2
Patch2:		pyexiv2-0.2.2-exiv2-0.21.patch
Patch3:		pyexiv2-0.2.2-link.patch
URL:		http://tilloy.net/dev/pyexiv2/
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:  libexiv-devel
BuildRequires:  boost-devel
BuildRequires:	scons
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
%py_platsitedir/*

%prep
%setup -q -n pyexiv2-%{version}
%patch2 -p0
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
