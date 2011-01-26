Summary:	Anomy Sanitizer
Name:		anomy-sanitizer
Version:	1.54
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://mailtools.anomy.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	977b20b2ecf47622b05f1933fad18a41
URL:		http://mailtools.anomy.net/
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
%setup -q -n anomy

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}
cp -a bin/Anomy $RPM_BUILD_ROOT%{perl_vendorlib}/Anomy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.sanitizer CREDITS README.sanitizer sanitizer.html
%{perl_vendorlib}/Anomy
