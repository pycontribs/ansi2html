%if 0%{?rhel} == 3
%define __python_ver 2.3
%endif
%define python python%{?__python_ver}
%define __python /usr/bin/%{python}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		ansi2html
Version:	0.5.02
Release:	1%{?dist}
Summary:	Python module that converts text with ansi color to HTML

Group:		Development/Libraries
License:	GPLv3+
URL:		http://github.com/ralphbean/ansi2html
Source0:	http://pypi.python.org/packages/source/a/ansi2html/ansi2html-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python,python-setuptools
Requires:	python,python-genshi

%description
The ansi2html module can convert text with ansi color codes to HTML.


%prep
%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build


%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%if "%{python_version}" >= "2.5"
%dir %{python_sitelib}/%{name}*.egg-info
%{python_sitelib}/%{name}*.egg-info/*
%endif

%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/*.py*

%dir %{python_sitelib}/%{name}/templates
%{python_sitelib}/%{name}/templates/*.html


%changelog
* Tue Sep 7 2010 Ralph bean <ralph.bean@gmail.com> - 0.5.02-1
- Initial RPM packaging

