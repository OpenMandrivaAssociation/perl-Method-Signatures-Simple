%define upstream_name    Method-Signatures-Simple
Name:		perl-%{upstream_name}
Version:	1.07
Release:	2

Summary:	Basic method declarations with signatures, without source filters
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rhesa/method-signatures-simple
Source0:	https://cpan.metacpan.org/authors/id/R/RH/RHESA/Method-Signatures-Simple-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Devel::Declare)
BuildRequires:	perl(Module::Implementation)
BuildArch:	noarch

%description
Basic method declarations with signatures, without source filters.

%prep
%setup -q -n %{upstream_name}-%{version}

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
