%define major 5
%define libname %mklibname KF5ConfigWidgets %{major}
%define devname %mklibname KF5ConfigWidgets -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kconfigwidgets
Version:	5.26.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 library for providing configuration frontends
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5DocTools)
BuildRequires: kauth
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Test)
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 library for providing configuration frontends.

%package -n %{libname}
Summary: KDE Frameworks 5 library for providing configuration frontends
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Frameworks 5 library for providing configuration frontends.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}
Requires: cmake(ECM)
Requires: cmake(KF5Auth)
Requires: cmake(KF5Codecs)
Requires: cmake(KF5Config)
Requires: cmake(KF5GuiAddons)
Requires: cmake(KF5I18n)
Requires: cmake(KF5WidgetsAddons)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kconfigwidgets5

%files -f kconfigwidgets5.lang
%{_bindir}/*
%{_datadir}/locale/*/kf5_entry.desktop
%{_mandir}/man1/*
%optional %lang(ca) %{_mandir}/ca/man1/*
%optional %lang(de) %{_mandir}/de/man1/*
%optional %lang(it) %{_mandir}/it/man1/*
%optional %lang(nl) %{_mandir}/nl/man1/*
%optional %lang(pt_BR) %{_mandir}/pt_BR/man1/*
%optional %lang(ru) %{_mandir}/ru/man1/*
%optional %lang(sv) %{_mandir}/sv/man1/*
%optional %lang(uk) %{_mandir}/uk/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
