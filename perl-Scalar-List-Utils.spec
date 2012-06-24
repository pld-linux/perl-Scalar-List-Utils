#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Scalar
%define		pnam	List-Utils
Summary:	List::Util and Scalar::Util perl modules
Summary(pl):	Modu�y perla List::Util i Scalar::Util
Name:		perl-Scalar-List-Utils
Version:	1.13
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2b1ccf73ba7f290021587b3a681a9e69
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a selection of subroutines that people have
expressed would be nice to have in the perl core, but the usage would
not really be high enough to warrant the use of a keyword, and the size
so small such that being individual extensions would be wasteful.

%description -l pl
Ten pakiet zawiera wybrane procedury, kt�re wed�ug niekt�rych ludzi
powinny znale�� si� w g��wnym pakiecie Perla, ale u�yteczno�� nie jest
zbyt du�a, a rozmiar za ma�y na tworzenie oddzielnych rozszerze�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL -xs \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_vendorarch}/List
%{perl_vendorarch}/List/*.pm
%dir %{perl_vendorarch}/Scalar
%{perl_vendorarch}/Scalar/*.pm
%dir %{perl_vendorarch}/auto/List
%dir %{perl_vendorarch}/auto/List/Util
%attr(755,root,root) %{perl_vendorarch}/auto/List/Util/*.so
%{perl_vendorarch}/auto/List/Util/*.bs
%{_mandir}/man3/*
