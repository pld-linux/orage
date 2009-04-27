Summary:	Calendar for Xfce
Summary(pl.UTF-8):	Kalendarz dla Xfce
Name:		orage
Version:	4.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	24fa43dd86ec5af5a4766620fd972cf2
URL:		http://www.xfce.org/projects/orage/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= %{version}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Obsoletes:	xfcalendar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orage is a time-managing application that is part of the Xfce Desktop
Environment and features a calendar window, lists of events and
reminders. It also provides an easy way to archive and manage your old
appointments.

%description -l pl.UTF-8
Orage to aplikacja do zarządzania czasem będąca częścią środowiska
graficznego Xfce. Zawiera okno kalendarza, listę wydarzeń i
przypominajek. Udostępnia także łatwy sposób archiwizowania i
zarządzania starymi spotkaniami.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/globaltime
%attr(755,root,root) %{_bindir}/orage
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/orageclock
%{_datadir}/orage
%{_desktopdir}/xfcalendar.desktop
%{_desktopdir}/xfce-xfcalendar-settings.desktop
%{_datadir}/dbus-1/services/org.xfce.calendar.service
%{_datadir}/dbus-1/services/org.xfce.orage.service
%{_datadir}/xfce4/panel-plugins/orageclock.desktop
%{_mandir}/man1/globaltime.1*
%{_mandir}/man1/orage.1*
%{_iconsdir}/hicolor/*/*/*
