%define module	Object-Signature
%define name	perl-%{module}
%define version 1.05
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Generate cryptographic signatures for objects
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/PAR/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch

%description
Object::Signature is an abstract base class that you can inherit from in order
to allow your objects to generate unique cryptographic signatures.

%prep
%setup -q -n %{module}-%{version}
chmod 644 README Changes lib/Object/Signature.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Object
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


