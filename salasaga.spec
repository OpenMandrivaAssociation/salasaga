Summary: An Integrated Development Environment for producing Elearning
Name: salasaga
Version: 0.8.0
%define beta alpha7
Release: %mkrel -c %beta 2
License: LGPL3+
Group: Education
URL: http://www.salasaga.org
Source0: http://www.salasaga.org/downloads/%beta/%{name}-%{version}-%{beta}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ming-devel
BuildRequires: gtk+2-devel
BuildRequires: libxml2-devel
BuildRequires: libgnome2-devel
BuildRequires: libnotify-devel

%description
A free, easy to use GUI authoring environment that helps you create
visually impressive, useful learning material.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/pixmaps/salasaga-icon.png
%{_datadir}/applications/salasaga.desktop
%{_datadir}/salasaga
