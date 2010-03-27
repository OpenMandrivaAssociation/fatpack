%define upstream_name    App-FatPacker
%define upstream_version 0.009001

Name:       fatpack
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Pack your dependencies onto your script file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_bindir}/fatpack
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*


