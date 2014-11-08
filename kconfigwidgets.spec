%define major 5
%define libname %mklibname KF5ConfigWidgets %{major}
%define devname %mklibname KF5ConfigWidgets -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kconfigwidgets
Version: 5.4.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: KDE Frameworks 5 library for providing configuration frontends
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5DocTools)
BuildRequires: extra-cmake-modules5
BuildRequires: kauth
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
Requires: %{libname} = %{EVRD}

%description
KDE Frameworks 5 library for providing configuration frontends.

%package -n %{libname}
Summary: KDE Frameworks 5 library for providing configuration frontends
Group: System/Libraries

%description -n %{libname}
KDE Frameworks 5 library for providing configuration frontends.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}
Requires: extra-cmake-modules5
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
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5
%find_lang kconfigwidgets5

%files -f kconfigwidgets5.lang
%{_bindir}/*
%{_datadir}/kf5/%{name}
%{_datadir}/locale/*/kf5_entry.desktop
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
