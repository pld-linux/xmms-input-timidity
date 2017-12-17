Summary:	MIDI music input plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzająca muzykę w formacie MIDI
Name:		xmms-input-timidity
Version:	0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/libtimidity/xmms-timidity-%{version}.tar.gz
# Source0-md5:	dd5534afab254201e849eb3f4750a6ca
URL:		http://libtimidity.sourceforge.net/
BuildRequires:	libtimidity-devel >= 0.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 2:1.2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the MIDI input plugin for XMMS. This plugin plays MIDI files
using libtimidity.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę wejściową MIDI dla XMMS-a. Odtwarza pliki
MIDI przy użyciu libtimidity.

%prep
%setup -q -n xmms-timidity-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{xmms_input_plugindir}/libtimidity.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{xmms_input_plugindir}/libtimidity.so
