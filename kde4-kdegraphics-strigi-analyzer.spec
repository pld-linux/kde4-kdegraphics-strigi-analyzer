%define		_state		stable
%define		orgname		kdegraphics-strigi-analyzer
%define		qtver		4.8.0

Summary:	K Desktop Environment - Strigi analyzers for various graphic types
Name:		kde4-kdegraphics-strigi-analyzer
Version:	4.14.3
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	f8a48a2a44f2c6352e6cb9f68bb97591
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
