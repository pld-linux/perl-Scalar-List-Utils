# $Revision: 1.2 $
%include	/usr/lib/rpm/macros.perl
%define	pdir	Scalar
%define	pnam	List-Utils
Summary:	List::Util and Scalar::Util perl modules
Summary(pl):	Modu³y perla List::Util i Scalar::Util
Name:		perl-%{pdir}-%{pnam}
Version:	1.0701
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a selection of subroutines that people have
expressed would be nice to have in the perl core, but the usage would
not really be high enough to warrant the use of a keyword, and the size
so small such that being individual extensions would be wasteful.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL -xs
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitearch}/List/*.pm
%{perl_sitearch}/Scalar/*.pm
%dir %{perl_sitearch}/auto/List/Util
%attr(755,root,root) %{perl_sitearch}/auto/List/Util/*.so
%{perl_sitearch}/auto/List/Util/*.bs
%{_mandir}/man3/*
