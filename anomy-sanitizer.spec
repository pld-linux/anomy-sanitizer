Summary:	Anomy Sanitizer
Name:		anomy-sanitizer
Version:	1.76
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://mailtools.anomy.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	1f53b7da3cc4f3d78631546335ff9dcd
URL:		http://mailtools.anomy.net/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Anomy sanitizer is what most people would call "an email virus
scanner". That description is not totally accurate, but it does cover
one of the more important jobs that the sanitizer can do for you - it
can scan email attachments for viruses.

Other things it can do:
- Disable potentially dangerous HTML code, such as javascript, within
  incoming email.
- Protect you from email-based break-in attempts which exploit bugs in
  common email programs (Outlook, Eudora, Pine, ...).
- Block or "mangle" attachments based on their file names. This way if
  you don't need to recieve e.g. visual basic scripts, then you don't
  have to worry about the security risk they imply (the ILOVEYOU virus
  was a visual basic program). This lets you protect yourself and your
  users from whole classes of attacks, without relying on complex,
  resource intensive and outdated virus scanning solutions.

%prep
%setup -qc
mv anomy/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}}
cp -a bin/Anomy $RPM_BUILD_ROOT%{perl_vendorlib}/Anomy

for a in bin/*.pl; do
	f=${a#*/}
	f=anomy-${f%.pl}
	install -p $a $RPM_BUILD_ROOT%{_bindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.sanitizer CREDITS README.sanitizer sanitizer.html UNICODE.TXT
%doc contrib
%attr(755,root,root) %{_bindir}/anomy-mailblogger
%attr(755,root,root) %{_bindir}/anomy-sanitizer
%attr(755,root,root) %{_bindir}/anomy-simplify
%{perl_vendorlib}/Anomy
