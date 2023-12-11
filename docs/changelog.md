---
title: Changelog
---

# 1.7.0

## Minor Changes

- Replace recommendation of using system packages with pip3
  ([#129](https://github.com/pycontribs/ansi2html/pull/129))
  @ssbarnea
- Add truecolor support
  ([#155](https://github.com/pycontribs/ansi2html/pull/155))
  @miltolstoy
- Generate documentation with Sphinx and use Read the Docs
  ([#141](https://github.com/pycontribs/ansi2html/pull/141))
  @tristanlatr
- Adds support for OSC hyperlink sequences.
  ([#131](https://github.com/pycontribs/ansi2html/pull/131))
  @hakonhagland

## Bugfixes

- Add test coverage
  ([#148](https://github.com/pycontribs/ansi2html/pull/148))
  @ziegenberg
- Replace pkg_resources with importlib.metadata
  ([#144](https://github.com/pycontribs/ansi2html/pull/144))
  @ziegenberg
- fix including of CHANGELOG.rst
  ([#151](https://github.com/pycontribs/ansi2html/pull/151))
  @ziegenberg
- Update linting dependencies
  ([#147](https://github.com/pycontribs/ansi2html/pull/147))
  @ziegenberg
- Upgrade the build process
  ([#145](https://github.com/pycontribs/ansi2html/pull/145))
  @ziegenberg
- Add type hinting
  ([#143](https://github.com/pycontribs/ansi2html/pull/143))
  @ziegenberg
- Update CI badges in readme
  ([#142](https://github.com/pycontribs/ansi2html/pull/142))
  @ssbarnea
- Bump setuptools-scm version
  ([#138](https://github.com/pycontribs/ansi2html/pull/138))
  @ssbarnea

Kudos goes to: @hakonhagland, @miltolstoy, @pre-commit-ci,
@pre-commit-ci\[bot\], @ssbarnea, @tristanlatr and @ziegenberg

# 1.6.0

## Changes

- Switching from nosetest to unittest
  ([#103](https://github.com/pycontribs/ansi2html/pull/103))
  @paolostivanin
- Add dracula colorscheme
  ([#106](https://github.com/pycontribs/ansi2html/pull/106))
  @ahmubashshir
- Refactor packaging by replacing old setup.py based packaging with
  modern pep517 based one
  ([#112](https://github.com/pycontribs/ansi2html/pull/112))
  @ssbarnea
- Replace travis with github actions
  ([#121](https://github.com/pycontribs/ansi2html/pull/121))
  @ssbarnea

## Bugfixes

- Correct author metadata
  ([#122](https://github.com/pycontribs/ansi2html/pull/122))
  @ssbarnea

## Deprecations

- Officially retire support for Python \<=3.5
  ([#112](https://github.com/pycontribs/ansi2html/pull/112))
  @ssbarnea

# 1.5.2

## Commits {#commits_1_5_2}

- Update pypi python versions.
  [5688d50ae](https://github.com/pycontribs/ansi2html/commit/5688d50ae)

# 1.5.1

Include manpage in release.

# 1.5.0

## Pull Requests {#pr_1_5_0}

- add support for vt100 box drawing mode and high-intensity ansi codes
  ([#90](https://github.com/pycontribs/ansi2html/pull/90))
  @p-sherratt

## Commits {#commits_1_5_0}

- add support for vt100 box drawing mode and high-intensity ansi codes
  [bf327d216](https://github.com/pycontribs/ansi2html/commit/bf327d216)
- make \'intense\' colors more \'intense\'
  [d9bf45f81](https://github.com/pycontribs/ansi2html/commit/d9bf45f81)
- restore css ordering for unit tests
  [3bf89663a](https://github.com/pycontribs/ansi2html/commit/3bf89663a)
- trivial fix/update
  [289d01595](https://github.com/pycontribs/ansi2html/commit/289d01595)
- update test_produce_headers unit test
  [0ea0a71f7](https://github.com/pycontribs/ansi2html/commit/0ea0a71f7)
- another fix/update for box drawing & high-intensity patch
  [ed942a5d2](https://github.com/pycontribs/ansi2html/commit/ed942a5d2)

# 1.4.2

## Commits {#commits_1_4_2}

- py36
  [efb491f09](https://github.com/pycontribs/ansi2html/commit/efb491f09)
- Restore CSS styles for background colors.
  [947f813a3](https://github.com/pycontribs/ansi2html/commit/947f813a3)

# 1.4.1

## Pull Requests {#pr_1_4_1}

- Fix undefined behavior with linkify when same url is repeated in
  same line ([#85](https://github.com/pycontribs/ansi2html/pull/85))
  @qsujanadiga-practo

## Commits {#commits_1_4_1}

- Update converter.py
  [9adc3ddef](https://github.com/pycontribs/ansi2html/commit/9adc3ddef)
- Fix linkify with latex
  [11cb73657](https://github.com/pycontribs/ansi2html/commit/11cb73657)
- Update url regex
  [190835f4f](https://github.com/pycontribs/ansi2html/commit/190835f4f)

# 1.4.0

## Pull Requests {#pr_1_4_0}

- Prune CSS classes from output that are not used
  ([#84](https://github.com/pycontribs/ansi2html/pull/84)) @cfstras

## Commits {#commits_1_4_0}

- Prune CSS classes from output that are not used
  [61f4b5368](https://github.com/pycontribs/ansi2html/commit/61f4b5368)
- fix tests: remove unused CSS
  [753220215](https://github.com/pycontribs/ansi2html/commit/753220215)

# 1.3.0

**Relicensed to LGPLv3+**.

## Pull Requests {#pr_1_3_0}

- Relicensed to LGPLv3+
  ([#80](https://github.com/pycontribs/ansi2html/pull/80)) @ralphbean

## Commits {#commits_1_3_0}

- Relicensed to LGPLv3+
  [f74316174](https://github.com/pycontribs/ansi2html/commit/f74316174)

# 1.2.0

## Pull Requests {#pr_1_2_0}

- enable python 3 input decoding
  ([#64](https://github.com/pycontribs/ansi2html/pull/64)) @kaspar030
- Fix handling cursor move up with unique and empty lines
  ([#67](https://github.com/pycontribs/ansi2html/pull/67)) @gberaudo
- Give more useful TaskWarrior example
  ([#68](https://github.com/pycontribs/ansi2html/pull/68))
  @AloisMahdal
- Update style.py
  ([#69](https://github.com/pycontribs/ansi2html/pull/69)) @karjaneth
- Revert \"six is called six, not python-six\"
  ([#73](https://github.com/pycontribs/ansi2html/pull/73))
  @JensTimmerman

## Commits {#commits_1_2_0}

- enable python 3 input decoding
  [d6e4bc0aa](https://github.com/pycontribs/ansi2html/commit/d6e4bc0aa)
- Fix handling cursor move up with unique and empty lines
  [1e6a3b81f](https://github.com/pycontribs/ansi2html/commit/1e6a3b81f)
- Give more useful TaskWarrior example
  [46e480143](https://github.com/pycontribs/ansi2html/commit/46e480143)
- Update style.py
  [0c975b60b](https://github.com/pycontribs/ansi2html/commit/0c975b60b)
- Revert \"six is called six, not python-six\"
  [168805a00](https://github.com/pycontribs/ansi2html/commit/168805a00)
- Tox for tests.
  [90c8c2303](https://github.com/pycontribs/ansi2html/commit/90c8c2303)
- Merge branch \'develop\' of github.com:ralphbean/ansi2html into
  develop
  [1366309e1](https://github.com/pycontribs/ansi2html/commit/1366309e1)

# 1.1.1

## Pull Requests {#pr_1_1_1}

- six is called six, not python-six
  ([#61](https://github.com/pycontribs/ansi2html/pull/61))
  @JensTimmerman

## Commits {#commits_1_1_1}

- Drop 2.6
  [81bb739b1](https://github.com/pycontribs/ansi2html/commit/81bb739b1)
- six is called six, not python-six
  [cec1dd933](https://github.com/pycontribs/ansi2html/commit/cec1dd933)
- Exclude .pyc files from the release tarball.
  [0dfd66b0b](https://github.com/pycontribs/ansi2html/commit/0dfd66b0b)
- Remove CHANGELOG header.
  [7b8643066](https://github.com/pycontribs/ansi2html/commit/7b8643066)

# 1.1.0

- 1.0.4
  [96b6f19ae](https://github.com/pycontribs/ansi2html/commit/96b6f19ae99a239051cd52c8edd7980d791736e9)
- 1.0.4
  [b7e6e048c](https://github.com/pycontribs/ansi2html/commit/b7e6e048cc78324849c2af93d4948f6bc696ff09)
- 1.0.5
  [f9cab7af7](https://github.com/pycontribs/ansi2html/commit/f9cab7af7483969d73e3696e988945cc797e5149)
- 1.0.9
  [1594cddb7](https://github.com/pycontribs/ansi2html/commit/1594cddb714890ee7878150da679c89373f8846b)

# 1.0.8

- added setup.cfg file
  [547bd1cb5](https://github.com/pycontribs/ansi2html/commit/547bd1cb5e5e65ab674d3cd489af872213f60051)
- Merge branch \'develop\' of github.com:ralphbean/ansi2html into
  develop
  [352d14be6](https://github.com/pycontribs/ansi2html/commit/352d14be694c0bfb10119c00639f319697587c26)
- changed setup.cfg to work on python 2.6.6
  [7a12a92ed](https://github.com/pycontribs/ansi2html/commit/7a12a92edf1747e64b28cb41c7e0f11787d7774e)
- actually, python 2.6.6 on RH, centos etc has OrderedDict
  [512377d63](https://github.com/pycontribs/ansi2html/commit/512377d63f7ecfb583530121330d9a0552a24e78)
- Merge pull request #55 from JensTimmerman/develop
  [03c3e680c](https://github.com/pycontribs/ansi2html/commit/03c3e680c90ca77c24ee465213a88f3726caf5bf)
- Prevent IndexError while handling CursorMoveUp
  [7a91200df](https://github.com/pycontribs/ansi2html/commit/7a91200df0d6f088b0ba947420d8829bf04caecd)
- Merge pull request #56 from lqez/fix/over-cursormoveup
  [a23772b57](https://github.com/pycontribs/ansi2html/commit/a23772b57d584676792cbcdb74266c361a831f61)
- style: Include all 16 solarized colors in the scheme
  [081c9a741](https://github.com/pycontribs/ansi2html/commit/081c9a741d1b0f09d8ab9c66dc9647bb882142c2)
- style: Encode pallete in 256 color encoding
  [acaa92ff2](https://github.com/pycontribs/ansi2html/commit/acaa92ff2370d7ebda85ee68a47bfdb7d309a811)
- Merge pull request #57 from tbabej/develop
  [e1bd92d3e](https://github.com/pycontribs/ansi2html/commit/e1bd92d3e735d5143a81836ca6eb5e6d597bd987)
- Update travis config.
  [74c4f1dc8](https://github.com/pycontribs/ansi2html/commit/74c4f1dc8b6c3ca41dd9dee284922c88f5934d10)
- Fix existing test suite.
  [eb7798cb7](https://github.com/pycontribs/ansi2html/commit/eb7798cb7704465f242e97149d7483074f4d6226)
- Fill out color palettes that were under-specified.
  [5e55018eb](https://github.com/pycontribs/ansi2html/commit/5e55018eb331e2d934215821e874e30eab20e6ef)
- Merge branch \'feature/fixes\' into develop
  [100be7c2d](https://github.com/pycontribs/ansi2html/commit/100be7c2d83d40d10b161d3def9b8e2b56e49b32)
- Fix line height stuff.
  [db1ee5b47](https://github.com/pycontribs/ansi2html/commit/db1ee5b47c0495ebb6bffb39c17891fe25dcd8d7)
- Fix tests for the new palette values.
  [e8c6b9362](https://github.com/pycontribs/ansi2html/commit/e8c6b9362287033c6d9296d61f8940aaae8703a4)

# 1.0.7

- Implemented LaTeX support. Only colors are supported but it does
  already what I need.
  [caa8c6fe5](https://github.com/pycontribs/ansi2html/commit/caa8c6fe5010c3d912aac47ce1e6e3aeaddfaa17)
- Updated README.rst.
  [4979c1409](https://github.com/pycontribs/ansi2html/commit/4979c14091e43ee1090dc2399e04f57e8d60db95)
- Added first test for LaTeX output.
  [4b80d41e0](https://github.com/pycontribs/ansi2html/commit/4b80d41e0bd1f7bc4dd73df82cc67acb6917d4e9)
- Added title and linkify for LaTeX.
  [3a869bce1](https://github.com/pycontribs/ansi2html/commit/3a869bce19a6ad0c219d1c5f524e9c7b9784f978)
- Trying to fix
  <https://travis-ci.org/ralphbean/ansi2html/jobs/25808505>.
  [a0a06b41c](https://github.com/pycontribs/ansi2html/commit/a0a06b41cc7fe10e5241954fc03438c41a16a338)
- Fixed unicode escape problem. Fixes
  <https://travis-ci.org/ralphbean/ansi2html/builds/26243970>.
  [095eca5a5](https://github.com/pycontribs/ansi2html/commit/095eca5a5731ce45a1a4cbf77e3cdfdf2e6716cb)
- Sure % has a special meaning ...
  [2324a3dcf](https://github.com/pycontribs/ansi2html/commit/2324a3dcfe5b9896d0e93aec4b9de4202894eb73)
- Merge pull request #48 from ypid/ansi2latex
  [91e174cfd](https://github.com/pycontribs/ansi2html/commit/91e174cfd207c2fa273153ba11275459c3a5a1a2)
- set pre\'s id to \"content\"
  [6f14bc202](https://github.com/pycontribs/ansi2html/commit/6f14bc202afa20379cdc3b5c15819119ea8b524f)
- the css
  [418bef2f0](https://github.com/pycontribs/ansi2html/commit/418bef2f03dd36e7ad0dac663db0e917879d3dee)
- Merge pull request #50 from szepeviktor/patch-2
  [97977e53b](https://github.com/pycontribs/ansi2html/commit/97977e53b4c85738be603c7f236958f95aacf1f9)
- Merge pull request #52 from szepeviktor/patch-3
  [620fc1032](https://github.com/pycontribs/ansi2html/commit/620fc1032af177406b17facfa20093b85772a2c5)
- Use the data_files that we build above.
  [654bc30b4](https://github.com/pycontribs/ansi2html/commit/654bc30b40d89acdec91a194ff8651a6db86f812)

# 1.0.6

- 1.0.5
  [f9cab7af7](https://github.com/pycontribs/ansi2html/commit/f9cab7af7483969d73e3696e988945cc797e5149)
- use optparse choices to deal with invalid scheme selection.
  [214d73609](https://github.com/pycontribs/ansi2html/commit/214d73609ff0e0dd645778dbbc0392cd340f8df5)
- added solarized and os X terminal color schemes
  [2176bc4d0](https://github.com/pycontribs/ansi2html/commit/2176bc4d050f52b69dd9227e29508a9dfd2e1b0a)
- Merge pull request #41 from schettino72/more-schemes
  [609326371](https://github.com/pycontribs/ansi2html/commit/609326371e74c8f19c4185f76a64e24f54d6cfbf)
- Revert \"Conditionally install man page into system or virtualenv.
  For #39.\"
  [c1ee2bac9](https://github.com/pycontribs/ansi2html/commit/c1ee2bac9bf66944cce387a4f1a534a408966d6a)
- Install man page to \${PREFIX}, not /usr (issue #39)
  [86abc9e3d](https://github.com/pycontribs/ansi2html/commit/86abc9e3dd8769af848a93ac2afc3728688554b3)
- Merge pull request #42 from hartwork/issue-39
  [e81c55b38](https://github.com/pycontribs/ansi2html/commit/e81c55b38b3368ceb05842823f980320607ed6db)
- add empty title element to head section in html output
  [c16fe680b](https://github.com/pycontribs/ansi2html/commit/c16fe680b18fa5c880ae8ed71fab3b062c2a371a)
- Merge pull request #43 from CBke/develop
  [c13f4a985](https://github.com/pycontribs/ansi2html/commit/c13f4a9852785fc4c68d416747923b2f6653faca)
- 1.0.4
  [40526f43a](https://github.com/pycontribs/ansi2html/commit/40526f43a009c85fddc0ab34de51e9eb94883e1c)
- 1.0.5
  [e6a150e9d](https://github.com/pycontribs/ansi2html/commit/e6a150e9dd00f607ad32377878e36e2783cba784)
- Fix tests for added title.
  [aab8348ce](https://github.com/pycontribs/ansi2html/commit/aab8348ced14e747178772b49e0a796effeec974)
- add option \--title for filling in the title
  [007e77c50](https://github.com/pycontribs/ansi2html/commit/007e77c507cd9bc8465caa46fc47abbd66d5c313)
- Merge pull request #44 from CBke/develop
  [4fd918e54](https://github.com/pycontribs/ansi2html/commit/4fd918e54e62d2658f3fdedc5347070de96ddcff)
- Drop manpage installation stuff.
  [a2f157614](https://github.com/pycontribs/ansi2html/commit/a2f157614243e70d0134818ef1c37b1b780339d5)

# 1.0.5

- added support to select a color-scheme. added schemes \'xterm\' and
  \'xterm-bright\'
  [367289a86](https://github.com/pycontribs/ansi2html/commit/367289a86bb81f0c22801b6db7b63cc8acdec300)
- Merge pull request #40 from schettino72/color-schemes
  [1111aec78](https://github.com/pycontribs/ansi2html/commit/1111aec7863584c1153438e89833f53be29fa249)
- 1.0.4
  [96b6f19ae](https://github.com/pycontribs/ansi2html/commit/96b6f19ae99a239051cd52c8edd7980d791736e9)
- 1.0.4
  [b7e6e048c](https://github.com/pycontribs/ansi2html/commit/b7e6e048cc78324849c2af93d4948f6bc696ff09)

# 1.0.4

# 1.0.3

- Makefile: Fix regression where version bumps would not force a
  rebuild of the man page
  [750fe09fe](https://github.com/pycontribs/ansi2html/commit/750fe09feccf600ee19d5842649a9b9cd6965510)
- Makefile: Mark target upload as phony
  [ac3877f57](https://github.com/pycontribs/ansi2html/commit/ac3877f5728281ed2df792767ad18e6283001615)
- Merge pull request #38 from hartwork/dependency-regression
  [10b6051a4](https://github.com/pycontribs/ansi2html/commit/10b6051a4bd207064a77b5f28be7e6954c028d8b)
- Conditionally install man page into system or virtualenv. For #39.
  [720ac2f93](https://github.com/pycontribs/ansi2html/commit/720ac2f93e6dfb1c77520dc5f7aeab4f031dfd75)

# 1.0.2

- Add an upload command to the Makefile.
  [12e68427c](https://github.com/pycontribs/ansi2html/commit/12e68427c8dc4255bb4da8ccd8024c2b742be8e8)
- Tweak travis setup.
  [07a95ef6e](https://github.com/pycontribs/ansi2html/commit/07a95ef6e5d0c6afc5ee53fa5ce6f9c5bc3a2bab)
- Remove a forgotten import.
  [756139724](https://github.com/pycontribs/ansi2html/commit/75613972499b6ee18326bdd2989e5411ad475ce9)

# 1.0.1

- Change the way we store version info.
  [4e4eaef33](https://github.com/pycontribs/ansi2html/commit/4e4eaef33d27aea931b57c3eee61ec16cc47cf87)

# 1.0.0

- Add trove for py3.3.
  [683f672fa](https://github.com/pycontribs/ansi2html/commit/683f672fa6071cc7390b6c64858127fe0b1e2e77)
- Stop adding unwanted spaces (issue 26)
  [b5163a80f](https://github.com/pycontribs/ansi2html/commit/b5163a80feea7f6ba8879357524ccbe143e68281)
- Add test for issue 25
  [6df79eb8b](https://github.com/pycontribs/ansi2html/commit/6df79eb8b95b2c36e7395bedcd13e0facb323434)
- Fix destructive reset marker handling (issue 25)
  [4db97b126](https://github.com/pycontribs/ansi2html/commit/4db97b126c600d30a922ab5899faa8879f699739)
- Fix ANSI code decoding (issue 25)
  [f277f8f3c](https://github.com/pycontribs/ansi2html/commit/f277f8f3c4eaa1256c5df66238583b5a69882456)
- Fix writing to sys.stdout.buffer
  [7a3267d53](https://github.com/pycontribs/ansi2html/commit/7a3267d53a2ea61a0af6021faedf154ba89b2f87)
- Add convenience Makefile
  [8d3f3e055](https://github.com/pycontribs/ansi2html/commit/8d3f3e055e679bf723d6a846fbff2c95a7224b9a)
- Merge pull request #30 from hartwork/makefile
  [156bc89da](https://github.com/pycontribs/ansi2html/commit/156bc89da97c7de19b2beb8e2de7bde2f2535a20)
- Merge pull request #29 from hartwork/issue_29
  [8495723ae](https://github.com/pycontribs/ansi2html/commit/8495723ae8e057248537a53f9e7e800547d6640e)
- Merge pull request #27 from hartwork/issue_26
  [74d237c18](https://github.com/pycontribs/ansi2html/commit/74d237c18165625bedde85e25f1eb988f0da8ca1)
- Merge pull request #28 from hartwork/issue_25
  [8c77f6d93](https://github.com/pycontribs/ansi2html/commit/8c77f6d93754c03fc256754de73b8b2bf1d6c08c)
- Fix italic to be font-style (rather than font-weight)
  [47b533b6d](https://github.com/pycontribs/ansi2html/commit/47b533b6de62ebe97d32322eaa3a5dcec735a077)
- Add inv\* CSS classes
  [408808197](https://github.com/pycontribs/ansi2html/commit/408808197e9b33aa55210b5f03940267b3e01c83)
- Handle state in code, not in HTML; support more ANSI codes
  [fce66a6a9](https://github.com/pycontribs/ansi2html/commit/fce66a6a905fb6aa006cfa1f6ad4716ebb46e63b)
- Adapt tests to new approach to state
  [49046c620](https://github.com/pycontribs/ansi2html/commit/49046c620079d3a325753081ba99b1deb0c8287a)
- Add CSS classes for lighter font style (2), blinking (5/6), hidden
  text (8)
  [e488daca3](https://github.com/pycontribs/ansi2html/commit/e488daca38176c9cdba7318a958fc79bfb16f9cb)
- Save producing no-op span tags
  [340620f88](https://github.com/pycontribs/ansi2html/commit/340620f88b66a686c16f155465f172321fe39cff)
- Test ANSI codes that just turned supported
  [f4774bcf0](https://github.com/pycontribs/ansi2html/commit/f4774bcf0005175bc00f282f73365fa59b6f47fb)
- Make code testing pairs of files re-usable
  [f95ca305d](https://github.com/pycontribs/ansi2html/commit/f95ca305dba5951c25178fc12fb0e206120aa1b4)
- Add testcase for output from \"eix -I svn -F\"
  [e3f593671](https://github.com/pycontribs/ansi2html/commit/e3f59367174fb9ed4df2d19ed012bae45f0ce2ce)
- Merge pull request #31 from hartwork/font-style-italic
  [a25950fe6](https://github.com/pycontribs/ansi2html/commit/a25950fe6f0bdd12c92cbbd2109655bfd1cc5a36)
- Tweak for py3 support.
  [9766508e1](https://github.com/pycontribs/ansi2html/commit/9766508e16007fdcd764ba52c79af798d8d816fd)
- Add py3.3 to travis config.
  [ceef1eb8e](https://github.com/pycontribs/ansi2html/commit/ceef1eb8e83a58fe895f67185f4242b8e49f7b7c)
- Merge branch \'stateful\' into develop
  [29868b6ec](https://github.com/pycontribs/ansi2html/commit/29868b6ec1e742a23e3b60db17f187ce75bb3d57)
- 0.10.0
  [b5c65d3a4](https://github.com/pycontribs/ansi2html/commit/b5c65d3a4fa666aa397409900677c9c115625be7)
- Add missing license headers
  [44e5e52fa](https://github.com/pycontribs/ansi2html/commit/44e5e52faf6ea1eef57b8a3b1173f6794683dd4d)
- Fix README example to not produce unwanted spaces (issue 26)
  [cc6a0dbfa](https://github.com/pycontribs/ansi2html/commit/cc6a0dbfa2a86a827f8f737b0b610cbcb9afe282)
- Add \--version parameter, control version in version.py
  [0b2006095](https://github.com/pycontribs/ansi2html/commit/0b2006095e4b56896773fdaa4fb6b5526ecbde58)
- Improve \--help output
  [26d297807](https://github.com/pycontribs/ansi2html/commit/26d2978072f2f13836219d4999ff6b7d12ed031a)
- Add and integrate man page
  [2ec363007](https://github.com/pycontribs/ansi2html/commit/2ec363007f49b91275d146414313783ba4d5ab61)
- No longer process line-by-line (fixes \--partial and \--inline,
  issue 36)
  [e3e86f9f8](https://github.com/pycontribs/ansi2html/commit/e3e86f9f874a4243ee66a88022e752c7ceaf338e)
- Test cross-line state (related to issue 36)
  [c3eb8b9c5](https://github.com/pycontribs/ansi2html/commit/c3eb8b9c51828da2e94aff9f5f77a363bc841850)
- Fix approach to trailing newlines
  [95e75e4d3](https://github.com/pycontribs/ansi2html/commit/95e75e4d3e844aa33fb89045953c5d4869b3dbd2)
- Merge pull request #37 from hartwork/fix-line-handling
  [0fb5443ca](https://github.com/pycontribs/ansi2html/commit/0fb5443ca094bed79a4e30964716b2c3f875cb96)
- Merge pull request #33 from hartwork/headers
  [12bfa3251](https://github.com/pycontribs/ansi2html/commit/12bfa325141f7c7f7d7a9f65147d30a3082fc53b)
- Merge pull request #34 from hartwork/fix-readme-example
  [b1ed96e00](https://github.com/pycontribs/ansi2html/commit/b1ed96e00d324f0a4557917c02f425266dd224c1)
- Merge pull request #35 from hartwork/manpage
  [ad608eb2b](https://github.com/pycontribs/ansi2html/commit/ad608eb2b26751e983ac9e31ae412698f45d4664)

# 0.9.4

- Fix encoding issue.
  [64881f549](https://github.com/pycontribs/ansi2html/commit/64881f549126f5c576df7b75e70e49633fe59337)
- Silence silly py2.7 test errors.
  [b5db644ff](https://github.com/pycontribs/ansi2html/commit/b5db644ffa29497bd16dc0f0adae7f0847603f2c)

# 0.9.3

- Fix encoding issue.
  [64881f549](https://github.com/pycontribs/ansi2html/commit/64881f549126f5c576df7b75e70e49633fe59337)
- Silence silly py2.7 test errors.
  [b5db644ff](https://github.com/pycontribs/ansi2html/commit/b5db644ffa29497bd16dc0f0adae7f0847603f2c)
- Fix little encoding issue.
  [8cfbe166c](https://github.com/pycontribs/ansi2html/commit/8cfbe166c5645e459ad0ff3c061634a2146c26b9)
- Add trove for py3.3.
  [683f672fa](https://github.com/pycontribs/ansi2html/commit/683f672fa6071cc7390b6c64858127fe0b1e2e77)
- Stop adding unwanted spaces (issue 26)
  [b5163a80f](https://github.com/pycontribs/ansi2html/commit/b5163a80feea7f6ba8879357524ccbe143e68281)
- Add test for issue 25
  [6df79eb8b](https://github.com/pycontribs/ansi2html/commit/6df79eb8b95b2c36e7395bedcd13e0facb323434)
- Fix destructive reset marker handling (issue 25)
  [4db97b126](https://github.com/pycontribs/ansi2html/commit/4db97b126c600d30a922ab5899faa8879f699739)
- Fix ANSI code decoding (issue 25)
  [f277f8f3c](https://github.com/pycontribs/ansi2html/commit/f277f8f3c4eaa1256c5df66238583b5a69882456)
- Fix writing to sys.stdout.buffer
  [7a3267d53](https://github.com/pycontribs/ansi2html/commit/7a3267d53a2ea61a0af6021faedf154ba89b2f87)
- Add convenience Makefile
  [8d3f3e055](https://github.com/pycontribs/ansi2html/commit/8d3f3e055e679bf723d6a846fbff2c95a7224b9a)
- Merge pull request #30 from hartwork/makefile
  [156bc89da](https://github.com/pycontribs/ansi2html/commit/156bc89da97c7de19b2beb8e2de7bde2f2535a20)
- Merge pull request #29 from hartwork/issue_29
  [8495723ae](https://github.com/pycontribs/ansi2html/commit/8495723ae8e057248537a53f9e7e800547d6640e)
- Merge pull request #27 from hartwork/issue_26
  [74d237c18](https://github.com/pycontribs/ansi2html/commit/74d237c18165625bedde85e25f1eb988f0da8ca1)
- Merge pull request #28 from hartwork/issue_25
  [8c77f6d93](https://github.com/pycontribs/ansi2html/commit/8c77f6d93754c03fc256754de73b8b2bf1d6c08c)
- Fix italic to be font-style (rather than font-weight)
  [47b533b6d](https://github.com/pycontribs/ansi2html/commit/47b533b6de62ebe97d32322eaa3a5dcec735a077)
- Add inv\* CSS classes
  [408808197](https://github.com/pycontribs/ansi2html/commit/408808197e9b33aa55210b5f03940267b3e01c83)
- Handle state in code, not in HTML; support more ANSI codes
  [fce66a6a9](https://github.com/pycontribs/ansi2html/commit/fce66a6a905fb6aa006cfa1f6ad4716ebb46e63b)
- Adapt tests to new approach to state
  [49046c620](https://github.com/pycontribs/ansi2html/commit/49046c620079d3a325753081ba99b1deb0c8287a)
- Add CSS classes for lighter font style (2), blinking (5/6), hidden
  text (8)
  [e488daca3](https://github.com/pycontribs/ansi2html/commit/e488daca38176c9cdba7318a958fc79bfb16f9cb)
- Save producing no-op span tags
  [340620f88](https://github.com/pycontribs/ansi2html/commit/340620f88b66a686c16f155465f172321fe39cff)
- Test ANSI codes that just turned supported
  [f4774bcf0](https://github.com/pycontribs/ansi2html/commit/f4774bcf0005175bc00f282f73365fa59b6f47fb)
- Make code testing pairs of files re-usable
  [f95ca305d](https://github.com/pycontribs/ansi2html/commit/f95ca305dba5951c25178fc12fb0e206120aa1b4)
- Add testcase for output from \"eix -I svn -F\"
  [e3f593671](https://github.com/pycontribs/ansi2html/commit/e3f59367174fb9ed4df2d19ed012bae45f0ce2ce)
- Merge pull request #31 from hartwork/font-style-italic
  [a25950fe6](https://github.com/pycontribs/ansi2html/commit/a25950fe6f0bdd12c92cbbd2109655bfd1cc5a36)
- Tweak for py3 support.
  [9766508e1](https://github.com/pycontribs/ansi2html/commit/9766508e16007fdcd764ba52c79af798d8d816fd)
- Add py3.3 to travis config.
  [ceef1eb8e](https://github.com/pycontribs/ansi2html/commit/ceef1eb8e83a58fe895f67185f4242b8e49f7b7c)
- Merge branch \'stateful\' into develop
  [29868b6ec](https://github.com/pycontribs/ansi2html/commit/29868b6ec1e742a23e3b60db17f187ce75bb3d57)
