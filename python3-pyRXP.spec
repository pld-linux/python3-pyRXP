# TODO:
# - use external rxp
#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A Python wrapper for the RXP parser
Summary(pl.UTF-8):	Pythonowy interfejs do analizatora XML RXP
Name:		python3-pyRXP
Version:	3.0.1
Release:	2
License:	GPL v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyRXP/
Source0:	https://files.pythonhosted.org/packages/source/p/pyRXP/pyRXP-%{version}.tar.gz
# Source0-md5:	3942f6c321f34d25b3d951b01b4e79d8
URL:		https://pypi.org/project/pyRXP/
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyRXP is a Python wrapper for RXP, a validating namespace-aware
XML parser in C.

%description -l pl.UTF-8
pyRXP to pythonowy interfejs do RXP - kontrolującego poprawność
analizatora XML-a z obsługą przestrzeni nazw, napisanego w C.

%package doc
Summary:	Documentation for Python pyRXP module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona pyRXP
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
This package contains documentation files for Python pyRXP module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona pyRXP.

%prep
%setup -q -n pyRXP-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(readlink -f build-3/lib.*) \
%{__python3} test/runAll.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{py3_sitedir}/pyRXPU.cpython-*.so
%{py3_sitedir}/pyRXP-%{version}-py*.egg-info

%files doc
%defattr(644,root,root,755)
%doc docs/*.{gif,html}
