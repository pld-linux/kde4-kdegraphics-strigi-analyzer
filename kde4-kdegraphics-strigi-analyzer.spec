%define		_state		stable
%define		orgname		kdegraphics-strigi-analyzer
%define		qtver		4.7.4

Summary:	K Desktop Environment - Strigi analyzers for various graphic types
Name:		kdegraphics-strigi-analyzer
Version:	4.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	fdf05d436b34c7001a919be4c5049a27
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libtiff-devel
BuildRequires:	strigi-devel
Obsoletes:	kde4-kdegraphics-kfile < 4.6.99
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
