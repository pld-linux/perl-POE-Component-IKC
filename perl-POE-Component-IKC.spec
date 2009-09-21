#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-IKC
Summary:	POE::Component::IKC - POE Inter-Kernel Communication
Summary(pl.UTF-8):	POE::Component::IKC - komunikacja wewnątrz jądra POE
Name:		perl-POE-Component-IKC
Version:	0.2200
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e185f5c1e070451156c7415d0676eec
URL:		http://search.cpan.org/dist/POE-Component-IKC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-POE >= 2:1
BuildRequires:	perl-POE-API-Peek >= 1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This a first draft if Inter-Kernel Communication for POE. It is
intended as a point of reference for discusion of issues involved.

%description -l pl.UTF-8
To jest pierwszy szkic komunikacji wewnątrz jądra dla POE. Ma być
punktem odniesienia do dyskutowania napotkanych problemów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO FUTUR ikc-architecture.txt
%{perl_vendorlib}/POE/Component/IKC.pm
%dir %{perl_vendorlib}/POE/Component/IKC
%{perl_vendorlib}/POE/Component/IKC/*.pm
%{_mandir}/man3/*
