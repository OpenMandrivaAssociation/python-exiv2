Name:		python-exiv2
Version:	0.3.0
Release:	3
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
