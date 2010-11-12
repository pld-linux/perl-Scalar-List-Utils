#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Scalar
%define		pnam	List-Utils
Summary:	List::Util and Scalar::Util - selection of general-utility scalar subroutines
Summary(pl.UTF-8):	List::Util i Scalar::Util - wybór procedur skalarnych ogólnego zastosowania
Name:		perl-Scalar-List-Utils
Version:	1.23
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e7909f8737cd6eecd8520b77326916b
URL:		http://search.cpan.org/dist/Scalar-List-Utils/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%doc Change* README
%dir %{perl_vendorarch}/List
%{perl_vendorarch}/List/*.pm
%dir %{perl_vendorarch}/List/Util
%{perl_vendorarch}/List/Util/*.pm
%dir %{perl_vendorarch}/Scalar
%{perl_vendorarch}/Scalar/*.pm
%dir %{perl_vendorarch}/Scalar/Util
%{perl_vendorarch}/Scalar/Util/*.pm
%dir %{perl_vendorarch}/auto/List
%dir %{perl_vendorarch}/auto/List/Util
%attr(755,root,root) %{perl_vendorarch}/auto/List/Util/*.so
%{perl_vendorarch}/auto/List/Util/*.bs
%{_mandir}/man3/*
