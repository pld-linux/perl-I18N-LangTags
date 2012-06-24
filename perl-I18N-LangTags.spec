#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# it doesn't like environment set by our automatics
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	I18N
%define		pnam	LangTags
Summary:	I18N::LangTags Perl module - dealing with RFC3066-style language tags
Summary(pl.UTF-8):   Moduł Perla I18N::LangTags - obsługa oznaczeń języków w stylu RFC3066
Name:		perl-I18N-LangTags
Version:	0.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	baa1e87e8559f488997081a7cb837f66
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I18N::LangTags - functions for dealing with RFC3066-style language
tags.

%description -l pl.UTF-8
I18N::LangTags - funkcje do operowania na oznaczeniach języków
zgodnych z RFC3066.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/I18N/LangTags.pm
%{perl_vendorlib}/I18N/LangTags
%{_mandir}/man3/*
