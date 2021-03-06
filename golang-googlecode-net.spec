%global forgeurl        https://github.com/golang/net
%global goipath         golang.org/x/net
%global commit          db08ff08e8622530d9ed3a0e8ac279f6d4c02196

%global x_name          golang-golang-org-net

%gometa -i

Name:       golang-googlecode-net
Version:    0
Release:    0.47%{?dist}
Summary:    Supplementary Go networking libraries
License:    BSD
URL:        %{gourl}
Source0:    %{gosource}
Source1:    glide.lock
Source2:    glide.yaml

%description
%{summary}

%package -n %{x_name}-devel
Summary:       Supplementary Go networking libraries for golang.org/x/ imports

BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/encoding/charmap)
BuildRequires:  golang(golang.org/x/text/encoding/htmlindex)
BuildRequires:  golang(golang.org/x/text/secure/bidirule)
BuildRequires:  golang(golang.org/x/text/transform)
BuildRequires:  golang(golang.org/x/text/unicode/norm)

%description -n %{x_name}-devel

This package contains library source intended for building other packages
which use the supplementary Go text libraries with golang.org/x/ imports.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .

%install
files="$(find . -iname testdata)"
%goinstall $files glide.yaml glide.lock

%check
%gochecks -d icmp -d bpf -d http/httpproxy -d http/httpguts -d http2

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files -n %{x_name}-devel -f devel.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README.md CONTRIBUTING.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Jan Chaloupka <jchaloup@redhat.com>
- Upload glide files

* Thu Jun 14 2018 Robert-André Mauchin <zebob.m@gmail.com> -0-0.45.20180614gitdb08ff0
- Bump to db08ff08e8622530d9ed3a0e8ac279f6d4c02196

* Tue Mar 13 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.44.git66aacef
- Upload handcrated glide.lock and glide.yaml files

* Thu Mar 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.43.git66aacef
- Bump to 66aacef3dd8a676686c7ae3716979581e8b03c47
  related: #1326890

* Tue Feb 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.42.git1c05540
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.41.git1c05540
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.40.git1c05540
- Bump to upstream 1c05540f6879653db88113bc4a2b70aec4bd491f
  related: #1326890

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.39.gitf249948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.38.gitf249948
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.37.gitf249948
- Bump to upstream f2499483f923065a842d38eb4c7f1927e6fc6e6d
  related: #1326890

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.git4d38db7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.35.git4d38db7
- Polish the spec file
  related: #1326890

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.34.git4d38db7
- Enable devel and unit-test for epel7
  related: #1326890

* Mon Jul 25 2016 jchaloup <jchaloup@redhat.com> - 0-0.33.git4d38db7
- Bump to upstream 4d38db76854b199960801a1734443fd02870d7e1
  resolves: #1326890

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.32.git6acef71
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.31.git6acef71
- Bump to upstream 6acef71eb69611914f7a30939ea9f6e194c78172
  related: #1230677

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.30.git04b9de9
- https://fedoraproject.org/wiki/Changes/golang1.6

* Fri Feb 19 2016 jchaloup <jchaloup@redhat.com> - 0-0.29.git04b9de9
- Bump to upstream 04b9de9b512f58addf28c9853d50ebef61c3953e
  related: #1230677

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.git1bc0720
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.27.git1bc0720
- Bump to upstream 1bc0720082d79ce7ffc6ef6e523d00d46b0dee45
  related: #1230677

* Thu Sep 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.6.git446d52d
- Change deps on compiler(go-compiler)
- Update Arches
- Use %%license

* Wed Jul 29 2015 jchaloup <jchaloup@redhat.com> - 0-0.25.git446d52d
- Update of spec file to spec-2.0
  related: #1230677

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.24.git446d52d
- No debuginfo
  related: #1230677

* Thu Jul 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.23.git446d52d
- Bump to upstream 446d52dd4018303a13b36097e26d0888aca5d6ef
  related: #1230677

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.22.git7dbad50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 jchaloup <jchaloup@redhat.com> - 0-0.21.git7dbad50
- Bump to 7dbad50ab5b31073856416cdcfeb2796d682f844
  resolves: #1230677

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.20.git71586c3
- Bump to upstream 71586c3cf98f806af322c5a361660eb046e00501
- Repo moved to github, changing spec file header and globals

* Thu Dec 18 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.19.hg937a34c9de13
- Resolves: rhbz#1056185 disable ipv6 test
- also disable html/charset test

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.18.hg937a34c9de13
- Update to the latest commit 937a34c9de13c766c814510f76bca091dee06028
  related: #1009967

* Mon Nov 24 2014 jchaloup <jchaloup@redhat.com> - 0-0.17.hg90e232e2462d
- Extend import paths for golang.org/x/
- context test failing on master
  related: #1009967

* Mon Sep 29 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.16.hg90e232e2462d
- Resolves: rhbz#1147193 - update to latest upstream revision 
  90e232e2462dedc03bf3c93358da62d54d55dfb6
- don't redefine gopath, don't own dirs owned by golang
- use golang >= 1.2.1-3 for golang specific rpm macros
- preserve timestamps of copied files
- br stuff from golang-googlecode-text

* Fri Jul 11 2014 Vincent Batts <vbatts@fedoraproject.org> - 0-0.15.hg84a4013f96e0
- don't fail on ipv6 test bz1056185

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.hg84a4013f96e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.hg84a4013f96e0
- golang exclusivearch for el6+
- add check

* Fri Jan 17 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.hg84a4013f96e0
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.11.hg84a4013f96e0
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.10.hg84a4013f96e0
- removed double quotes from Provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.hg84a4013f96e0
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.8.hg84a4013f96e0
- exclusivearch as per golang package
- debug_package nil

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.7.hg
- install just the source code for devel package

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.6.hg
- All Provides listed explicitly

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.hg
- Provides corrected

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.hg
- comment cleanup
- build explanation

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.hg
- html/webkit/scripted ownership set
- codereview.cfg not packaged

* Fri Sep 20 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.hg
- IPv6 doesn't build
- Typo correction
- directory ownership taken care of

* Thu Sep 19 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.hg
- Initial fedora package
