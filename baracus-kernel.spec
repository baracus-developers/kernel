# norootforbuild
%define sname baracus

Summary:   Files needed to perform independent baracus tasks
Name:      %{sname}-kernel
Version:   1.6.4
Release:   0
Group:     System/Services
License:   GPLv2 or Artistic V2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch
Source6:   initrd.%{sname}
Source7:   linux.%{sname}

%description
The necessary kernel and initrd for baracus to perform some independent
functions including hardware inventory and disk wipe.

%prep

%build

%install
mkdir -p %{buildroot}

install -D -m644 %{S:6} %{buildroot}%{_datadir}/%{sname}/data/initrd.%{sname}
install -D -m644 %{S:7} %{buildroot}%{_datadir}/%{sname}/data/linux.%{sname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/%{sname}*

%changelog
