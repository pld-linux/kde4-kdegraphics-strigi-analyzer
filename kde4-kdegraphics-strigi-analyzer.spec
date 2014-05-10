%define		_state		stable
%define		orgname		kdegraphics-strigi-analyzer
%define		qtver		4.8.0

Summary:	K Desktop Environment - Strigi analyzers for various graphic types
Name:		kde4-kdegraphics-strigi-analyzer
Version:	4.13.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	123745a5899432ac2842dae63ce84af5
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libtiff-devel
BuildRequires:	strigi-devel
Obsoletes:	kde4-kdegraphics-kfile < 4.6.99
Obsoletes:	kdegraphics-strigi-analyzer <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Strigi analyzers for various graphic types.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/strigi/strigiea_dvi.so
%attr(755,root,root) %{_libdir}/strigi/strigiea_tiff.so
