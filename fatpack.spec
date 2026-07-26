%define upstream_name    App-FatPacker
Name:       fatpack
Version:    0.010008
Release:    2

Summary:    Pack your dependencies onto your script file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://git.shadowcat.co.uk/gitweb/gitweb.cgi?p=p5sagit/App-FatPacker
Source0:    https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/App-FatPacker-%{version}.tar.gz

BuildRequires:	make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-devel

BuildArch: noarch

%description
Pack your dependencies onto your script file
Command line frontend for App::FatPacker  

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes META.yml
%{_bindir}/fatpack
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*




