%define		xfce_version	4.16.0
Summary:	Calendar for Xfce
Summary(pl.UTF-8):	Kalendarz dla Xfce
Name:		orage
Version:	4.18.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/orage/4.18/%{name}-%{version}.tar.bz2
# Source0-md5:	c12765da61022c710bb0d5aab3c9c56f
Patch0:		libical3.patch
URL:		https://www.xfce.org/projects/orage
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	libical-devel >= 0.43
BuildRequires:	libnotify-devel >= 0.3.2
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfce4-panel-devel >= %{xfce_version}
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme >= 0.12-4
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
#%patch0 -p1

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hy_AM

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/orage
%{_datadir}/orage
%{_desktopdir}/org.xfce.orage.desktop
%{_desktopdir}/org.xfce.orage-settings.desktop
%{_datadir}/dbus-1/services/org.xfce.orage.service
%{_datadir}/metainfo/org.xfce.orage.appdata.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/scalable/*/*.svg
