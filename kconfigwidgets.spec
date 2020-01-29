%define major 5
%define libname %mklibname KF5ConfigWidgets %{major}
%define devname %mklibname KF5ConfigWidgets -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kconfigwidgets
Version:	5.66.0
Release:	2
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
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: cmake(Qt5UiPlugin)
# For Python bindings
BuildRequires: cmake(PythonModuleGeneration)
BuildRequires: pkgconfig(python3)
BuildRequires: python-qt5-core
BuildRequires: python-qt5-gui
BuildRequires: python-qt5-widgets
BuildRequires: python-kcodecs
BuildRequires: python-kcoreaddons
BuildRequires: python-kwidgetsaddons
BuildRequires: python-kconfig
BuildRequires: python-kauth
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%package -n python-%{name}
Summary: Python bindings for %{name}
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n python-%{name}
Python bindings for %{name}

%package designer
Summary: Qt Designer plugin for handling %{name} widgets
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description designer
Qt Designer plugin for handling %{name} widgets

%files designer
%{_libdir}/qt5/plugins/designer/*.so

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

[ -s %{buildroot}%{python_sitearch}/PyKF5/__init__.py ] || rm -f %{buildroot}%{python_sitearch}/PyKF5/__init__.py
# Let's not ship py2 crap unless and until something still needs it...
rm -rf %{buildroot}%{_libdir}/python2*

%find_lang kconfigwidgets5 --all-name --with-man

%files -f kconfigwidgets5.lang
%{_bindir}/*
%{_datadir}/locale/*/kf5_entry.desktop
%{_mandir}/man1/*
%{_datadir}/qlogging-categories5/kconfigwidgets.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}

%files -n python-%{name}
%dir %{python_sitearch}/PyKF5
%{python_sitearch}/PyKF5/KConfigWidgets.so
%dir %{_datadir}/sip/PyKF5
%{_datadir}/sip/PyKF5/KConfigWidgets
