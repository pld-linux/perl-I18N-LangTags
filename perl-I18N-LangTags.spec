%include	/usr/lib/rpm/macros.perl
Summary:	I18N-LangTags perl module
Summary(pl):	Modu³ perla I18N-LangTags
Name:		perl-I18N-LangTags
Version:	0.23
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/I18N/I18N-LangTags-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I18N-LangTags - functions for dealing with RFC1766-style language
tags.

%description -l pl
I18N-LangTags - funkcje do operowania na oznaczeniach jêzyków zgodnych
z RFC1766.

%prep
%setup -q -n I18N-LangTags-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/I18N/LangTags.pm
%{_mandir}/man3/*
