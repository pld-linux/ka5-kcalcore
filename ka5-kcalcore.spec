%define		kdeappsver	19.04.1
%define		qtver		5.9.0
%define		kaname		kcalcore
Summary:	kcalcore
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	3
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8719a91a0a333d4da2ede7e478cd3c20
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Test-devel >= 5.9.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	libical-devel >= 2.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides access to and handling of calendar data. It
supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP.

A calendar contains information like incidences (events, to-dos,
journals), alarms, time zones, and other useful information. This API
provides access to that calendar information via well known calendar
formats iCalendar (or iCal) and the oolder vCalendar.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
/etc/xdg/kcalcore.categories
/etc/xdg/kcalcore.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5CalendarCore.so.5
%attr(755,root,root) %{_libdir}/libKF5CalendarCore.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KCalCore
%{_includedir}/KF5/kcalcore_version.h
%{_libdir}/cmake/KF5CalendarCore
%attr(755,root,root) %{_libdir}/libKF5CalendarCore.so
%{_libdir}/qt5/mkspecs/modules/qt_KCalCore.pri
