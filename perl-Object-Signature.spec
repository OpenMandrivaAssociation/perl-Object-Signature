%define upstream_name	 Object-Signature
%define upstream_version 1.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generate cryptographic signatures for objects
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/PAR/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Object::Signature is an abstract base class that you can inherit from in order
to allow your objects to generate unique cryptographic signatures.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Changes lib/Object/Signature.pm

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Object
%{_mandir}/*/*


%changelog
* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 648576
- update to new version 1.07

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 407955
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.05-4mdv2009.0
+ Revision: 258146
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.05-3mdv2009.0
+ Revision: 246259
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.05-1mdv2008.1
+ Revision: 123239
- kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 1.05-1mdv2007.0
+ Revision: 94371
- 1.05
- Import perl-Object-Signature

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2007.0
- new version
- spec cleanup
- rpmbuildupate aware
- fix directory ownership

* Thu Jan 05 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.03-1mdk
- First Mandriva release

