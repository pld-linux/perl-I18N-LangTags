%include	/usr/lib/rpm/macros.perl
%define	pdir	I18N
%define	pnam	LangTags
Summary:	I18N::LangTags perl module
Summary(pl):	Modu³ perla I18N::LangTags
Name:		perl-I18N-LangTags
Version:	0.27
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I18N::LangTags - functions for dealing with RFC1766-style language
tags.

%description -l pl
I18N::LangTags - funkcje do operowania na oznaczeniach jêzyków zgodnych
z RFC1766.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/I18N/LangTags.pm
%{perl_sitelib}/I18N/LangTags
%{_mandir}/man3/*
