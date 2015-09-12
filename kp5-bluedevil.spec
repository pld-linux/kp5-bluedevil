%define		kdeplasmaver	5.4.0
%define		qtver		5.3.2
%define		kpname		bluedevil
Summary:	Integrate the Bluetooth technology within KDE workspace and applications
Name:		kp5-%{kpname}
Version:	5.4.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	fbe40c558185fec6cba4087e42d3f8e8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-bluez-qt-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
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
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang bluedevil --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f bluedevil.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bluedevil-sendfile
%attr(755,root,root) %{_bindir}/bluedevil-wizard
%attr(755,root,root) %{_libdir}/bluedevil-authorize
%attr(755,root,root) %{_libdir}/bluedevil-requestconfirmation
%attr(755,root,root) %{_libdir}/bluedevil-requestpin
%attr(755,root,root) %{_libdir}/qt5/plugins/bluetoothfileitemaction.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_bluedeviladapters.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_bluedevildevices.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_bluedevilglobal.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/bluedevil.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/obexftpdaemon.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kio_bluetooth.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kio_obexftp.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth
%{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
%{_desktopdir}/org.kde.bluedevilsendfile.desktop
%{_desktopdir}/org.kde.bluedevilwizard.desktop
%dir %{_datadir}/bluedevilwizard
%{_datadir}/bluedevilwizard/pin-code-database.xml
%{_datadir}/knotifications5/bluedevil.notifyrc
%{_datadir}/kservices5/bluedeviladapters.desktop
%{_datadir}/kservices5/bluedevildevices.desktop
%{_datadir}/kservices5/bluedevilglobal.desktop
%{_datadir}/kservices5/bluedevilsendfile.desktop
%{_datadir}/kservices5/bluetooth.protocol
%{_datadir}/kservices5/obexftp.protocol
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.bluetooth.desktop
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth
%{_datadir}/remoteview/bluetooth-network.desktop
