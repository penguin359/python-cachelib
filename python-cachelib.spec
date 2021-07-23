%global srcname cachelib

Name:           python-%{srcname}
Version:        0.2.0
Release:        2%{?dist}
Summary:        A collection of cache libraries with a common API

License:        BSD
URL:            https://pypi.org/project/cachelib/
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A collection of cache libraries with a common API.

Extracted from Werkzeug.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  memcached
BuildRequires:  redis
BuildRequires:  python3-devel
BuildRequires:  python3-pylibmc
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xprocess
BuildRequires:  python3-redis
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%check
# uWSGI is not packaged for Fedora so skip tests for that backend.
%pytest -v -r s -k 'not Uwsgi'

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.rst
%doc CHANGES.rst
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Matěj Grabovský <mgrabovs@redhat.com> - 0.2.0-1
- New upstream release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Matěj Grabovský <mgrabovs@redhat.com> - 0.1.1-1
- Initial package
