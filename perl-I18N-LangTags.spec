%include	/usr/lib/rpm/macros.perl
Summary:	I18N-LangTags perl module
Summary(pl):	Modu³ perla I18N-LangTags
Name:		perl-I18N-LangTags
Version:	0.12
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/I18N/I18N-LangTags-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
I18N-LangTags - functions for dealing with RFC1766-style language tags.

%description -l pl
I18N-LangTags - funkcje do operowania na oznaczeniach jêzyków zgodnych
z RFC1766.

%prep
%setup -q -n I18N-LangTags-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/I18N/LangTags
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/I18N/LangTags.pm
%{perl_sitearch}/auto/I18N/LangTags

%{_mandir}/man3/*
