#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-plucky
Version  : 0.6.6
Release  : 3
URL      : https://rubygems.org/downloads/plucky-0.6.6.gem
Source0  : https://rubygems.org/downloads/plucky-0.6.6.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-core

%description
# Plucky
Thin layer over the ruby driver that allows you to quickly grab hold of your data (pluck it!).

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n plucky-0.6.6
gem spec %{SOURCE0} -l --ruby > rubygem-plucky.gemspec

%build
gem build rubygem-plucky.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
plucky-0.6.6.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/plucky-0.6.6.gem
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/README.md
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/UPGRADES
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/examples/query.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/criteria_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/extensions/duplicable.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/extensions/symbol.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/new_relic.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/normalizers/criteria_hash_key.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/normalizers/criteria_hash_value.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/normalizers/fields_value.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/normalizers/hash_key.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/normalizers/integer.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/normalizers/options_hash_value.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/normalizers/sort_value.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/options_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/pagination.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/pagination/collection.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/pagination/paginator.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/query.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/lib/plucky/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/plucky.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/script/bootstrap
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/script/criteria_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/script/release
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/script/test
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/functional/options_hash_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/criteria_hash_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/normalizers/criteria_hash_key_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/normalizers/criteria_hash_value_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/normalizers/fields_value_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/normalizers/hash_key_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/normalizers/integer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/normalizers/options_hash_value_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/normalizers/sort_value_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/options_hash_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/pagination/collection_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/pagination/paginator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky/query_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/plucky_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/symbol_operator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/spec/symbol_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/plucky-0.6.6/specs.watchr
/usr/lib64/ruby/gems/2.3.0/specifications/plucky-0.6.6.gemspec
