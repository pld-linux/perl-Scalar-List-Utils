#
# perl modules provided by this package are part of perl distribution (perl-Scalar-List-Utils subpackage)
# DO NOT send this package to Th builders if version is <= provided from perl.spec
#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%define		pdir	Scalar
%define		pnam	List-Utils
Summary:	List::Util and Scalar::Util - selection of general-utility scalar subroutines
Summary(pl.UTF-8):	List::Util i Scalar::Util - wybór procedur skalarnych ogólnego zastosowania
Name:		perl-Scalar-List-Utils
Version:	1.62
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Scalar/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e5186779360f938c8ec83030c7b5a03
URL:		https://metacpan.org/release/Scalar-List-Utils
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
#BuildRequires:	th-blocker, not for ftp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a selection of subroutines that people have
expressed would be nice to have in the perl core, but the usage would
not really be high enough to warrant the use of a keyword, and the
size so small such that being individual extensions would be wasteful.

%description -l pl.UTF-8
Ten pakiet zawiera wybrane procedury, które według niektórych ludzi
powinny znaleźć się w głównym pakiecie Perla, ale użyteczność nie jest
zbyt duża, a rozmiar za mały na tworzenie oddzielnych rozszerzeń.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL -xs \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%doc Changes README
%dir %{perl_vendorarch}/List
%{perl_vendorarch}/List/Util.pm
%dir %{perl_vendorarch}/List/Util
%{perl_vendorarch}/List/Util/*.pm
%dir %{perl_vendorarch}/Scalar
%{perl_vendorarch}/Scalar/Util.pm
%dir %{perl_vendorarch}/Sub
%{perl_vendorarch}/Sub/Util.pm
%dir %{perl_vendorarch}/auto/List
%dir %{perl_vendorarch}/auto/List/Util
%attr(755,root,root) %{perl_vendorarch}/auto/List/Util/Util.so
%{_mandir}/man3/List::Util*.3pm*
%{_mandir}/man3/Scalar::Util.3pm*
%{_mandir}/man3/Sub::Util.3pm*
