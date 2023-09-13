#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.8
%define		qtver		5.15.2
%define		kpname		bluedevil
Summary:	Integrate the Bluetooth technology within KDE workspace and applications
Name:		kp5-%{kpname}
Version:	5.27.8
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	20ea225d337ae5450a2e5ba367bdb379
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf5-bluez-qt-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kded-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kirigami2-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Integrate the Bluetooth technology within KDE workspace and
applications.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang bluedevil --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f bluedevil.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bluedevil-sendfile
%attr(755,root,root) %{_bindir}/bluedevil-wizard
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/bluedevil.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/kio_bluetooth.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/kio_obexftp.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth
%{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
%{_desktopdir}/org.kde.bluedevilsendfile.desktop
%{_desktopdir}/org.kde.bluedevilwizard.desktop
%dir %{_datadir}/bluedevilwizard
%{_datadir}/bluedevilwizard/pin-code-database.xml
%{_datadir}/knotifications5/bluedevil.notifyrc
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth
%{_datadir}/remoteview/bluetooth-network.desktop
%{_datadir}/metainfo/org.kde.plasma.bluetooth.appdata.xml
%dir %{_datadir}/kpackage/kcms/kcm_bluetooth
%dir %{_datadir}/kpackage/kcms/kcm_bluetooth/contents
%dir %{_datadir}/kpackage/kcms/kcm_bluetooth/contents/ui
%{_datadir}/kpackage/kcms/kcm_bluetooth/contents/ui/Device.qml
%{_datadir}/kpackage/kcms/kcm_bluetooth/contents/ui/General.qml
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.bluetooth.desktop
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_bluetooth.so
%{_desktopdir}/kcm_bluetooth.desktop
%{_datadir}/kpackage/kcms/kcm_bluetooth/contents/ui/main.qml
%{_datadir}/qlogging-categories5/bluedevil.categories
