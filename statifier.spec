Summary:	Convert elf dynamic linked exe to "pseudo-static"
Summary(pl):	Konwersja dynamicznych binarek ELF do pseudo-statycznych
Name:		statifier
Version:	1.5.0
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/statifier/%{name}-%{version}.tar.gz
# Source0-md5:	bf61de9dba74cce8708b21b1b39184c4
URL:		http://statifier.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch alpha amd64 ia64 ppc64 s390x sparc64
%define bits 64
%else
%define bits 32
%endif

%description
Statifier create from dynamically linked ELF executable and all it's
libraries (and all LD_PRELOAD libraries if any) one file. This file
can be copied and run on another machine without need to drag all it's
libraries.

%description -l pl
Statifier tworzy z dynamicznie zlinkowanej binarki ELF i wszystkich
jej bibliotek (oraz wszystkich bibliotek LD_PRELOAD je¿eli takie
wystêpuj±) jeden plik. Ten plik mo¿e byæ kopiowany i uruchamiany na
innej maszynie bez potrzeby przenoszenia wszystkich bibliotek.

%prep
%setup -q

%build
%{__make} all \
	FLAGS_ELF="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ INSTALL NEWS README THANKS TODO doc
%attr(755,root,root) %{_bindir}/statifier
%dir %{_libdir}/%{name}
%{_libdir}/statifier/VERSION
%attr(755,root,root) %{_libdir}/statifier/*.sh
%attr(755,root,root) %{_libdir}/statifier/*.src
%attr(755,root,root) %{_libdir}/statifier/*.gdb
%dir %{_libdir}/%{name}/%{bits}
%attr(755,root,root) %{_libdir}/statifier/%{bits}/*
%{_mandir}/man?/*
