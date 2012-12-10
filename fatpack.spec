%define upstream_name    App-FatPacker
%define upstream_version 0.009003

Name:       fatpack
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Pack your dependencies onto your script file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-devel
BuildArch: noarch

%description
Pack your dependencies onto your script file

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_bindir}/fatpack
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.9.3-2mdv2011.0
+ Revision: 654827
- rebuild for updated spec-helper

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.9.3-1mdv2011.0
+ Revision: 561028
- update to 0.009003

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.9.2-1mdv2011.0
+ Revision: 552253
- update to 0.009002

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.9.1-1mdv2010.1
+ Revision: 527937
- import fatpack


* Sat Mar 27 2010 cpan2dist 0.009001-1mdv
- initial mdv release, generated with cpan2dist
