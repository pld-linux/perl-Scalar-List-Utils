%include	/usr/lib/rpm/macros.perl
%define		pdir	Scalar
%define		pnam	List-Utils
Summary:	List::Util and Scalar::Util perl modules
Summary(pl):	Modu³y perla List::Util i Scalar::Util
Name:		perl-Scalar-List-Utils
Version:	1.11
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.005
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
%{__make} OPTIMIZE="%{rpmcflags}"
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
