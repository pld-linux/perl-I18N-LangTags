#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	I18N
%define	pnam	LangTags
Summary:	I18N::LangTags module - dealing with RFC3066-style language tags
Summary(pl):	Modu� I18N::LangTags - obs�uga oznacze� j�zyk�w w stylu RFC3066
Name:		perl-I18N-LangTags
Version:	0.29
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c7ea4ee671b58e4088f7791c02fa945
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I18N::LangTags - functions for dealing with RFC3066-style language
tags.

%description -l pl
I18N::LangTags - funkcje do operowania na oznaczeniach j�zyk�w
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
