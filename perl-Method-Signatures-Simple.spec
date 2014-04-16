%define upstream_name    Method-Signatures-Simple
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Basic method declarations with signatures, without source filters
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Method/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::Declare)
BuildRequires:	perl(Module::Implementation)
BuildArch:	noarch

%description
Basic method declarations with signatures, without source filters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*
