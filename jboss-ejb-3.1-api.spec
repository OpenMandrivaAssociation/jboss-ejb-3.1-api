%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-ejb-3.1-api
Version:          1.0.2
Release:          11.3
Summary:          EJB 3.1 API
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
Url:              https://www.jboss.org
Source0:          https://github.com/jboss/jboss-ejb-api_spec/archive/jboss-ejb-api_3.1_spec-%{namedversion}.tar.gz

BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin

BuildArch:        noarch

%description
The Java EJB 3.1 API classes.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-ejb-api_spec-jboss-ejb-api_3.1_spec-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Jul 01 2014 Marek Goldmann <mgoldman@redhat.com> - 1.0.2-11
- New guidelines

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.2-9
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.2-7
- Resolves #961454 - Remove unneeded maven-checkstyle-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 29 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.2-4
- Remove unneeded BR: maven-eclipse-plugin

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.3-1
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.2-1
- Upstream release 1.0.2.Final

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.2-0.1.20120309git53fbe3
- Packaging after license cleanup upstream

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-2
- Using geronimo-jta instead of jboss-transactions

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Initial packaging

