#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-IKC
Summary:	POE::Component::IKC - POE Inter-Kernel Communication
Summary(pl):	POE::Component::IKC - komunikacja wewn±trz j±dra POE
Name:		perl-POE-Component-IKC
Version:	0.1802
Release:	0.1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d76686340a6f13d024e7fb96891e3258
URL:		http://search.cpan.org/dist/POE-Component-IKC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-POE >= 0.28
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This a first draft if Inter-Kernel Communication for POE. It is
intended as a point of reference for discusion of issues involved.

%description -l pl
To jest pierwszy szkic komunikacji wewn±trz j±dra dla POE. Ma byæ
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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install client client2 client3 lclient $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install server server2 userver $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install shut-client shut-server test-lite test-client $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO FUTUR ikc-architecture.txt
%{perl_vendorlib}/POE/Component/IKC.pm
%dir %{perl_vendorlib}/POE/Component/IKC
%{perl_vendorlib}/POE/Component/IKC/*.pm
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
