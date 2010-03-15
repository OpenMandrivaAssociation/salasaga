Summary: An Integrated Development Environment for producing Elearning
Name: salasaga
Version: 0.8.0
%define beta alpha7
Release: %mkrel -c %beta 1
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/salasaga
/usr/bin/salasaga_screencapture
/usr/share/pixmaps/salasaga-icon.png
/usr/share/applications/salasaga.desktop
/usr/share/salasaga
/usr/share/locale/ar/LC_MESSAGES/salasaga.mo
/usr/share/locale/bg/LC_MESSAGES/salasaga.mo
/usr/share/locale/ca/LC_MESSAGES/salasaga.mo
/usr/share/locale/el/LC_MESSAGES/salasaga.mo
/usr/share/locale/en_AU/LC_MESSAGES/salasaga.mo
/usr/share/locale/en_GB/LC_MESSAGES/salasaga.mo
/usr/share/locale/es/LC_MESSAGES/salasaga.mo
/usr/share/locale/fil/LC_MESSAGES/salasaga.mo
/usr/share/locale/fr/LC_MESSAGES/salasaga.mo
/usr/share/locale/gl/LC_MESSAGES/salasaga.mo
/usr/share/locale/id/LC_MESSAGES/salasaga.mo
/usr/share/locale/it/LC_MESSAGES/salasaga.mo
/usr/share/locale/nb/LC_MESSAGES/salasaga.mo
/usr/share/locale/pt/LC_MESSAGES/salasaga.mo
/usr/share/locale/pt_BR/LC_MESSAGES/salasaga.mo
/usr/share/locale/ro/LC_MESSAGES/salasaga.mo
/usr/share/locale/ru/LC_MESSAGES/salasaga.mo
/usr/share/locale/tr/LC_MESSAGES/salasaga.mo
/usr/share/locale/zh_CN/LC_MESSAGES/salasaga.mo

