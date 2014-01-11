%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-ejb-3.1-api
Version:          1.0.2
Release:          8.1%{?dist}
Summary:          EJB 3.1 API

License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-ejb-api_spec.git jboss-ejb-3.1-api
# cd jboss-ejb-3.1-api/ && git archive --format=tar --prefix=jboss-ejb-3.1-api/ jboss-ejb-api_3.1_spec-1.0.2.Final | xz > jboss-ejb-3.1-api-1.0.2.Final.tar.xz
Source0:          jboss-ejb-3.1-api-%{namedversion}.tar.xz

BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin

Requires:         jboss-transaction-1.1-api
Requires:         jboss-jaxrpc-1.1-api
Requires:         jpackage-utils
Requires:         java
BuildArch:        noarch

%description
The Java EJB 3.1 API classes.

%package javadoc
Summary:          Javadocs for %{name}

Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-ejb-3.1-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-ejb-api_3.1_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/ $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc README LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
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

