%if 0%{?fedora} ||  0%{?rhel} >= 8
%global build_py3   1
%global default_py3 1
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%define pythonX %{?default_py3: python3}%{!?default_py3: python2}

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define _binaries_in_noarch_packages_terminate_build 0
%global debug_package %{nil}
Summary: Boot server configurator
Name: cobbler
License: GPLv2+
AutoReq: no
Version: 2.0.7.1
Release: 6%{?dist}
Source0: cobbler-%{version}.tar.gz
Patch0: cobbler-pxelinux-s390x-bz580072.patch
Patch1: cobbler-xenpv-tap-driver.patch
Patch2: cobbler-koan-rhpl.patch
Patch3: koan-el6-ks-embed.patch
Patch4: cobbler-disable-check-selinux-bz706857.patch
Patch5: cobbler-disable-hardlinks-bz568801.patch
Patch6: cobbler-no-remove-pub-bz707215.patch
Patch7: cobbler-keep-ssh-snippet.patch
Patch8: cobbler-netaddr.patch
Patch9: cobbler-lvm-installation.patch
Patch10: koan-cmdline-length.patch
Patch11: cobbler-bz-253274.patch
Patch12: cobbler-token-validation.patch
Patch13: cobbler-ipv6-xmlrpc.patch
Patch14: cobbler-ipv6-snippet.patch
Patch15: koan-xz-initrd.patch
Patch16: cobbler-nic-dash.patch
Patch17: cobbler-power-vulnerability.patch
Patch18: cobbler-rhel6-bonding.patch
Patch19: cobbler-catch-cheetah-exception.patch
Patch20: cobbler-lvm-selinux.patch
Patch21: koan_no_selinux_set.patch
Patch22: cobbler-buildiso.patch
Patch23: cobbler-daemon.patch
Patch24: cobbler-rhel7-snippets.patch
Patch25: koan-rhel7-initramfs-embedding.patch
Patch26: cobbler-bootproto-post-install.patch
Patch27: cobbler-triggers.patch
Patch28: cobbler-concurrency.patch
Patch29: koan-rhel7-virtinst.patch
Patch30: koan-rhel7-ppc.patch
Patch31: cobbler-rhel7-distros.patch
Patch32: cobbler-remote-addr.patch
Patch34: cobbler-modprobe-d.patch
Patch35: cobbler-findks.patch
Patch36: koan-virt-install-options.patch
Patch37: cobbler-power-status.patch
Patch38: koan-no-check_output.patch
Patch39: koan-rhel71.patch
Patch40: cobbler-unicode-scripts.patch
Patch41: cobbler-bz1052857.patch
Patch42: buildiso-boot-options.patch
Patch43: cobbler-uudecode.patch
Patch44: buildiso-no-local-hdd.patch
Patch45: cobbler-s390-kernel-options.patch
Patch46: koan-s390-kernel-options-parse.patch
Patch47: koan-remove-root-argument.patch
Patch48: cobbler-updating-logrotate-config.patch
Patch49: cobbler-post-install-network-defaults.patch
Patch50: 0001-exceptions-module-doesn-t-have-to-be-imported.patch
Patch51: 0002-cleanup-ANCIENT_PYTHON-stuff-and-unused-imports.patch
Patch52: 0003-fixing-xmlrpclib-urllib2-and-local-imports-in-Python.patch
Patch53: 0004-Python-3-compatible-prints.patch
Patch54: 0005-Python-3-compatible-exceptions.patch
Patch55: 0006-octal-number-Python-3-fix.patch
Patch56: 0007-Python-3-compatible-string-operations.patch
Patch57: 0008-do-not-require-urlgrabber.patch
Patch58: 0009-replace-iteritems-with-items.patch
Patch59: 0010-open-target-file-in-binary-mode.patch
Patch60: 0011-make-sure-it-s-a-string.patch
Patch61: 0012-make-sure-list-is-returned.patch
Patch62: 0013-Python-3-ethtool-and-indentation-fixes.patch
Patch63: 0014-has_key-is-not-in-Python-3.patch
Patch64: 0015-relative-imports-don-t-work-on-both-Python-2-and-3.patch
Patch65: 0016-keys-and-sort-doesn-t-work-on-Python-3.patch
Patch66: 0017-raise-is-a-function-call-in-python3.patch
Patch67: 0018-adapt-setup.py-for-both-py2-and-py3.patch
Patch68: koan-grubby480.patch
Patch69: koan-fix-TypeError.patch
Patch70: koan-support-osinfo-query.patch
Patch71: koan-support-kvm-type.patch
Patch72: koan-bz1699743.patch

Group: Applications/System

%if 0%{?default_py3}
%if 0%{?fedora} && 0%{?fedora} < 21
BuildRequires: python3-setuptools-devel
%else
BuildRequires: python3-setuptools
%endif
%if 0%{?suse_version} < 0
BuildRequires: redhat-rpm-config
%endif
BuildRequires: python3-PyYAML
%endif

Requires: python >= 2.3
Provides: cobbler2 = %{version}-%{release}

%if 0%{?suse_version} >= 1000
Requires: apache2
Requires: apache2-mod_python
Requires: tftp
%else
Requires: httpd
Requires: tftp-server
%endif

%if 0%{?rhel} >= 6
Requires: mod_wsgi
Requires: ipmitool
%else
Requires: mod_python
%endif

Requires: createrepo
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
Requires: genisoimage
%else
Requires: mkisofs
%endif
Requires: libyaml
Requires: python-cheetah
Requires: python-devel
Requires: python-netaddr
Requires: python-simplejson
Requires: python-urlgrabber
Requires: PyYAML
Requires: rsync
%if 0%{?fedora} >= 6 || 0%{?rhel} >= 5
Requires: yum-utils
%endif

Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig

Requires(preun): /sbin/service
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]" || echo 0)}
Requires: python(abi) >= %{pyver}
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://fedorahosted.org/cobbler

%description

Cobbler is a network install server.  Cobbler 
supports PXE, virtualized installs, and 
reinstalling existing Linux machines.  The last two 
modes use a helper tool, 'koan', that 
integrates with cobbler.  There is also a web interface
'cobbler-web'.  Cobbler's advanced features 
include importing distributions from DVDs and rsync 
mirrors, kickstart templating, integrated yum 
mirroring, and built-in DHCP/DNS Management.  Cobbler has 
a XMLRPC API for integration with other applications.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p1
%patch12 -p0
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p0
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1

%build
%{pythonX} setup.py build 

%install
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT
%if 0%{?suse_version} >= 1000
PREFIX="--prefix=/usr"
%endif
%if 0%{?build_py3}
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' {scripts/koan,scripts/cobbler-register}
%endif
%{pythonX} setup.py install --optimize=1 --root=$RPM_BUILD_ROOT $PREFIX
mkdir -p $RPM_BUILD_ROOT/var/log/koan
mkdir -p $RPM_BUILD_ROOT/var/spool/koan
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
cp docs/cobbler-register.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/
cp docs/koan.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/
cp koan/*py $RPM_BUILD_ROOT/%{python3_sitelib}/koan/

%post
if [ "$1" = "1" ];
then
    # This happens upon initial install. Upgrades will follow the next else
    /sbin/chkconfig --add cobblerd
elif [ "$1" -ge "2" ];
then
    # backup config
    if [ -e /var/lib/cobbler/distros ]; then
        cp /var/lib/cobbler/distros*  /var/lib/cobbler/backup 2>/dev/null
        cp /var/lib/cobbler/profiles* /var/lib/cobbler/backup 2>/dev/null
        cp /var/lib/cobbler/systems*  /var/lib/cobbler/backup 2>/dev/null
        cp /var/lib/cobbler/repos*    /var/lib/cobbler/backup 2>/dev/null
        cp /var/lib/cobbler/networks* /var/lib/cobbler/backup 2>/dev/null
    fi
    if [ -e /var/lib/cobbler/config ]; then
        cp -a /var/lib/cobbler/config    /var/lib/cobbler/backup 2>/dev/null
    fi
    # upgrade older installs
    # move power and pxe-templates from /etc/cobbler, backup new templates to *.rpmnew
    for n in power pxe; do
      rm -f /etc/cobbler/$n*.rpmnew
      find /etc/cobbler -maxdepth 1 -name "$n*" -type f | while read f; do
        newf=/etc/cobbler/$n/`basename $f`
        [ -e $newf ] &&  mv $newf $newf.rpmnew
        mv $f $newf
      done
    done
    # upgrade older installs
    # copy kickstarts from /etc/cobbler to /var/lib/cobbler/kickstarts
    rm -f /etc/cobbler/*.ks.rpmnew
    find /etc/cobbler -maxdepth 1 -name "*.ks" -type f | while read f; do
      newf=/var/lib/cobbler/kickstarts/`basename $f`
      [ -e $newf ] &&  mv $newf $newf.rpmnew
      cp $f $newf
    done
    # reserialize and restart
    # FIXIT: ?????
    #/usr/bin/cobbler reserialize
    /sbin/service cobblerd condrestart
fi

%preun
if [ $1 = 0 ]; then
    /sbin/service cobblerd stop >/dev/null 2>&1 || :
    chkconfig --del cobblerd || :
fi

%postun
if [ "$1" -ge "1" ]; then
    /sbin/service cobblerd condrestart >/dev/null 2>&1 || :
    /sbin/service httpd condrestart >/dev/null 2>&1 || :
fi


%clean
test "x$RPM_BUILD_ROOT" != "x" && rm -rf $RPM_BUILD_ROOT

%package -n koan

Summary: Helper tool that performs cobbler orders on remote machines.
Group: Applications/System
%if 0%{?build_py3}
Requires: python3-koan
%else
Requires: python2-koan
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://fedorahosted.org/cobbler/

%description -n koan

Koan stands for kickstart-over-a-network and allows for both
network installation of new virtualized guests and reinstallation 
of an existing system.  For use with a boot-server configured with Cobbler

%files -n koan
%defattr(644,root,root,755)
# FIXME: need to generate in setup.py
%dir /var/spool/koan
%{_mandir}/man1/koan.1.gz
%{_mandir}/man1/cobbler-register.1.gz
%dir /var/log/koan
%doc AUTHORS COPYING CHANGELOG README

%if 0%{?build_py3}

%package -n python3-koan

Summary: Helper tool that performs cobbler orders on remote machines.
Group: Applications/System
%{?__python3:Requires: %{__python3}}
BuildRequires: python3-devel
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}
Requires: python(abi) >= %{pyver}
%endif
%if 0%{?fedora} && 0%{?fedora} < 21
BuildRequires: python3-setuptools-devel
%else
BuildRequires: python3-setuptools
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://fedorahosted.org/cobbler/


%description -n python3-koan

Koan stands for kickstart-over-a-network and allows for both
network installation of new virtualized guests and reinstallation 
of an existing system.  For use with a boot-server configured with Cobbler

%files -n python3-koan
%{_bindir}/koan
%{_bindir}/cobbler-register
%{python3_sitelib}/koan/
%{python3_sitelib}/koan-*.egg-info

%endif

%changelog
* Tue Apr 23 2019 Michael Mraka <michael.mraka@redhat.com> 2.0.7.1-6
- 1699743 - grubby --bootloader-probe has been deprecated

* Thu Mar 21 2019 Michael Mraka <michael.mraka@redhat.com> 2.0.7.1-5
- 1686794 - backported koan kvm support patch

* Wed Mar 06 2019 Michael Mraka <michael.mraka@redhat.com> 2.0.7.1-4
- removed patches which break RHEL8

* Tue Mar 05 2019 Michael Mraka <michael.mraka@redhat.com> 2.0.7.1-3
- remove broken unused dependency

* Mon Nov 12 2018 Tomas Kasparek <tkasparek@redhat.com> 2.0.7.1-2
- 1647351 - fix provisioning of RHEL8 virtual guests (tkasparek@redhat.com)

* Wed Nov 07 2018 Tomas Kasparek <tkasparek@redhat.com> 2.0.7.1-1
- Resolves: rhbz#1647355 - RHEL8 version should be higher than RHEL7

* Fri Oct 19 2018 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-6
- 1633713 - Require the Python interpreter directly instead of using the
  package name (tkasparek@redhat.com)

* Thu Oct 18 2018 Michael Mraka <michael.mraka@redhat.com> 2.0.7-5
- 1640635 - don't quote kernel args (michael.mraka@redhat.com)
- use python3 dependencies (tkasparek@redhat.com)

* Tue Jul 24 2018 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-4
- require python3 packages in buildtime (tkasparek@redhat.com)

* Tue Jul 24 2018 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-3
- fix bogus changelog date (nils@redhat.com)
- remove subpackages we don't ship (nils@redhat.com)
- deactivate main package BRs if we don't build it (nils@redhat.com)
- concentrate main package BRs in one place (nils@redhat.com)
- add tito.props for cobbler (tkasparek@redhat.com)

* Thu Mar 08 2018 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-2
- reset package release (tkasparek@redhat.com)
- package koan properly (tkasparek@redhat.com)
- python-urlgrabber is no longer needed in koan (tkasparek@redhat.com)
- don't build cobbler subpackage at all (tkasparek@redhat.com)
- build python3 version of koan (tkasparek@redhat.com)
- add python3 patches (tkasparek@redhat.com)
- resue cobbler from Satellite git (tkasparek@redhat.com)

* Tue Oct 31 2017 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-69
- 1178515 - use empty string when key is not defined in
  post_install_network_config snippet
- 1314379 - updating logrotate config to cobbler 2.8 state

* Mon Apr 25 2016 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-68
- 1208253 - remove the root= argument to prevent booting the current OS

* Wed Jan 13 2016 Grant Gainey 2.0.7-67
- 1279986 - Updated version for PPC64LE release

* Wed Dec 09 2015 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-66
- add system support to --no-local-hdd option without need of profiles

* Thu Oct 29 2015 Jan Dobes 2.0.7-65
- 1270676 - split only once for creating key-value pairs

* Mon Oct 05 2015 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-64
- 1078820 - timeout to 1st available profile with --no-local-hdd instead of
  local hdd

* Wed Sep 09 2015 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-63
- 1199214 - removing kernel options for s390 systems
- add option to skip local harddrive as buildiso entry

* Wed Jul 29 2015 Grant Gainey 2.0.7-62
- 1245769 - Apply fix to remaining codepath

* Tue Jul 28 2015 Grant Gainey 2.0.7-61
- Having a patch isn't enough, the spec has to actually *apply* it

* Wed Jul 22 2015 Grant Gainey 2.0.7-60
- Let cobbler handle urlencoded URLs (see upstream commit
  c9a51eec74a66d5034c47f08212177884642d70e  for full explanation)

* Mon Jun 29 2015 Jan Dobes 2.0.7-59
- Revert "fix adding netmask kernel parameter into isolinux.cfg"

* Thu Jun 25 2015 Tomas Kasparek <tkasparek@redhat.com> 2.0.7-58
- 1095198 - fixing multiple nameserver boot options on rhel7 and fedora
- fix adding netmask kernel parameter into isolinux.cfg

* Tue Jun 02 2015 Jan Dobes 2.0.7-57
- 1227340 - fixing order of cheetah keywords

* Wed May 20 2015 Grant Gainey 2.0.7-56
- 1052857 - fix typo in patch

* Wed May 06 2015 Stephen Herr <sherr@redhat.com> 2.0.7-55
- 1052857 - remove python timing window for incorrect file permissions
- 1096263 - set Cheetah templates to use UTF-8

* Thu Jan 22 2015 Stephen Herr <sherr@redhat.com> 2.0.7-54
- 1184595 - update koan to be compatible with rhel 7.1 virt-install

* Mon Jan 12 2015 Stephen Herr <sherr@redhat.com> 2.0.7-53
- 1181286 - check_output is only available on RHEL 7

* Fri Dec 05 2014 Tomas Lestach <tlestach@redhat.com> 2.0.7-52
- 1169741 - accept more power status messages

* Mon Dec 01 2014 Stephen Herr <sherr@redhat.com> 2.0.7-51
- 1162311 - remove comment from power template

* Mon Nov 10 2014 Stephen Herr <sherr@redhat.com> 2.0.7-50
- 1162337 - install ipmitool by default so that power management will work
- 1162311 - add status power command support to cobbler

* Thu Nov 06 2014 Stephen Herr <sherr@redhat.com> 2.0.7-49
- 1002467 - add optional virt-install options to koan
- cobbler (koan) is in RHN Tools which we build on all RHEL 5/6/7

* Fri Sep 26 2014 Stephen Herr <sherr@redhat.com> 2.0.7-48
- 1138710 - fixing arm-arch patch, cobbler-2.0.7 does not have cache arg

* Thu Sep 11 2014 Stephen Herr <sherr@redhat.com> 2.0.7-47
- 979966 - auto-trialing-whitespace trim broke patch file
- 905129 - add support for cobbler findks operation

* Thu Sep 11 2014 Michael Mraka <michael.mraka@redhat.com> 2.0.7-46
- 979966 - support modprobe.d on RHEL6

* Fri Sep 05 2014 Stephen Herr <sherr@redhat.com> 2.0.7-45
- 1138710 - cobbler should support provisioning aarch64 systems

* Mon Jun 02 2014 Stephen Herr <sherr@redhat.com> 2.0.7-44
- 1057785 - set REMOTE_ADDR for cobbler triggers

* Wed Apr 09 2014 Stephen Herr <sherr@redhat.com> 2.0.7-43
- 1051160 - update available distros to include rhel7

* Tue Mar 25 2014 Stephen Herr <sherr@redhat.com> 2.0.7-42
- 1073822 - koan needs to be grub2 aware for ppc

* Thu Dec 05 2013 Stephen Herr <sherr@redhat.com> 2.0.7-41
- 1029493 - fixing koan guest arch and kvm acceleration issue

* Fri Nov 22 2013 Stephen Herr <sherr@redhat.com> 2.0.7-40
- 1029493 - provisioning virtual guests on rhel 7 fails

* Thu Oct 24 2013 Stephen Herr <sherr@redhat.com> 2.0.7-39
- 1008967 - adding finally blocks to lock releases - cobbler concurrency

* Mon Oct 21 2013 Stephen Herr <sherr@redhat.com> 2.0.7-38
- 1008967 - better concurrency in cobbler

* Wed Jul 17 2013 Stephen Herr <sherr@redhat.com> 2.0.7-37
- 856944 - make cobbler triggers work

* Fri Jul 12 2013 Stephen Herr <sherr@redhat.com> 2.0.7-36
- 506485 - spaces in the source file mean you have to keep spaces in the patch

* Fri Jul 12 2013 Stephen Herr <sherr@redhat.com> 2.0.7-35
- 506485 - cobbler buildiso documentation updates

* Fri Jul 12 2013 Milan Zazrivec <mzazrivec@redhat.com> 2.0.7-34
- 895096 - correctly setup dhcp networking for new systems
- 886609 - Support for ks.cfg initramfs embedding on RHEL-7
- 883885 - pre/post install_network_config: RHEL-7 support

* Thu Jul 11 2013 Stephen Herr <sherr@redhat.com> 2.0.7-33
- 978601 - fixing cobbler buildiso selinux issue

* Tue Jun 18 2013 Michael Mraka <michael.mraka@redhat.com> 2.0.7-32
- 718238 - detach daemon from terminal

* Wed May 22 2013 Stephen Herr <sherr@redhat.com> 2.0.7-29
- 506485 - Cobbler buildiso changes
- update dist-git branches for cobbler

* Wed Apr 10 2013 Tomas Lestach <tlestach@redhat.com> 2.0.7-28
- 768451 - do not set selinux context for patition locations

* Wed Mar 27 2013 Stephen Herr <sherr@redhat.com> 2.0.7-27
- 768451 - bumping build number so the tag won't interfere with SATELLITE-5.5
- 768451 - actually adding the patch is a good thing
- 768451 - /dev/mapper doesn't work with lvm if selinux is on

* Tue Mar 19 2013 Michael Mraka <michael.mraka@redhat.com> 2.0.7-24
- provide cobbler2 to satisfy deps in spacewalk 1.8+ packages

* Tue Nov 20 2012 Tomas Lestach <tlestach@redhat.com> 2.0.7-23
- fix patch to match --fuzz=0 option on rhel6

* Tue Nov 20 2012 Tomas Lestach <tlestach@redhat.com> 2.0.7-22
- 866326 - catch cheetah exception in mod_pythod/mod_wsgi and forward it as 500
  SERVER ERROR

* Thu Sep 06 2012 Milan Zazrivec <mzazrivec@redhat.com> 2.0.7-21
- 784049 - support XZ packes ramdisk: correct bash syntax

* Fri Aug 24 2012 Stephen Herr <sherr@redhat.com> 2.0.7-20
- 589318 - make sure modprobe.conf exists if we need to create a bond
- updating tito configs to move from Satellite-5.x* to Satellite-5.5* branches

* Tue Jul 03 2012 Stephen Herr <sherr@redhat.com> 2.0.7-19
- 836545 - have to convert from unicode to string on RHEL 6

* Fri Jun 29 2012 Stephen Herr <sherr@redhat.com> 2.0.7-18
- 830662 - fixing power vulnerability patch so that templated commands will run
  properly
- 830662 - fixing 'no power type set for system' errors

* Thu Jun 21 2012 Milan Zazrivec <mzazrivec@redhat.com> 2.0.7-17
- 784049 - correct support for xz packed ramdisk

* Mon Jun 11 2012 Jan Pazdziora 2.0.7-16
- CVE-2012-2395 - power vulnerability patch. (sherr@redhat.com)
- update build settings for cobbler (mzazrivec@redhat.com)

* Wed Mar 14 2012 Milan Zazrivec <mzazrivec@redhat.com> 2.0.7-15
- 789037 - handle nic with a dash correctly (mzazrivec@redhat.com)
- 784049 - support for XZ packed ramdisk (mzazrivec@redhat.com)
- 784912 - post_install_network snippet: IPv6 support (mzazrivec@redhat.com)
- 717884 - make cobblerd work in IPv6 environment (mzazrivec@redhat.com)

* Thu Dec 08 2011 Tomas Lestach <tlestach@redhat.com> 2.0.7-14
- 723060 - fix token validation (tlestach@redhat.com)

* Fri Sep 23 2011 Miroslav Suchý 2.0.7-13
- 253274 - if resolving to ip address fail, use hostname

* Wed Aug 24 2011 Milan Zazrivec <mzazrivec@redhat.com> 2.0.7-12
- 728268 - update allowed kernel command line parameter length
- 708347 - fix koan error when provisioning VM to use a logical volume
- 717344 - fix problem with CIDR network notation in RHEL-6
- 723898 - fix keep_ssh_host_keys snippet

* Fri May 27 2011 Jan Pazdziora 2.0.7-11
- 707215 - cobbler should not remove pub during sync as the cobbler rpm owns
  that directory.

* Wed May 25 2011 Jan Pazdziora 2.0.7-10
- 568801 - hardlinks ruin SELinux contexts because multiple paths match, avoid
  hardlinks.

* Wed May 25 2011 Jan Pazdziora 2.0.7-9
- 706857 - disable the SELinux part of cobbler check.

* Thu Mar 31 2011 Milan Zazrivec <mzazrivec@redhat.com> 2.0.7-8
- 673388 - embed kickstart file into ramdisk for RHEL-6 and static networking

* Mon Mar 28 2011 Tomas Lestach <tlestach@redhat.com> 2.0.7-7
- remove fence-agents Require from cobbler (tlestach@redhat.com)
- We need to be building cobbler / koan for RHEL-4 as well
  (mzazrivec@redhat.com)

* Mon Jan 10 2011 Milan Zazrivec <mzazrivec@redhat.com> 2.0.7-6
- 660673 - RHEL-6: replace rhpl with ethtool
- 610174 - use tap driver for Xen PV disks

* Thu Dec 02 2010 Jan Pazdziora 2.0.7-5
- 580072 - avoid copying pxelinux.0 on arches where it is not present (s390x).

* Tue Oct 26 2010 Justin Sherrill <jsherril@redhat.com> 2.0.7-4
- fixing previous dep for koan to not appear within an if statement
  (jsherril@redhat.com)

* Mon Oct 25 2010 Justin Sherrill <jsherril@redhat.com> 2.0.7-3
- adding missing python-urlgrabber dep for koan (jsherril@redhat.com)

* Mon Oct 18 2010 Shannon Hughes <shughes@redhat.com> 2.0.7-2
- combine patches into new version build (shughes@redhat.com)
- build.py.props for cobbler (mzazrivec@redhat.com)

* Mon Oct 18 2010 Scott Henson <shenson@redhat.com> - 2.0.7-1
- Bug fix relase, see Changelog for details

* Tue Jul 13 2010 Scott Henson <shenson@redhat.com> - 2.0.5-1
- Bug fix release, see Changelog for details

* Tue Apr 27 2010 Scott Henson <shenson@redhat.com> - 2.0.4-1
- Bug fix release, see Changelog for details

* Mon Mar  1 2010 Scott Henson <shenson@redhat.com> - 2.0.3.1-3
- Bump release because I forgot cobbler-web

* Mon Mar  1 2010 Scott Henson <shenson@redhat.com> - 2.0.3.1-2
- Remove requires on mkinitrd as it is not used

* Mon Feb 15 2010 Scott Henson <shenson@redhat.com> - 2.0.3.1-1
- Upstream Brown Paper Bag Release (see CHANGELOG)

* Thu Feb 11 2010 Scott Henson <shenson@redhat.com> - 2.0.3-1
- Upstream changes (see CHANGELOG)

* Mon Nov 23 2009 John Eckersberg <jeckersb@redhat.com> - 2.0.2-1
- Upstream changes (see CHANGELOG)

* Tue Sep 15 2009 Michael DeHaan <mdehaan@redhat.com> - 2.0.0-1
- First release with unified spec files

