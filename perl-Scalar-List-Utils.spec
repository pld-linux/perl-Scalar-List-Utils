#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Scalar
%define		pnam	List-Utils
Summary:	List::Util and Scalar::Util - selection of general-utility scalar subroutines
Summary(pl):	List::Util i Scalar::Util - wybór procedur skalarnych ogólnego zastosowania
Name:		perl-Scalar-List-Utils
Version:	1.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64f5c079fe9be0fff55c1365dd7eec96
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a selection of subroutines that people have
expressed would be nice to have in the perl core, but the usage would
not really be high enough to warrant the use of a keyword, and the size
so small such that being individual extensions would be wasteful.

%description -l pl
Ten pakiet zawiera wybrane procedury, które wed³ug niektórych ludzi
powinny znale¼æ siê w g³ównym pakiecie Perla, ale u¿yteczno¶æ nie jest
zbyt du¿a, a rozmiar za ma³y na tworzenie oddzielnych rozszerzeñ.

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
