%define upstream_name	 Object-Signature
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Generate cryptographic signatures for objects
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/PAR/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Object::Signature is an abstract base class that you can inherit from in order
to allow your objects to generate unique cryptographic signatures.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Changes lib/Object/Signature.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Object
%{_mandir}/*/*
