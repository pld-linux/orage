Summary:	Calendar for Xfce
Summary(pl):	Kalendarz dla Xfce
Name:		orage
Version:	4.3.90.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-4.3.90.1/src/%{name}-%{version}.tar.bz2
# Source0-md5:	6f3432b282cd6883b41089f80b9a38be
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.6.4
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= %{version}
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
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_datadir}/orage
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
