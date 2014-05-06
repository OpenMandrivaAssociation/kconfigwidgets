%define major 5
%define libname %mklibname KF5ConfigWidgets %{major}
%define devname %mklibname KF5ConfigWidgets -d
%define debug_package %{nil}

Name: kconfigwidgets
Version: 4.98.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
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

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*
