Summary:	Calendar for Xfce
Summary(pl):	Kalendarz dla Xfce
Name:		orage
Version:	4.3.99.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	40607e4b116c4d298745ef0672826cd8
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= %{version}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Obsoletes:	xfcalendar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orage is a time-managing application that is part of the Xfce Desktop
Environment and features a calendar window, lists of events and
reminders. It also provides an easy way to archive and manage your old
appointments.

%description -l pl
Orage to aplikacja do zarz±dzania czasem bêd±ca czê¶ci± ¶rodowiska
graficznego Xfce. Zawiera okno kalendarza, listê wydarzeñ i
przypominajek. Udostêpnia tak¿e ³atwy sposób archiwizowania i
zarz±dzania starymi spotkaniami.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po
mv -f po/{nb_NO,nb}.po

%build
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

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.la

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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*
%{_datadir}/orage
%{_desktopdir}/*.desktop
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_iconsdir}/hicolor/*/*/*
